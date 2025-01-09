import sys
import os
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Functions import type, newline, clr, sleep

#--------------------------------------------------------------------------

def interaction():
    type('MIKA: ', 'bold white')
    type('Hey! Can I get some help?\n')
    newline()

    type('YOU: ', 'bold white')
    type('Sure')