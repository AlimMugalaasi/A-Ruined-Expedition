import Area1.Area1_map as A1, Area2.Area2_map as A2, Area3.Area3_map as A3, Area4.Area4_map as A4, TheSummit.Area5 as summit
import pyfiglet, os, rich, sys
from time import sleep
from rich.console import Console
console = Console()
from rich.text import Text


#----------------------------------------------------------------------------------
os.system('clear')


#Function that creates a typewriter animation for printing strings
def type(line, style):
    line = Text(line)
    line.stylize(style)
    for char in line:
        console.print(char, end='')
        sys.stdout.flush()
        sleep(0.03)

def print(string, style):
    console.print(string, style=style )
    

#Title screen
pyfiglet.print_figlet("           A", font="slant", colors='white')
pyfiglet.print_figlet("  R U I N E D", font="slant", colors='white')
pyfiglet.print_figlet("EXPEDITION",font="slant" ,colors='white')


print('A GAME BY ALIM MUGALAASI', "green")
