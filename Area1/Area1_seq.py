import os;import questionary, GameAssets
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

player_position = (0, 0)

def game_A1Z1lckSQ1():
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
                        global Action
                        Action = action
            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                move_player(key, CRD_A1Z1lckSQ1)
            elif key == 'I' or key == 'i':
                startPos == GameAssets.Player.positionDEC
                GameAssets.player.open_inventory(GameAssets.Player)
                clr()
                break
            elif key == 'E' or key == 'e':
                if Action == 'E - interact':
                    if GameAssets.Player.activeSQ == 'None':
                        GameAssets.NPC_Charlie.interact(1)
                        GameAssets.Player.add_item(GameAssets.Charlie_House_key)
                        GameAssets.SQ1.start_sq(GameAssets.Player)
                        return
                    elif GameAssets.Player.activeSQ == 'SQ1':
                        GameAssets.NPC_Charlie.interact(2)
                        GameAssets.SQ1.complete_sq(GameAssets.Player)
                        return
                    elif Action == 'E - Enter House':
                        type('You need a ')
                        type('key ', 'bold yellow')
                        type('to do that!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrline()
                        clrline()
        continue




game_A1Z1lckSQ1()
if GameAssets.Player.activeSQ == 'SQ1':
    player_position = (2,0)
    print('Now we do A1Z1_ACTIVESQ1')
elif GameAssets.SQ1.complete:
    print('Now Run full unlocked level (charlie goes, house cant go in)')
    
