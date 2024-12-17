import os;import questionary





os.system('clear')


'''
# Grid-based world
game_world = {
    (0, 0): "Starting Point",
    (0, 1): "Forest",
    (1, 0): "Cave Entrance",
    (1, 1): "River",
    (0,-1): 'idk'
}

player_position = (0, 0)

def move_player(direction):
    global player_position
    x, y = player_position
    if direction == "north":
        new_position = (x, y + 1)
    elif direction == "south":
        new_position = (x, y - 1)
    elif direction == "east":
        new_position = (x + 1, y)
    elif direction == "west":
        new_position = (x - 1, y)
    else:
        print("Invalid direction!")
        return

    if new_position in game_world:
        player_position = new_position
        print(f"You moved to {game_world[new_position]}.")
    else:
        print("You can't go that way!")

# Test the movement
while True:
    gg=input('input: ')
    move_player(gg)
'''

'''
game_world = {
    (0, 0): "Starting Point",
    (0, 1): "Forest",
    (1, 0): "Cave Entrance",
    (1, 1): "River",
    (0,-1): 'idk'
}

game_world.append[(2,1):'lake']

'''



#---------------------------------------

'''

from ExtraFunctions import type, clr, clrline
import questionary, sys

clr()

line1 = 'CHARLIE: this is an example'
line2 = 'are you sure?'
line3 = 'yes. I am SURE this is an example'
conversation = []
conversation.append(line1)
conversation.append(line2)
conversation.append(line3)


countA = 0
countB = 1

outOfRangeA = False
outOfRangeB = False

while True:
    if outOfRangeA == True:
        break
    else:
        type(conversation[countA])
        countA += 2
        print(' ')
        questionary.press_any_key_to_continue().ask()
        clrline()
        print(' ')
        if countA > (len(conversation) -1):
            outOfRangeA = True

    if outOfRangeB == True:
        break
    else:
        type(conversation[countB])
        countB += 2
        print(' ')
        questionary.press_any_key_to_continue().ask()
        clrline()
        print(' ')
        if countB > (len(conversation) -1):
            outOfRangeB = True

            '''

