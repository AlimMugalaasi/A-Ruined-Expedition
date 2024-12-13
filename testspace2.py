import os; from time import sleep; import sys
os.system('clear')

def type(line):
    for char in line:
        print(char, end='')
        sys.stdout.flush()
        sleep(0.03)

type('This is a test')


