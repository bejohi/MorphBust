"""
MorphBust - A program to detect manipulation (morphing) in images.
Copyright (C) 2017 Jasper Ben Orschulko, Jonas Hielscher, Philip Wiegratz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import sys
from skimage import io as img_io
from log import Log
import dlib


class FaceDetector:
    """ Provides functions to detect exactly one face in an image, which will be loaded from the given file path."""

    __dlib_face_detector = dlib.get_frontal_face_detector()
    __upsample_times = 1  # Defines how often the image will be upsampled, before the detection algorithm acts.


    def __init__(self, img_path: str):
        self.origin_img_path = img_path

        self.img = self.__load_img(img_path)
        self.__detection_obj, self.face_coordinates = self.__detect_face()

    def get_face_img(self):
        """
        :return: A new image object which shows the found face.
        """
        left = self.face_coordinates[0]
        top = self.face_coordinates[1]
        right = self.face_coordinates[2]
        bottom = self.face_coordinates[3]
        face_img = self.img[top:bottom, left:right]
        return face_img

    def save_face(self, full_save_path: str = None, delete_origin: bool = False):
        """
            Saves the face as a new image on the harddrive.
        :param delete_origin: If true the origin image will get deleted.
        :param full_save_path: The path + name of the new image
        :return:
        """
        if full_save_path is None:
            full_save_path = self.__create_name_for_face_img()
        elif self.check_if_jpg(full_save_path) is False:
            Log.face_detection.error(
                str(FaceDetector.__detect_face.__name__) + ": not a .jpg image path: " + str(full_save_path))
            return

        try:
            img_io.imsave(full_save_path, self.get_face_img())

            if delete_origin:
                os.remove(self.origin_img_path)

            success_msg = str(FaceDetector.__detect_face.__name__) + ": face img successfully saved: " + str(
                full_save_path)
            print(success_msg)
            Log.face_detection.info(success_msg)

        except FileExistsError:
            error_message = str(FaceDetector.__detect_face.__name__) + ": the image already exists: " + str(
                full_save_path)
            Log.face_detection.error(error_message)
            raise FileExistsError(error_message)
        except FileNotFoundError:
            error_message = str(FaceDetector.__detect_face.__name__) + ": origin image not found for deletion: " \
                            + self.origin_img_path
            Log.face_detection.error(error_message)
            raise FileExistsError(error_message)

    def __create_name_for_face_img(self):
        """
        :return: The origin image path with the additional keyword 'face' in it.
        """
        return self.origin_img_path.replace(".jpg", "face.jpg").replace(".jpeg", "face.jpeg")

    def __detect_face(self):
        """
             Detects exactly one image from the image instance.
        :return:the dlib detection object (only for class internal use) and an list of integer values: [left,top,right,bottom]
        :raises ValueError
        """

        detection = self.__dlib_face_detector(self.img, self.__upsample_times)
        if len(detection) == 0:
            error_message = str(FaceDetector.__detect_face.__name__) + ": No face was detected!"
            Log.face_detection.error(error_message)
            raise ValueError(error_message)
        if len(detection) > 1:
            error_message = str(FaceDetector.__detect_face.__name__) + ": More than one face was found!"
            Log.face_detection.error(error_message)
            raise ValueError(error_message)
        for k, d in enumerate(detection):
            return detection, [d.left(), d.top(), d.right(), d.bottom()]

    @staticmethod
    def check_if_jpg(img_path: str):
        """
            Checks (very naively) if the given image_path points to a .jpg image.
        :param img_path: The path to the potential .jpg image.
        :return: True if is an .jpg image, False otherwise.
        """
        return img_path.endswith(".jpg") or img_path.endswith(".jpeg")

    @staticmethod
    def __load_img(img_path):
        """Loads an image from the given source on the hard drive."""
        try:
            if FaceDetector.check_if_jpg(img_path) is False:
                error_message = str(FaceDetector.__load_img.__name__) + ": not an .jpg image: " + str(img_path)
                Log.face_detection.error(error_message)
                raise ValueError(error_message)
            return img_io.imread(img_path)
        except FileNotFoundError:
            error_message = str(FaceDetector.__load_img.__name__) + ": no image was found: " + str(img_path)
            Log.face_detection.error(error_message)
            raise FileNotFoundError(error_message)

    def show_picture_and_shape(self):
        """Shows the image and the face shape on the screen."""
        win = dlib.image_window()
        win.set_image(self.img)
        win.add_overlay(self.__detection_obj)
        win.wait_until_closed()


    def show_face(self):
        """
            Shows the found face on the screen.
        """
        win = dlib.image_window()
        win.set_image(self.get_face_img())
        win.wait_until_closed()


def __get_all_jpg_paths_from_file_path(folder_path: str):
    """
        Returns a list with the paths of all found .png images at the given folder path.
    :param folder_path:
    :return:
    """
    image_list = []
    for file_name in os.listdir(folder_path):
        if FaceDetector.check_if_jpg(file_name) \
                and not file_name.endswith("face.jpg"):  # In case we already created a face img. TODO:[bejohi] Cleanup.
            image_path = folder_path + "/" + file_name
            image_list.append(image_path)
    return image_list


if __name__ == "__main__":
    """Find all images in the given folder, extracts the images and save them."""
    image_folder_path = str(sys.argv[1])
    jpg_img_paths = __get_all_jpg_paths_from_file_path(image_folder_path)
    for jpg_path in jpg_img_paths:
        detector = FaceDetector(jpg_path)
        detector.save_face()

