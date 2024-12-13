import Area1.Area1_map as A1, Area2.Area2_map as A2, Area3.Area3_map as A3, Area4.Area4_map as A4, TheSummit.Area5 as summit
import Area1.Area1_seq as A1s, Area2.Area2_seq as A2s, Area3.Area3_seq as A3s, Area4.Area4_seq as A4s
import pyfiglet, keyboard
from time import sleep
from rich.console import Console
console = Console()
from ExtraFunctions import type, printc, clrline, clr, ld
import AreaNavigation as anv
#----------------------------------------------------------------------------------
clr()

#The user needs some things like pyfiglet installed via terminal before the game can run - this instructs them to do so
printc('[bold]Hello Player![/bold] Before we start a few things need to be done for the game to run:')
print('1. You must have the following installed:\n\nkeyboard\npyfiglet\nrich\nquestionary\n\nThese can be done in the terminal by running the pip install command.')
print('\n2. Please Make sure you have the terminal opened in a seperate window.')
print("In VS code, just click the terminal name and click the option 'move terminal into new window'")
print('I recommend you run this on Visual Studio Code (can be done via GitHub) if you can, as some things might not work on other terminals.')
print('\nYou may have to quit and reload the terminal again, then in the terminal you just type in python main.py to start the game again.')
check = input('\nIf you need to quit the programme, type QUIT, or If all the above is done, set the window to full screen (f11) and press ENTER to play!: ')
if check == 'QUIT':
    quit()

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
type('STORYLINE: (X then ENTER to skip)', 'italic bold white')
canc2 = input(type('\nPress Enter to continue...', 'bold blue'))
skipStoryLine = False
if canc2 == 'x' or canc2 == 'X':
    skipStoryLine = True
clrline()
print(' ')

if not skipStoryLine:
    with open('storyline.txt', 'r') as file:
        for line in file:
            type(line.strip(),None)
            canc = input(type('\nPress Enter to continue...', 'bold blue', 0.01))
            if canc == 'x' or canc == 'X':
                break
            else:
                clrline()
                print(' ')
                continue

clr()
ld()

player_name = input(type('Enter a name for your player!: ',None, 0.01))

#------------------------------------------------------------------------------------------

#LOADING CLASSES AND ELEMENTS

ld(5)

anv.areaNav_ulckA1()


