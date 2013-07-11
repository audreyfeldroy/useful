#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""Asks for coffee using different Python text-to-speech modules.
"""

import pyttsx

def ask_for_coffee_mac():
    """
    Use macspeechX to synthesize speech asking for coffee.
    Note: sometimes doesn't work. It's a bit unpredictable.
    Seems to work in the Python interactive shell only.

    .. warning:: You may have trouble importing macspeechX if you're not on a Mac,
        or if you're on a Mac but in a virtualenv without Foundation on your path.

        * https://pypi.python.org/pypi/macspeechX/
        * http://old.nabble.com/Re:-py-access-to-speech-synth--p18845607.html

    """

    from macspeechX import SpeakString
    SpeakString("Can you please make me some coffee, dearest?")
    SpeakString("Please?")
    SpeakString("Perché è questo caffè così amaro?")

def ask_for_coffee():
    """ Use pyttsx to synthesize speech asking for coffee. """
    engine = pyttsx.init()
    engine.say('Can you please get me some coffee?')
    engine.say('Please?')

    # Note: looks like it doesn't work with accented characters (yet)
    engine.say("Perché è questo caffè così amaro?")

    engine.runAndWait()


if __name__ == '__main__':
    ask_for_coffee()
