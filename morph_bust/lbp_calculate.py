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

The lbp_calculate module provides functions to convert a given image step by step into a binary skeleton.

"""
from PIL import Image

"""A list of (y,x) positions of all neighbours of a pixel."""
__pixel_neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def load_image(image_path: str):
    """

    :param image_path: the path + name of the image.
    :return: the image object, converted to a grayscale image.
    :raises FileNotFoundError
    """
    image = Image.open(image_path)
    return image.convert("LA")


def calculate_lbp_pattern(img: Image.Image, x: int, y: int):
    """
    Calculates the lbp pattern for a single pixel in a given pixel matrix and returns the pattern as an list,
    e.g [1,0,0,0,1,0,1,0]

    :param img: The pillow image object we run the calculations on.
    :param x: the x position of the pixel we want to calculate the pattern for.
    :param y: the y position of the pixel we want to calculate the pattern for.
    :return a list with binary values (LBP pattern of the pixel at the given position).
    """
    lbp_pattern = []
    for y_n, x_n in __pixel_neighbours:
        y_neighbour = y_n + y
        x_neighbour = x_n + x

        if x_neighbour < 0 or y_neighbour < 0:
            raise IndexError("The x and y coordinates can not be directly at the image border.")

        neighbour_brightness = img.getpixel((x_neighbour, y_neighbour))
        pixel_brightness = img.getpixel((x, y))
        lbp_pattern.append(__decide_lbp_1_or_0(pixel_brightness, neighbour_brightness))

    return lbp_pattern


def calculate_lbp_pattern_for_complete_image(img: Image.Image):
    """
        Creates a complete new 2D Matrix out of a given brightness matrix. The new matrix contains the lbp pattern for
        every pixel, expect the once at the direct border.
    :param img: The pillow image object we run the calculations on.
    :return: a 2d matrix, where every cell holds a list of binary values.
    """
    """ """
    lbp_pattern_matrix = __init_2d_matrix_with_none(img.width, img.height)

    for y in range(img.height):
        for x in range(img.width):
            if not __is_coordinates_in_lbp_calculation_range(x, y, img.width, img.height):
                lbp_pattern_matrix[y][x] = []  # The pixel at the direct border get a empty lbp_pattern.
                continue
            lbp_pattern = calculate_lbp_pattern(img, x, y)
            lbp_pattern_matrix[y][x] = lbp_pattern

    return lbp_pattern_matrix


def convert_lbp_matrix_to_binary_skeleton(lbp_matrix: list):
    """
        Converts a given 2D matrix with lbp-patterns, into a 2D matrix which holds only 1s and 0s, depending on the
        morph relevance of the pattern in each field.
    :param: lbp_matrix: a 2d list with a lbp_pattern (binary list with len == 8) in each cell.
    :return: a 2d list which only contains 1s and 0s in every cell.
    """
    height = len(lbp_matrix)
    width = len(lbp_matrix[0])
    binary_skeleton = __init_2d_matrix_with_none(width, height)

    for y in range(height):
        for x in range(width):
            morph_relevant = is_lbp_pattern_morph_relevant(lbp_matrix[y][x])
            binary_skeleton[y][x] = morph_relevant

    return binary_skeleton


def is_lbp_pattern_morph_relevant(lbp_pattern: list):
    """ Only lpb-pattern with exact 2 1s, where both 1s are direct neighbours, are relevant, e.g. [0,1,1,0,0,0,0,0]."""
    sum_of_1s = 0
    has_neighbours = False
    for index in range(len(lbp_pattern)):
        sum_of_1s += lbp_pattern[index]
        if sum_of_1s > 2:
            return False
        if lbp_pattern[index] == 1 and lbp_pattern[index - 1] == 1:
            has_neighbours = True
    return has_neighbours


def __decide_lbp_1_or_0(pixel_brightness: float, neighbour_brightness: float):
    """
        Decides if the lbp value for a pair of central-, and neighbour- pixel has the lbp value 1, or 0.
    :param pixel_brightness: the value of the center pixel.
    :param neighbour_brightness: the value of one neighbour pixel.
    :return:
    """
    if neighbour_brightness >= pixel_brightness:
        return 1
    else:
        return 0


def __is_coordinates_in_lbp_calculation_range(x: int, y: int, width: int, height: int):
    """
        Checks if a lbp-calculation for the given coordinates is possible.
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    if x <= 0 or y <= 0:
        return False
    if x >= width - 1 or y >= height - 1:
        return False
    else:
        return True


def __init_2d_matrix_with_none(width: int, height: int):
    """
        Initializes a 2d matrix with the value None.
    :param width:
    :param height:
    :return: a 2d matrix.
    """
    matrix = [[None for _ in range(width)] for _ in range(height)]
    return matrix
