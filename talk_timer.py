#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import argparse
from time import sleep

import pyttsx


parser = argparse.ArgumentParser(
    description='Presentation timer with spoken warnings.'
)
parser.add_argument(
    'minutes',
    type=int,
    help='Length of talk in minutes'
)
args = parser.parse_args()

print "Timing a {0}-minute talk.".format(args.minutes)

# Sleep for X-minute talk duration
sleep(args.minutes * 60)

# Text to speech
engine = pyttsx.init()
engine.say("Time is up")
engine.runAndWait()

print("Time is up")
