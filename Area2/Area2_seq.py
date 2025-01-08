import sys,os, time
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline, printc, clr, type, sleep, open_chest, clrlines,ld, invisiType
from ExtraFunctions import move_player, bossBattle
import Area2.Area2_map as Area2_map

#--------------------------------------------------------------------AREA 2 SEQUENCE

#-----------------------------------ZONE 1

CRD_A2Z1_CRT = {
    (0,0) : GameAssets.A2Z1_Crate
}

def game_A2Z1_CRT():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Crate'
    global Actions
    Actions = []
    global solved
    solved = False
    GameAssets.Player.positionENC = GameAssets.A2Z1_Crate
    GameAssets.Player.positionDEC = 'A2Z1_Crate'
    while True:
        GameAssets.Player.drop_item_able = False
        clr()
        map = Area2_map.A2Z1_lckCRT
        printc(map)
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))
                

            if 'E - Read Note' not in Actions and not solved:
                while True:
                    user_input = ""
                    typeTimer = time.time()
                    key = get_key()
                    current_time = time.time()
                    Typeruntime = current_time - typeTimer
                    if float(f"{Typeruntime:.2f}") >= 2.00:
                        continue
                    if key in ('\x08', '\x7f'):
                        user_input = user_input[:-1]
                    else:
                        user_input += key
                    if user_input.lower == 'e - open crate':
                        Actions.append('E - Open Crate')
                        solved = True
                        break
                    elif user_input.lower == 'q':
                        return
                break

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'D' or key == 'd' or key == 's' or key == 'S':
                player_position = move_player(key, CRD_A2Z1_CRT, player_position)
                Actions = []

            elif key == 'E' or key == 'e':
                if 'E - Read Note' in Actions:
                    GameAssets.A2Z1_Crate.actions.remove('E - Read Note')
                    type('The crate has no visible mechanism. The solution lies in retracing its design.\n')
                    questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                    clrlines(2)
                    break

                elif 'E - Open Crate' in Actions:
                    type('Elixir of Immortality ', 'bold magenta')
                    type('- Your Max Health has increased to')
                    type(' 200!\n', 'green')
                    questionary.press_any_key_to_continue().ask()
                    clrlines(2)
                    GameAssets.Player.HP = 200
                    GameAssets.Player.HP_MAX = 200
                    Actions.remove('E - Open Crate')
                    break

            elif key == 'Q' or key == 'q':
                if'Q - Exit' in Actions:
                    return
    
                                
                
        continue

#-----------------------
CRD_A2Z1 = {
    (0,0) : GameAssets.A2Z1_Start,
    (1,0) : GameAssets.A2Z1_a,
    (1,-1) : GameAssets.A2Z1_b,
    (2,-1) : GameAssets.A2Z1_c,
    (2,-2) : GameAssets.A2Z1_Chest,
    (3,-1) : GameAssets.A2Z1_d,
    (3,-2) : GameAssets.A2Z1_e,
    (4,-2) : GameAssets.A2Z1_f,
    (5,-2) : GameAssets.A2Z1_g,
    (5,-3) : GameAssets.A2Z1_h,
    (6,-3) : GameAssets.A2Z1_i
}

def game_A2Z1():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start'
    global Actions
    Actions = []
    while True:
        GameAssets.Player.drop_item_able = True
        clr()
        map = Area2_map.A2Z1
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))

            key = get_key()

            if key == 'W' or key == 'w' and GameAssets.Player.positionDEC == 'A2Z1_F':
                type('Large rocks block your path...\n')
                questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                startPos = 'F'
                break

            elif key == 'S' or key == 's' and GameAssets.Player.positionDEC == 'A2Z1_I':
                type('Large rocks block your path...\n')
                questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                startPos = 'I'
                break

            elif key == 'W' or key == 'w' and GameAssets.Player.positionDEC == 'A2Z1_G':
                clr()
                sleep(1)
                game_A2Z1_CRT()
                player_position = (5,-2)
                GameAssets.Player.positionENC = GameAssets.A2Z1_g
                GameAssets.Player.positionDEC = 'A2Z1_G'
                startPos = 'G'
                break
                

            elif key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z1, player_position)
                Actions = []
                
            elif key == 'T' or key == 't':
                for action in GameAssets.Player.positionENC.actions:
                    if action.startswith('T - Pick up '):
                        pickup_item = action[12:]
                        for item in GameAssets.Player.dropped_items:
                            if pickup_item == item.name:
                                GameAssets.Player.add_item(item)
                break

            elif key == 'I' or key == 'i':
                startPos = GameAssets.Player.positionENC.name
                GameAssets.player.open_inventory(GameAssets.Player)
                clr()
                break
            elif key == 'E' or key == 'e':
                if 'E - Open Chest' in Actions:
                    if 'Medkit' in GameAssets.Player.inventoryDEC:
                            break
                    else:
                        A2Z1Chest = open_chest()
                        if A2Z1Chest:
                            GameAssets.Player.add_item(GameAssets.Medkit)
                            GameAssets.A2Z1_Chest.actions.remove('E - Open Chest')
                            startPos = 'Chest'
                            break
                        else:
                            GameAssets.A2Z1_Chest.actions.remove('E - Open Chest')
                            startPos = 'Chest'
                            break
        continue



game_A2Z1()