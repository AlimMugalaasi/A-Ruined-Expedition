import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#------------------------------------------------------
clr() #TST

def start_interaction():
    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('Beware.\n', 'italic white')
    newline()

    type('YOU: ', 'bold')
    type('What?\n')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('Beware...\n', 'bold italic red')
    newline()

    type('YOU: ', 'bold')
    type('Beware what? is this some kind of joke?\n')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('The artifact you seek is at the Summit of ')
    type('Dark-Back Mountain', 'italic blue')
    type('.\n')
    newline()

    type('YOU: ', 'bold')
    type('I know that. Why are you telling me this? Do you work for the same company as me?\n')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('There are')
    type(' treasure hunters', 'yellow')
    type(' also trying to collect that artifact. They are just as powerful as you, ')
    type('PLAYER NAME...\n', 'bold magenta')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('Therefore, ')
    type('beware, ', 'bold italic red')
    type('and be prepared.\n')
    newline()

    type('YOU: ', 'bold')
    type('Ok- who are you? How do you know about me? Are you')
    type(' a spy?!\n', 'yellow')
    newline()

    type('YOU: ', 'bold')
    type('You', 'italic')
    type(" wrote that note, didn't you?\n")
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('...\n')
    newline()

    type('YOU: ', 'bold')
    type('ANSWER ME!\n', 'bold red')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type('...\n')
    newline()

    type('YOU: ', 'bold')
    type('Fine. If you tell anyone about me- I will ')
    type('end you.\n', 'red')
    newline()

    type('ANONYMOUS CIVILIAN: ', 'bold')
    type("...I'd get going if I were you.\n")
    newline()