import os;import questionary, GameAssets
os.system('clear')
from ExtraFunctions import get_key, clrline

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
                                     CHEST├────────┘               
'''                                      

CRD_A1Z1lckSQ1 = {
    (0, 0): "Start",
    (1, 0): 'A',
    (1 ,1): 'House',
    (2, 0): '[!]'
}

player_position = (0, 0)

def move_player(direction):
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

    if new_position in CRD_A1Z1lckSQ1:
        player_position = new_position
        clrline()
        print(f"Position: {CRD_A1Z1lckSQ1[new_position]}")
    else:
        return

# Test the movement
def move_input():
    print("-WASD to move-\n")
    print('Position: Start')
    while True:
        key = get_key()
        move_player(key)


move_input()
#game_world.append[(2,1):'lake']