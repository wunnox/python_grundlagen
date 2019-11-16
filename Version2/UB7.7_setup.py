#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibm.py")
)
