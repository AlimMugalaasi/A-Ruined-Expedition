import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#------------------------------------------------------
clr() #TST
def interaction1():
    type('CHARLIE: ', 'bold')
    type('Hey there stranger! ', ' italic green')
    type('It seems you would like to pass over this ')
    type('bridge...\n', 'italic blue')
    newline()

    type('CHARLIE: ', 'bold')
    type("I'm the guard, Charlie. Let me just look for the key- \n")
    newline()

    type('CHARLIE: ', 'bold')
    type("OH NO! I CAN'T FIND THE KEY!\n", 'bold yellow')
    newline()

    type('CHARLIE: ', 'bold')
    type("If that key is really lost I am going to be in deep trouble with the ")
    type('authorities...\n', 'italic red')
    newline()

    type('YOU: ', 'bold')
    type('Maybe I can help?\n')
    newline()

    type('CHARLIE: ', 'bold')
    type("Really? I would be really grateful if you could. That key could be anywhere and I'm not as agile as you.\n")
    newline()

    type('CHARLIE: ', 'bold')
    type("Here is the ")
    type('key ', 'bold yellow')
    type('to my house. If it is anywhere, it should be somewhere in there.\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Thanks again stranger!\n')
    newline()


def interaction2():
    type('CHARLIE: ', 'bold')
    type('Oh, you actually found it...\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('I really thought I had lost that key- I would have been in deep trouble with the ')
    type('authorities ', 'italic red')
    type('had I not found it. Thank you so much!\n')
    newline()

    type('CHARLIE: ', 'bold')
    type('Here. Take this ')
    type('spear', 'bold green')
    type(". There aren't many nice people around here...\n")
    newline()

    type('YOU: ', 'bold')
    type("Thanks Charlie, I'm sure this will be of great use. Keep that key safe.\n")
    newline()
