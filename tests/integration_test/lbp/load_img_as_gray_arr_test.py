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

import unittest

from lbp import load_img_as_gray_arr
import numpy as np


class LoadImgAsGrayArrTest(unittest.TestCase):
    test_img_path = "../../mock_data/example_image_davinci.png"
    test_img_height = 800
    test_img_width = 800

    def test_return_type_is_numpy_array(self):
        # arrange & act
        img = load_img_as_gray_arr(self.test_img_path)

        # assert
        self.assertTrue(isinstance(img, np.ndarray))

    def test_height_and_with_ar_ok(self):
        # arrange & act
        img = load_img_as_gray_arr(self.test_img_path)

        # assert
        self.assertEqual(len(img), self.test_img_height)
        self.assertEqual(len(img[0]), self.test_img_width)

if __name__ == "__main__":
    unittest.main()
