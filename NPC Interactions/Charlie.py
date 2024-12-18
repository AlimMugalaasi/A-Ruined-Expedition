import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#------------------------------------------------------
clr() #TST
def start_interaction1():
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

def start_interaction2(): #maybe re-write??
    type('CHARLIE: ', 'bold')
    type('Oh, you actually found it...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('I really thought I had lost that key- No one was going over that bridge any time soon...\n')
    newline()

    type('YOU: ', 'bold')
    type('Well there it is. Also, you should try not to misplace the key to the only way for people to navigate across this place...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Yeah... thanks again friend!\n')#NEEDS EDITING
    newline()

    type('YOU: ', 'bold')
    type('(Confused) Sure...\n')
    newline()


start_interaction2()


