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

import datetime

__log_path = "log.txt"


def log_info(message: str):
    complete_message = str(datetime.datetime.now()) + ": " + str(message)
    print(complete_message)
    __write_to_log_file(complete_message)


def log_error(message: str):
    complete_message = "ERROR: " + str(datetime.datetime.now()) + ": " + str(message)
    print(complete_message)
    __write_to_log_file(complete_message)


def set_log_path(path: str):
    global __log_path
    __log_path = path


def __write_to_log_file(message: str):
    try:
        log_file = open(__log_path, "a")
        log_file.write(message + "\n")
        log_file.close()
    except FileNotFoundError:
        print("FATAL LOGGING ERROR: Writing fo file " + str(__log_path) + " was not possible")


class Log:
    def init(self, log_path: str):
        pass

