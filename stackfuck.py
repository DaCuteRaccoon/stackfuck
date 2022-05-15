# -*- coding: utf-8 -*-

NAME = 'StackFuck Interpreter'
DEVELOPER = 'DaCuteRaccoon'
VERSION = '1.0'
DESCRIPTION = 'Interpreter for the StackFuck programming language.'

import imp
import sys
import glob
from os.path import join, basename, splitext

allnums = '0123456789.'
cmd_dict = {}
