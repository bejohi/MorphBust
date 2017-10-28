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

The visualizer-module helps to visualize image and binary data.
"""

from matplotlib.pyplot import *

from lbp import load_img_as_gray_arr

if __name__ == "__main__":
    """For testing purpose only!"""
    img_path = "../tests/mock_data/morph_example.jpg"
    gray_img = load_img_as_gray_arr(img_path)
    print(gray_img.shape)
    print(gray_img[0])
    imshow(gray_img)
    show()
