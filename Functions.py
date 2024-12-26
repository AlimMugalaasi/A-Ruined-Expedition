from rich.console import Console
console = Console()
from rich.text import Text
from time import sleep
import sys, os, termios, tty
import random, questionary
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

#Using rich to sylise text
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

#simulating loading
def ld(counts=None):
    clr()
    if counts is None:
        counts = 100
    for i in track(range(counts), description=printc('LOADING...', 'bold green' )):
        timing = random.uniform(0.01, 0.3)
        sleep(timing)
    sleep(0.3)
    clr()

#Adding a new line in a conversation
def newline():
    questionary.press_any_key_to_continue().ask()
    clrline()
    print(' ')

#Detecting a keypress (Without causing problems related to OS - which is why I had to source this)
def get_key_unix():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_key_windows():
    import msvcrt
    return msvcrt.getch().decode('utf-8')

def get_key():
    if os.name == 'nt':
        return get_key_windows()
    else:
        return get_key_unix()
