import sys
import os
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Functions import type, newline, clr, sleep

#--------------------------------------------------------------------------

def interaction1():
    type('MIKA: ', 'bold white')
    type('Hey! Can I get some help?\n')
    newline()

    type('YOU: ', 'bold white')
    type('Sure, how can I help?\n')
    newline()

    type('MIKA: ', 'bold white')
    type("My fire here is about to go out but I can't go get wood from the forest...\n")
    newline()

    type('YOU: ', 'bold white')
    type('Well...\n')
    newline()

    type('MIKA: ', 'bold white')
    type("...I'm not usually home alone.\n")
    newline()

    type('YOU: ', 'bold white')
    type('...\n')
    newline()

    type('MIKA: ', 'bold white')
    type("Tell you what, I have a chest hidden ")
    type("somewhere in the forest.", 'italic green')      
    type(" If you can help me, I'll let you know the code for it.\n")
    newline()

    type('YOU: ', 'bold white')
    type("Now we're talking. I'll get that wood to you as soon as I can.\n")
    newline()

    type('MIKA: ', 'bold white')
    type("Thanks! Here. I'll open the gate to the surface. Be quick! I don't know how long this fire will last....\n")
    newline()

def interaction2():
    type('MIKA: ', 'bold white')
    type("Aaah, thank you so much, I could be in the dark in a few minutes if it wasn't for you!\n")
    newline()

    type('MIKA: ', 'bold white')
    type("Well, a deal is a deal. The code to that chest is 9abc3. Don't get it wrong, or it'll lock!\n")
    newline()