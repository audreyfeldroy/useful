#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import site
from distutils.sysconfig import get_python_lib

print("Your main site-packages directory:")
print(get_python_lib())

print()

print("All global site-packages directories on your system:")
print(site.getsitepackages())

