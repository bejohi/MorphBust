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
from PIL import Image

from log import Log


def convert_png_to_jpg(png_img_path: str, delete_old_img: bool = False):
    try:
        img = Image.open(png_img_path)
    except FileNotFoundError:
        error_message = str(convert_png_to_jpg.__name__) + ": no image was found: " + str(png_img_path)
        Log.face_detection.error(error_message)
        raise FileNotFoundError(error_message)


def __extract_img_name_from_path(img_path: str):
    pass
