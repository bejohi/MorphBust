#! /usr/bin/env python3

import argparse
import datetime
from pathlib import Path


home = str(Path.home())
now = datetime.datetime.now()
timestamp = str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)

parser = argparse.ArgumentParser(description='MorphBust - detect manipulation (morphing) in password images.')
parser.add_argument('imagepaths', metavar='ImagePath', nargs='+',
                    help='add (multiple) image file paths to be examinated')
parser.add_argument('-l', '--log', default=home+'/morphbust_'+timestamp+'.log',
                    help='change log file path (by default the log file is stored in your home directory)')
parser.add_argument('-r', '--raw', action='store_true',
                    help='disable face detection and croping (might result in long calculations)') 
parser.add_argument('-v', '--verbose', action='store_true',
                    help='enable verbose output')
args = parser.parse_args()

