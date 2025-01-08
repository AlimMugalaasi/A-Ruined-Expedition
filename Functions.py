from rich.console import Console
console = Console()
from rich.text import Text
from time import sleep
import sys, os, termios, tty, time
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

#small puzzle to open chests
codes = [
    "ab2c3", "f4d5e", "gh6i7", "j8k9l", "mn0op",
    "1qrs2", "3tuv4", "5wxy6", "7zab8", "9cdef",
    "gh0ij", "k1lmn", "2opqr", "s3tuv", "4wxyz",
    "5abcd", "ef6gh", "7ijkl", "mn8no", "p9qrs",
    "tuvwx", "y0zab", "1cdef", "gh2ij", "kl3mn",
    "o4pqr", "s5tuv", "wx6yz", "ab7cd", "ef8gh",
    "9ijkl", "mn0no", "p1qrs", "t2uvw", "x3yza",
    "4cdef", "gh5ij", "kl6mn", "o7pqr", "s8tuv",
    "wx9yz", "ab0cd", "ef1gh", "ij2kl", "mn3no",
    "p4qrs", "t5uvw", "x6yza", "7cdef", "gh8ij"
]


def open_chest():
    type('Repeat the 5-character code that breifly apperars to open the chest. You have one chance.\n', 'yellow', 0.004)
    questionary.press_any_key_to_continue('Press any key to begin...').ask()
    clrline()
    code = random.choice(codes)
    codes.remove(code)
    type(f'{code}\n', 'bold green', 0.2)
    clrline()
    user_code = input('Enter Code: ')
    if user_code == code:
        printc('-ACCEPTED-', 'bold green')
        sleep(0.7)
        return True
    else:
        printc('-DENIED-', 'bold red')
        sleep(0.7)
        return False


#clearing multiple lines

def clrlines(lines):
    for i in range(lines):
        clrline()

#printing navigation help (made it here just to decrease amount of lines used)

def nav():
    printc('''
          
      W     
      ▲      
 A ◄──┼──► D | Use the 'Position: ' indicator to determine your position relative to the map.
      ▼     
      S     
           
''')

#typing out a string in rainbow colors (made this for one cause only but put it as a function becausue why not?)
def rainbow_type(string, speed):
    colors = ['red', 'rgb(255,165,0)', 'yellow', 'green', 'blue', 'rgb(75,0,130)', 'violet']
    count = 0
    for char in string:
        type(char, f'bold {colors[count]}')
        count +=1
        if count == 7:
            count = 0
        sleep(speed)
        continue

#HP:0...

def no_HP():
    type('HP: \n', 'bold red', 0.4)
    clrline()
    printc('HP: 0', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP:  ', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP: 0', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP:  ', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP: 0', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP:  ', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP: 0', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP:  ', 'bold red')
    sleep(0.3)
    clrline()
    printc('HP: 0', 'bold red')
    sleep(1)


# checking the time that has been played (for the hunter mechanic)

def time_elapsed(script_start_time):
    current_time = time.time()
player_position = (5,-2)
                GameAssets.Player.positionENC = GameAssets.A2Z1_g
                GameAssets.Player.positionDEC = 'A2Z1_G'
    return time_el

#Invisible typing (for some fun gimmicks)

def invisiType():
    user_input = ""
    while True:
        key = get_key()
        if key == '\r':
            break
        if key in ('\x08', '\x7f'):
            user_input = user_input[:-1]
        else:
            user_input += key
    return user_input