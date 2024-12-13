import Area1.Area1_map as A1, Area2.Area2_map as A2, Area3.Area3_map as A3, Area4.Area4_map as A4, TheSummit.Area5 as summit
import pyfiglet, os, sys
from time import sleep
from rich.console import Console
console = Console()
from ExtraFunctions import type, printc, clrline, clr

'''
also nees installed

keyboard
pyfiglet
rich
that movement thingy
'''

#----------------------------------------------------------------------------------

clr()

printc('[bold]Hello Player![/bold] Before we start, please Make sure you have the terminal opened in a seperate window.')
print("in VS code, just click the terminal name and click the option 'move terminal into new window'")
print('You may have to quit and reload the terminal again, then in the terminal you just type in python main.py to start the game again.')
input('Set it to full screen (f11) and press Enter when ready!')

clr()
print('Loading...')
sleep(0.3)
clr()

#Title screen
sleep(0.7)
pyfiglet.print_figlet("           A", font="slant", colors='white')
sleep(0.7)
pyfiglet.print_figlet("  R U I N E D", font="slant", colors='red')
sleep(0.7)
pyfiglet.print_figlet("EXPEDITION",font="slant" ,colors='white')
sleep(0.7)
type('A GAME BY ALIM MUGALAASI', "bold green", 0.07)
print('\n')
sleep(0.5)
input(type('Press Enter to continue...', 'bold blue'))

#Printing out the storyline from its file
clr()
type('STORYLINE: (X to skip)', 'italic bold white')
input(type('\nPress Enter to continue...', 'bold blue'))
clrline()
print(' ')


with open('storyline.txt', 'r') as file:
    for line in file:
        type(line.strip(),None)
        input(type('\nPress Enter to continue...', 'bold blue', 0.01))
        clrline()
        print(' ')

'''
import keyboard

# Example: Check if 'X' is pressed
if keyboard.is_pressed('x'):
    print("The 'X' key was pressed!")
'''

        
        
        




