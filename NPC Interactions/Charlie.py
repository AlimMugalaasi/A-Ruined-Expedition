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
    type('Hey there stranger! ', ' italic green')
    type('It seems you would like to pass over this ')
    type('bridge...\n', 'italic blue')
    newline()

    type('CHARLIE: ', 'bold')
    type("I'm the owner, Charlie. Let me just look for the key- \n")
    newline()

    type('CHARLIE: ', 'bold')
    type('Hmm... It seems like I may have left the key at my house...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type("Do you think you could get it for me?\n")
    newline()

    type('YOU: ', 'bold')
    type('Well... Its not like I have a choice, do I.\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Oh yeah... Anyway, here is the ')
    type('key ', 'bold yellow')
    type('to my house.\n')
    newline()

def start_interaction2():
    type('CHARLIE: ', 'bold')
    type('Oh, you actually found it...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('I really thought I had lost that key- I would have been in deep trouble with the authorities had I not found it.\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Thank you so much! I owe you one.\n')
    newline()

def start_interaction3():
    type('CHARLIE: ', 'bold')
    type('Hey stranger! ', 'italic')
    type('Over here!\n')
    newline()

    type('YOU: ', 'bold')
    type('Charlie?\n', 'bold blue')
    newline()

    type('CHARLIE: ', 'bold')
    type('Yes, its me. Remember when I told you I owed you one?\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Yeah...\n')
    newline()

    #TBC
