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

testList = ['CLOSE','a', 'b','c', 'd', 'e', 'f']

    

    

questionary.select("Select An item to equip it, or select CLOSE to close inventory", choices=testList).ask()

