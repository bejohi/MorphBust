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

import logging
import os
import errno


class LogManager:
    def init(self, debug, logpath):
        self.logger = logging.getLogger()
        self.logger.name = 'MorphBust'
        self.ch = logging.StreamHandler()
        os.makedirs(os.path.dirname(logpath), exist_ok=True)
        self.fh = logging.FileHandler(logpath)
        if debug == 'True':
            self.logger.setLevel(logging.DEBUG)
            self.ch.setLevel(logging.DEBUG)
            self.fh.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
            self.ch.setLevel(logging.INFO)
            self.fh.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.ch.setFormatter(self.formatter)
        self.fh.setFormatter(self.formatter)
        self.logger.addHandler(self.ch)
        self.logger.addHandler(self.fh)

    def __getattr__(self, name):
        return logging.getLogger(name)


Log = LogManager()
