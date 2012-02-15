#!/usr/bin/env python

# Metitation timer
# Version 0.2
# 2011-12-15

# Statue sits, quiet
# unending meditation
# expression of bliss

"""
Metitation timer
A tool to assist in the practice of mindfullness

Usage:
    meditation_timer.py [period] [delay]

The meditation period duration and the initial delay, in minutes, are optional.
If ommited, they default to a meditation period of 30 minutes and a preparation
delay of 1.3 minutes, or 78 seconds.
"""

LICENCE = """
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

# Importing modules
import sys
import getopt
import os
from os.path import join, dirname
from time import time, sleep
try:
    import pygame
except:
    print "Python module 'pygame' is required, please install it"
    sys.exit(1)

# Defining global variables
if dirname(__file__) == "/usr/local/bin":
    DATA_PATH = "/usr/share/meditation-timer/data"
elif dirname(__file__) == ".":
    DATA_PATH = "./data"
else:
    print "Cannot launch Meditation-timer."
    print "Read the installation procedure in the README file."

# Defining functions
def wait(duration):
    """Wait a certain number of minutes
    """
    time_end = time() + float(duration) * 60
    time_diff = time_end - time()
    while time_diff > 0:
        sleep(1)
        time_diff = time_end - time()

def _play_chime():
    """Play a sound file once
    """
    pygame.init()
    pygame.mixer.music.load(join(DATA_PATH, "bowl.ogg"))
    pygame.mixer.music.play()
    sleep(10)

def print_text_file(ascii_file):
    """Print the content of a text file, for example ascii art
    """
    ascii_data = open(ascii_file)
    print "\n" * 69
    for line in ascii_data:
        print line,
    print

def timer(period=30, delay=1.3):
    """Meditation timer. Sound a bell after an initial delay and at the end of
the meditation period, both given in minutes
    """
    print_text_file(join(DATA_PATH, "buddha0.txt"))
    wait(3./60)
    print_text_file(join(DATA_PATH, "buddha1.txt"))
    wait(delay)
    print_text_file(join(DATA_PATH, "buddha2.txt"))
    for i in range(3):
        _play_chime()
    print_text_file(join(DATA_PATH, "buddha.txt"))
    wait(period)
    _play_chime()
    print_text_file(join(DATA_PATH, "buddha3.txt"))

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        if opts[0][0].lower() in ["-h", "-help", "--help"]:
            print __doc__
            sys.exit(0)
    except getopt.error, msg:
        print __doc__
        sys.exit(1)
    timer(*args)

if __name__ == "__main__":
    main()