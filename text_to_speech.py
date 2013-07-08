#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks for coffee using different Python modules.

Requires macspeechX module:
* https://pypi.python.org/pypi/macspeechX/
* http://old.nabble.com/Re:-py-access-to-speech-synth--p18845607.html
"""

from macspeechX import SpeakString
import pyttsx

# Using macspeechX
# Note: sometimes doesn't work. It's a bit unpredictable.
# Seems to work in the Python interactive shell only.
SpeakString("Can you please make me some coffee, dearest?")
SpeakString("Please?")
SpeakString("Perché è questo caffè così amaro?")

# Using pyttsx
engine = pyttsx.init()
engine.say('Can you please get me some coffee?')
engine.say('Please?')

# Note: looks like it doesn't work with accented characters (yet)
engine.say("Perché è questo caffè così amaro?")

engine.runAndWait()
