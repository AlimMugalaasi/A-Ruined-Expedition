import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#--------------------------------------------------------