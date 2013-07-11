#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import site
from distutils.sysconfig import get_python_lib


def print_site_packages():
    """ Prints your main global site-packages directory, as well
        as all of your global ones. """
    print("Your main site-packages directory:")
    print(get_python_lib())

    print()

    print("All global site-packages directories on your system:")
    print(site.getsitepackages())


if __name__ == '__main__':
    print_site_packages()
