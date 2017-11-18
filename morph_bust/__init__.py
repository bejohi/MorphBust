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

import argparse
import datetime
from pathlib import Path
from morph_bust.log import Log
from morph_bust.face_detection import FaceDetector


def main():
    home = str(Path.home())
    now = datetime.datetime.now()
    timestamp = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)

    parser = argparse.ArgumentParser(description='MorphBust - detect manipulation (morphing) in images.')
    parser.add_argument('imagepaths', metavar='ImagePath', type=str, nargs='+',
                        help='add (multiple) image file paths to be examinated')
    parser.add_argument('-r', '--raw', action='store_true',
                        help='disable face detection and cropping (might result in long calculations)')
    parser.add_argument('-l', '--log', default=home + '/morphbust/morphbust_' + timestamp + '.log',
                        help='change log file path (by default the log file is stored in your home directory)')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='enable debugging for more detailed output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0.1',
                        help='show programs version number and exit')
    args = parser.parse_args()

    Log.init(args.debug, args.log)
    Log.logger.info('Program started.')
    Log.logger.debug('Debugging is set to ' + str(args.debug) + '.')


if __name__ == "__main__":
    main()
