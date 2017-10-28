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


class IntegrationTestBase:
    """Stores information and provides methods which are necessary trough a great number of integration tests."""
    test_img_path = "../../mock_data/example_image_davinci.png"
    test_img_height = 800
    test_img_width = 800
    morph_img_path = "../../mock_data/morph_example.jpg"
    morph_img_height = 240
    morph_img_width = 480
