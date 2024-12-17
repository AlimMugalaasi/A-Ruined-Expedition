import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#------------------------------------------------------
clr() #TST
def start_interaction():
    type('CHARLIE: ', 'bold')
    type('Hey there! ', ' italic green')
    type('It seems you would like to pass over this ')
    type('bridge...\n', 'italic blue')
    newline()

    type('CHARLIE: ', 'bold')
    type('Let me just look for the key- \n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Hmm... It seems like I may have left the key at my house...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type("Do you think you could get it for me? I don't really feel like moving...\n")
    newline()

    type('YOU: ', 'bold')
    type('Well... Its not like I have a choice, do I.\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Oh yeah... Anyway, here is the ')
    type('key ', 'bold yellow')
    type('to my house. Thanks very much!\n')
    newline()

    type('YOU: ', 'bold')
    type('Whatever...\n')
    newline()

start_interaction()
