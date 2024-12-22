import os;import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline

def test_map():
    print(
        '''                                                          
                   HOUSE                                           
                     ┬                                             
                     │      ┌ ┐                                    
                     │       !                                     
                     │      └ ┘                                    
 START├──────────────A──────────  ─  ─  ─  ─  ─────B────────────┤► 
                                                   │               
                                                   │               
                                                   │               
                                                   │               
                                                   │               
                                     CHEST├────────C               
'''                                      
    )



CRD_A1Z1lckSQ1 = {
    (0, 0): GameAssets.A1Z1_Start,
    (1, 0): GameAssets.A1Z1_a,
    (1 ,1): GameAssets.A1Z1_House,
    (2, 0): GameAssets.A1Z1_BridgeLCK
}

player_position = (0, 0)

# TO BE MOVED TO FUNCTIONS
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
        print(f"Position: {coordinate_sys[new_position].name}")
        GameAssets.Player.position = coordinate_sys[new_position].code
    else:
        return

# TO BE MOVED TO FUNCTIONS
def move_input(startPos):
    print("-WASD to move-\n")
    print(f'Position: {startPos}')
    while True:
        key = get_key()
        if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
            move_player(key, CRD_A1Z1lckSQ1)
        elif key == 'E' or key == 'e':
            GameAssets.player.open_inventory()
        else:
            #action check?
            pass

test_map()
move_input('Start')

#game_world.append[(2,1):'lake']

#Action check - function exclusive to each sequence that checks any available actions that the player can do.