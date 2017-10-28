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
import log as log
import numpy as np

"""A list of (y,x) positions of all neighbours of a pixel."""
__pixel_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


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
        error_msg = str(load_img_as_gray_arr.__name__) + ": Image " + str(img_path) + " was not found."
        log.log_error(error_msg)
        raise FileNotFoundError(error_msg)


def create_lbp_skeleton(gray_arr: np.ndarray):
    """
    Creates a 2D array of lbp patterns (arrays with binary data and a length of 8) from a given 2D array with gray 
    values. 
    
    Keyword arguments:
        gray_arr -- a 2D image with gray values (typical unit8).
    
    """
    height = len(gray_arr)
    if height is 0:
        return np.empty(0)
    width = len(gray_arr)
    lbp_skeleton = np.array(__init_2d_matrix_with_none(width, height))

    for y in range(height):
        for x in range(width):
            if not __is_coordinates_in_lbp_calculation_range(x, y, width, height):
                continue
            lbp_skeleton[y, x] = create_lbp_neighbour_pattern(gray_arr, x, y)

    return lbp_skeleton


def create_lbp_neighbour_pattern(gray_arr: list, x: int, y: int):
    lbp_pattern = np.empty(8)
    counter = 0
    for y_n, x_n in __pixel_neighbours:
        y_neighbour = y_n + y
        x_neighbour = x_n + x

        if x_neighbour < 0 or y_neighbour < 0:
            raise IndexError("The x and y coordinates can not be directly at the image border.")

        neighbour_value = gray_arr[y_neighbour, x_neighbour]
        pixel_value = gray_arr[y, x]
        lbp_pattern[counter] = __decide_lbp_1_or_0(pixel_value, neighbour_value)
    return lbp_pattern


def __decide_lbp_1_or_0(pixel_value: float, neighbour_value: float):
    """Decides if the lbp value for a pair of central-, and neighbour- pixel has the lbp value 1, or 0."""
    if neighbour_value >= pixel_value:
        return 1
    else:
        return 0


def __is_coordinates_in_lbp_calculation_range(x: int, y: int, width: int, height: int):
    """Checks if a lbp-calculation for the given coordinates is possible."""
    if x <= 0 or y <= 0:
        return False
    if x >= width - 1 or y >= height - 1:
        return False
    else:
        return True


def __init_2d_matrix_with_none(width: int, height: int):
    """Initializes a 2d matrix with the value None."""
    matrix = [[None for _ in range(width)] for _ in range(height)]
    return matrix
