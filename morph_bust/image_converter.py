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
from PIL import Image
from log import Log


def convert_png_to_jpg(png_img_path: str, delete_old_img: bool = False):
    """
        Converts a given png img to a jpg image.
    :param png_img_path: the full path to the .png image.
    :param delete_old_img: if true, the old image will be deleted after convert.
    :return True if the convert was successful, False otherwise.
    :raises FileNotFoundError, FileExistsError
    """
    if __check_if_png(png_img_path) is False:
        return False

    try:
        img = Image.open(png_img_path)
        jpg_path = __convert_png_name_to_jpg_name(png_img_path)
        img.save(jpg_path)

        if delete_old_img:
            os.remove(png_img_path)

        success_msg = str(convert_png_to_jpg.__name__) + ": image successfully converted: " + str(png_img_path)
        print(success_msg)
        Log.face_detection.info(success_msg)
        return True

    except FileNotFoundError:
        error_message = str(convert_png_to_jpg.__name__) + ": no image was found: " + str(png_img_path)
        Log.face_detection.error(error_message)
        raise FileNotFoundError(error_message)
    except FileExistsError:
        error_message = str(convert_png_to_jpg.__name__) + ": .jpg image with the given name all: " + str(png_img_path)
        Log.face_detection.error(error_message)
        raise FileNotFoundError(error_message)


def __convert_png_name_to_jpg_name(img_path: str):
    return img_path.replace(".png", ".jpg")


def __check_if_png(img_path: str):
    """
        Checks (very naively) if the given image_path points to a .png image.
    :param img_path: The path to the potential .png image.
    :return: True if is an .png image, False otherwise.
    """
    return img_path.endswith(".png")


def __get_all_png_paths_from_file_path(folder_path: str):
    """
        Returns a list with the paths of all found .png images at the given folder path.
    :param folder_path:
    :return:
    """
    image_list = []
    for file_name in os.listdir(folder_path):
        if __check_if_png(file_name):
            image_path = folder_path + "/" + file_name
            image_list.append(image_path)
    return image_list


if __name__ == "__main__":
    """Converts all images at the given folder to .jpg images."""
    image_folder_path = str(sys.argv[1])
    png_img_paths = __get_all_png_paths_from_file_path(image_folder_path)
    print(str(len(png_img_paths)) + " .png images where found.")
    for img_path in png_img_paths:
        convert_png_to_jpg(img_path,True)
