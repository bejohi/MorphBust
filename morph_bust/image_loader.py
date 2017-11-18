import os
import imghdr

import sys

from log import Log


def import_image(image_path:str):
    # TODO Write method documentation.
    # TODO Don't exit the system in a function called "image_load", but return an error value or raise an error.
    if os.path.isfile(image_path) is False:
        Log.image_loader.error('File ' + image_path + ' does not exist.')
        sys.exit(1)
    if not imghdr.what(image_path) in ("'png'", "'jpeg'"):
        Log.image_loader.error('File ' + image_path + ' is not a valid image file.')
        sys.exit(1)
