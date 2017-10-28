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

The lbp-module provides functions to calculate the local binary pattern from a given image source.
"""

from PIL import Image
import morph_logging as log
import numpy as np


def load_img_as_gray_arr(img_path: str):
    """
    Loads an image from the hard drive and converts it to an 2D array, which stores the gray values
    for every pixel. Returns a numpy.array. Might raise FileNotFound error.
        
    Keyword arguments:
        img_path -- the image path on the file system.
    """
    try:
        img_gray = Image.open(img_path).convert("L")
        return np.asarray(img_gray)
    except FileNotFoundError:
        error_msg = "Image " + str(img_path) + " was not found."
        log.log_error(error_msg)
        raise FileNotFoundError(error_msg)
