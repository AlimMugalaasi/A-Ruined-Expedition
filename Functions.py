from rich.console import Console
console = Console()
from rich.text import Text
from time import sleep
import sys, os, termios, tty
import random, questionary, GameAssets
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
    
#Moving the player around a map

def move_player(direction, coordinate_sys):
    global player_position
    x, y = player_position
    if direction == "W" or direction =='w':
        new_position = (x, y + 1)
    elif direction == "A" or direction =='a':
        new_position = (x - 1, y)
    elif direction == "S" or direction =='s':
        new_position = (x, y - 1)
    elif direction == "D" or direction =='d':
        new_position = (x + 1, y)
    else:
        return

    if new_position in coordinate_sys:
        player_position = new_position
        clrline()
        printc(f"Position: [bold]{coordinate_sys[new_position].name}[/bold]")
        GameAssets.Player.positionENC = coordinate_sys[new_position]
        GameAssets.Player.positionDEC = coordinate_sys[new_position].code
    else:
        return