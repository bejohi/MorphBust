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

from skimage import io as img_io
import dlib

import log


class FaceDetector:
    """ Provides functions to detect exactly one face in an image, which will be loaded from the given file path."""

    __blib_face_detector = dlib.get_frontal_face_detector()
    __upsample_times = 1  # Defines how often the image well get upsampled, before the detection algorithm acts.

    def __init__(self, img_path: str):
        self.img = self.__load_img(img_path)
        self.__detection_obj, self.face_coordinates = self.__detect_face()

    @staticmethod
    def __load_img(img_path):
        """Loads an image from the given source on the hard drive."""
        try:
            # TODO: bejohi: Check if image is a JPEG Image.
            return img_io.imread(img_path)
        except FileNotFoundError:
            error_message = str(FaceDetector.__load_img.__name__) + ": no image was found: " + str(img_path)
            log.log_error(error_message)
            raise FileNotFoundError(error_message)

    def __detect_face(self):
        """
        Detects exactly one image from the image instance.

        Raises an ValueError if more than one face is found.

        Returns the dlib detection object (only for class internal use) and an list of integer values: [left,top,
        right,bottom].
        """
        detection = self.__blib_face_detector(self.img, self.__upsample_times)
        if len(detection) > 1:
            error_message = str(FaceDetector.__detect_face.__name__) + ": more than one face was found!"
            log.log_error(error_message)
            raise ValueError(error_message)
        for k, d in enumerate(detection):
            return detection, [d.left(), d.top(), d.right(), d.bottom()]

    def show(self):
        """Shows the image and the face shape on the screen."""
        win = dlib.image_window()
        win.set_image(self.img)
        win.add_overlay(self.__detection_obj)
        win.wait_until_closed()


if __name__ == "__main__":
    """For testing purpose only!"""
    path = "../tests/sample_data/001.jpg"
    detector = FaceDetector(path)
    print(detector.face_coordinates)
    detector.show()
