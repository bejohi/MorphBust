import os
import imghdr

import sys


def import_image(image_path:str):
    # TODO Write method documentation.
    # TODO Don't print directly, but use logging instead.
    # TODO Don't exit the system in a function called "image_load", but return an error value or raise an error.
    if os.path.isfile(image_path) is False:
        print("File " + image_path + " does not exist. Terminating.")
        sys.exit(1)
    if not imghdr.what(image_path) in ("'png'", "'jpeg'"):
        print("File " + image_path + "is not a valid image file. Terminating.")
        sys.exit(1)
