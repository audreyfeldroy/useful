#!/usr/bin/env python
# -*- coding: utf-8 -*-

import parawrap


with open('LICENSE', 'r') as license_file:
    strings = license_file.read()

file_string = ''.join(strings)
wrapped_text = parawrap.fill(text=file_string, width=75)

with open('LICENSE', 'w') as license_file:
    license_file.write(wrapped_text)
