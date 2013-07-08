#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from time import sleep
import pyttsx

# Sleep for 5 min lightning talk duration
# TODO: make this a command line arg
sleep(60 * 5)

# Text to speech
engine = pyttsx.init()
engine.say("Time is up")
engine.runAndWait()

print("Time is up")
