import sys,os
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline, printc, clr, move_player, type
import Area1_map

#-----------------------------------------------------------

CRD_A1Z1lckSQ1 = {
    (0, 0): GameAssets.A1Z1_Start,
    (1, 0): GameAssets.A1Z1_a,
    (1 ,1): GameAssets.A1Z1_House,
    (2, 0): GameAssets.A1Z1_BridgeLCK
}

def game_A1Z1lckSQ1():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start'
    while True:
        clr()
        map = Area1_map.A1Z1_lckSQ1
        printc(map)
        printc("-WASD to move-\n", 'bold')
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        
        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        clrline()
                        global Action
                        Action = action
            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A1Z1lckSQ1, player_position)
                
                
            elif key == 'I' or key == 'i':
                startPos == GameAssets.Player.positionDEC
                GameAssets.player.open_inventory(GameAssets.Player)
                clr()
                break
            elif key == 'E' or key == 'e':
                if Action == 'E - Interact':
                    if GameAssets.Player.activeSQ == 'None':
                        GameAssets.NPC_Charlie.interact(1)
                        GameAssets.Player.add_item(GameAssets.Charlie_House_key)
                        GameAssets.SQ1.start_sq(GameAssets.Player)
                        player_position = (2,0)
                        startPos = '[!]'
                        break
                    elif GameAssets.Player.activeSQ == 'SQ1':
                        if 'Bridge Key' in GameAssets.Player.inventoryDEC:
                            GameAssets.NPC_Charlie.interact(2)
                            GameAssets.Player.remove_item('Bridge Key')
                            GameAssets.Player.remove_item("Charlie's House Key")
                            GameAssets.Player.add_item('Spear')
                            GameAssets.SQ1.complete_sq(GameAssets.Player)
                            return
                        else:
                            GameAssets.NPC_Charlie.interact(3)
                            player_position = (2,0)
                            startPos = '[!]'
                            break
                elif Action == 'E - Enter House':
                    if GameAssets.Player.item_equippedDEC == "Charlie's House Key":
                        input('IN HOUSE')
                        player_position = (1,1)
                        startPos = 'House'
                        break

                    elif GameAssets.Player.item_equippedDEC != "Charlie's House Key":
                        type('You need to ')
                        type('equip ', 'blue')
                        type('the key to use it!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrline()
                        clrline()

                    elif "Charlie's House Key" not in GameAssets.Player.inventoryDEC: #EDIT THIS - KEY MUST BE EQUIPPED
                        type('You need a ')
                        type('key ', 'bold yellow')
                        type('to do that!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrline()
                        clrline()
                    
                    
        continue




game_A1Z1lckSQ1()
print('Done')
    
#DROPPING ITEMS MUST BE DONE BEFORE WE MOVE ON EVEN IF IT WONT HAPPEN HERE
