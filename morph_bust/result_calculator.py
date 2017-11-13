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


def extract_img_info_from_result_file(file_path: str, reduced_set: bool = False):
    """
        Extracts the img nr informations and pixel information from a file with the form:
        "imgNr1_imgNr2_[XXX];lbpRelevantPixel;OverallPixel"
    :param reduced_set: In case the list of images are not morph images, set it True.
    :param file_path: the path to the result txt file on the harddrive
    :return: a list of the form [img_nr_1, img_nr_2, lbp_relevant_pixel, pixel_counter]
    :raises FileNotFoundError
    """
    file = open(file_path)
    all_lines = file.readlines()
    information_arr = []
    for line in all_lines:
        underscore_split = line.split("_")
        img_nr_1 = int(underscore_split[0])
        if not reduced_set:
            img_nr_2 = int(underscore_split[1])
        else:
            img_nr_2 = -1
        semicolon_split = line.split(";")
        lbp_relevant_pixel = int(semicolon_split[1])
        pixel_counter = int(semicolon_split[2])
        average = lbp_relevant_pixel / (pixel_counter / 100)
        information_arr.append([img_nr_1, img_nr_2, lbp_relevant_pixel, pixel_counter, average])
    return information_arr


def get_all_info_about_img_nr(img_nr: int, image_info: list):
    """
        Returns a subset of the given image_info list where only theses lines are included where the given img_nr
        occurred.
    :param img_nr:
    :param image_info:
    :return:
    """
    img_info_matching_list = []
    for img in image_info:
        if img[0] == img_nr or img[1] == img_nr:
            img_info_matching_list.append(img)

    return img_info_matching_list


def get_overall_average_of_list(info_list: list):
    count = 0
    for info in info_list:
        count += info[4]
    return count / len(info_list)


def get_first_img_info_with_matching_number(info_list: list, img_nr: int):
    for info in info_list:
        if info[0] == img_nr or info[1] == img_nr:
            return info

    return None


def calculate_differences_between_morphs_and_origin(morph_info_list: list, origin_info_list: list):
    difference_list = list()

    for morph_info in morph_info_list:
        origin_pic_1 = get_first_img_info_with_matching_number(origin_info_list, morph_info[0])
        origin_pic_2 = get_first_img_info_with_matching_number(origin_info_list, morph_info[1])

        if origin_pic_1 is None or origin_pic_2 is None:
            difference_list.append([str(morph_info[0]) + "+" + str(morph_info[1]), -1, -1])
        else:
            diff_to_1 = origin_pic_1[4] - morph_info[4]
            diff_to_2 = origin_pic_2[4] - morph_info[4]
            difference_list.append([str(morph_info[0]) + "+" + str(morph_info[1]), diff_to_1, diff_to_2])
    return difference_list


if __name__ == "__main__":
    __complete_path = "../result_data/image_scan_result_complete_07.11.2017.csv"
    __combined_path = "../result_data/image_scan_result_combined_11.11.2017.csv"
    __splicing_path = "../result_data/image_scan_result_splicing_07.11.2017.csv"
    __neutral_path = "../result_data/image_scan_result_neutral_13.11.2017.csv"
    complete_info = extract_img_info_from_result_file(__complete_path)
    combined_info = extract_img_info_from_result_file(__combined_path)
    splicing_info = extract_img_info_from_result_file(__splicing_path)
    neutral_info = extract_img_info_from_result_file(__neutral_path, True)

    print("Neutral average: " + str(get_overall_average_of_list(neutral_info)) + " with " + str(
        len(neutral_info)) + " images")
    print("Splicing average: " + str(get_overall_average_of_list(splicing_info)) + " with " + str(
        len(splicing_info)) + " images")
    print("Combined average: " + str(get_overall_average_of_list(combined_info)) + " with " + str(
        len(combined_info)) + " images")
    print("Complete average: " + str(get_overall_average_of_list(complete_info)) + " with " + str(
        len(complete_info)) + " images")

    complete_diff = calculate_differences_between_morphs_and_origin(complete_info, neutral_info)
    combined_diff = calculate_differences_between_morphs_and_origin(combined_info, neutral_info)
    splicing_diff = calculate_differences_between_morphs_and_origin(splicing_info, neutral_info)
    print(str(len(complete_diff)))
    print(str(len(combined_diff)))
    print(str(len(splicing_diff)))
