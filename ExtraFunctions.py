from rich.console import Console
console = Console()
from rich.text import Text
from time import sleep
import sys, os
import random
from rich.progress import track

#---------------------------------------------------------------------------------

#Function that creates a typewriter animation for printing strings
def type(line, style=None, speed=None):
    line = Text(line)
    if style is None:
        line.stylize('white')
    else:
        line.stylize(style)
    for char in line:
        console.print(char, end='')
        sys.stdout.flush()
        if speed is None:
            sleep(0.03)
        else:
            sleep(speed)
    return ''

def printc(string, style=None):
    if style is None:
        console.print(string, style='white' )
    else:
        console.print(string, style=style )
    return ''

#clearing a line from the console
def clrline():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

#clear console
def clr():
    os.system('clear')

def ld(counts=None):
    clr()
    if counts is None:
        counts = 100
    for i in track(range(counts), description=printc('LOADING...', 'bold green' )):
        timing = random.uniform(0.01, 0.3)
        sleep(timing)
    sleep(0.3)
    clr()
