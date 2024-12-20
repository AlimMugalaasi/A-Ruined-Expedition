import sys
import os
# Getting the parent directory of the current folder (so i can import Extra Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from ExtraFunctions import type, newline, clr

#--------------------------------------------------------
clr() #TST


def interaction():
    type('ZEXRASH: ', 'bold white')
    type('Hey you! over there! Can I ask you something?\n')
    newline()

    type('YOU: ', 'bold')
    type('Uhhh... sure? What do you need to know?\n')
    newline()

    type('ZEXRASH: ', 'bold white')
    type("I'm sure you have heard of the rumours of a great ")
    type('artifact ', 'bold yellow')
    type('that many treasure hunters and bounty hunters are looking to claim... know anything about it?\n')
    newline()

    type('YOU: ', 'bold')
    type('Nope. Never heard of it. Just the fact that it is a pretty hard piece to find.')
    newline()

    type('ZEXRASH: ', 'bold')
    type("That's a shame. When I get my hands on that thing, Oh, the ")
    type('riches', 'green')
    type(' I will obtain will be incomparable...\n')
    newline()

    type('YOU: ', 'bold')
    type("...\n")
    newline()

    type('ZEXRASH: ', 'bold')
    type("Hmm... You don't look like you're from around here. What brings you up into the shadow plains?\n")
    newline()

    type('YOU: ', 'bold')
    type("Nothing so important... just.... uuh....collecting something. For a friend.\n")
    newline()

    type('ZEXRASH: ', 'bold')
    type("Sure, but that doesn't explain why you are carrying a spear on your back")
    #TBC