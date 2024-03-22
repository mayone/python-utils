# -*- coding: utf-8 -*-

import os
import sys
import inspect


if not hasattr(sys.modules[__name__], "__file__"):
    # Handle __file__ not defined
    __file__ = inspect.getfile(inspect.currentframe())

dir_path = os.path.dirname(os.path.realpath(__file__))

INPUT_PATH = f"{dir_path}/input.csv"
OUTPUT_FIT_PATH = f"{dir_path}/fit.csv"
OUTPUT_FAT_PATH = f"{dir_path}/fat.csv"
