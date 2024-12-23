import os;import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline, printc, clr

def test_map():
    map = (
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
    return map



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
        printc(f"Position: [bold]{coordinate_sys[new_position].name}[/bold]")
        GameAssets.Player.positionENC = coordinate_sys[new_position]
        GameAssets.Player.positionDEC = coordinate_sys[new_position].code
    else:
        return

# TO BE MOVED TO FUNCTIONS
def move_input(map, startPos):
    while True:
        print(map)
        printc("-WASD to move-\n", 'bold')
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        
        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        clrline()
            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                move_player(key, CRD_A1Z1lckSQ1)
            elif key == 'I' or key == 'i':
                startPos == GameAssets.Player.positionDEC
                GameAssets.player.open_inventory(GameAssets.Player)
                clr()
                break
            else:
                if action == 'E - interact':
                    if GameAssets.Player.activeSQ == 'None':
                        GameAssets.NPC_Charlie.interact(1)
                        GameAssets.Player.activeSQ = 'A1Z1_SQ1'
                    elif GameAssets.Player.activeSQ == 'A1Z1_SQ1':
                        GameAssets.NPC_Charlie.interact(2)
                        GameAssets.Player.activeSQ == 'None'
                        return
        continue

move_input(test_map(),'Start')

#game_world.append[(2,1):'lake']

#We have been able to format it so when we are at positions that have extra functions, it shows them.
#Now we need to programme those extra fucntions for those specific positions
#Action check was a way but it becomes difficult because its only one function that checks for possible actions for all positions that have actions.

#We also need to be able to pick up dropped items from certain positions (there is a dropped_items attribute in positions)