import os;import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline, printc, clr, move_player
import Area1_map

#-----------------------------------------------------------

CRD_A1Z1lckSQ1 = {
    (0, 0): GameAssets.A1Z1_Start,
    (1, 0): GameAssets.A1Z1_a,
    (1 ,1): GameAssets.A1Z1_House,
    (2, 0): GameAssets.A1Z1_BridgeLCK
}

player_position = (0, 0)

def game_A1Z1(): #You might not actually have to put this in a function!!!!!!
    while True:
        map = Area1_map.A1Z1_lckSQ1
        startPos = 'Start'
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
                        return
                    elif GameAssets.Player.activeSQ == 'A1Z1_SQ1':
                        GameAssets.NPC_Charlie.interact(2)
                        GameAssets.Player.activeSQ == 'None'
                        return
        continue

move_input(Area1_map.A1Z1_lckSQ1, 'Start')
if GameAssets.Player.activeSQ == 'A1Z1_SQ1':
    player_position = (2,0)
    
