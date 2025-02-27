import sys,os, time
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import questionary, GameAssets, random
os.system('clear')
from Functions import get_key, clrline, printc, clr, type, sleep, open_chest, clrlines,ld,firewood_minigame, rainbow_type
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
                challenge = input('')
                if challenge.lower() == 'e - open crate':
                    GameAssets.A2Z1_Crate.actions = ['E - Open Crate']
                    solved = True
                    break
                else:
                    break

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'D' or key == 'd' or key == 's' or key == 'S':
                player_position = move_player(key, CRD_A2Z1_CRT, player_position)
                Actions = []

            elif key == 'E' or key == 'e':
                if 'E - Read Note' in Actions:
                    type('The crate has no visible mechanism. The solution to opening it lies in retracing its design.\n')
                    questionary.press_any_key_to_continue().ask()
                    clrline()
                    type('Should you choose to accept the challenge, there is no turning back.\n')
                    sleep(1)
                    conf = questionary.confirm('Accept the challenge?').ask()
                    if conf:
                        GameAssets.A2Z1_Crate.actions.remove('E - Read Note')
                        break
                    else:
                        return

                elif 'E - Open Crate' in Actions:
                    type('Elixir of Immortality ', 'bold magenta')
                    type('- Your Max Health has increased to')
                    type(' 200!\n', 'green')
                    questionary.press_any_key_to_continue().ask()
                    clrlines(2)
                    GameAssets.Player.HP = 200
                    GameAssets.Player.HP_MAX = 200
                    return

            elif key == 'Q' or key == 'q':
                if'Q - Exit' in Actions:
                    return
    
                                
            else:
                startPos = GameAssets.Player.positionENC.name
                break    
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
    (6,-3) : GameAssets.A2Z1_i,
    (7,-3) : GameAssets.A2Z1_End
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
                    if action == 'E - Continue to Zone 2':
                        printc(f'{action}', 'bold green')
                        Actions.append(action)
                    else:
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
                if GameAssets.Player.HP_MAX != 200:
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
                elif 'E - Continue to Zone 2' in Actions:
                    return
            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue

#---------------------------ZONE 2

CRD_A2Z2_ulckSQ2_ulcklvr = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTulck,
    (1,-2) : GameAssets.A2Z2_b,
    (2,-2) : GameAssets.A2Z2_Chest1,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,2) : GameAssets.A2Z2_e,
    (3,2) : GameAssets.A2Z2_f,
    (3,3) : GameAssets.A2Z2_g,
    (3,4) : GameAssets.A2Z2_Forest,
    (4,3) : GameAssets.A2Z2_lvr,
    (2,4) : GameAssets.A2Z2_Chest2,
    (2,-1): GameAssets.A2Z2_End
}


def game_A2Z2_ulckSQ2_ulcklvr():
    global player_position
    player_position = (4,3)
    global startPos
    startPos = 'Lever'
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z2_ulckSQ2_ulcklvr
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                    if action == 'E - Continue to Zone 3':
                        printc(f'{action}', 'bold green')
                        Actions.append(action)
                    else:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z2_ulckSQ2_ulcklvr, player_position)
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
                if 'E - Continue to Zone 3' in Actions:
                    if GameAssets.Player.activeSQ != 'None':
                        type('You cannot exit a Zone with an active sidequest.\n')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        clrlines(2)
                        break
                    else:
                        return

                elif 'E - Interact' in Actions:
                    if 'E - Collect Firewood' not in Actions and GameAssets.Player.activeSQ != 'None':
                        GameAssets.NPC_Mika.interact(2)
                        GameAssets.SQ2.complete_sq(GameAssets.Player)
                        startPos = 'House'
                        break
                    elif 'E - Collect Firewood' not in Actions and GameAssets.Player.activeSQ == 'None':
                        type('MIKA: ', 'bold white')
                        type('The code is 9abc3!\n')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        clrlines(2)
                        break


                elif 'E - Open Chest' in Actions:
                    if GameAssets.Player.positionENC == GameAssets.A2Z2_Chest1:
                        A2Z2Chest = open_chest()
                        if A2Z2Chest:
                            GameAssets.Player.add_item(GameAssets.BandAid)
                            GameAssets.Player.add_item(GameAssets.silent_knife)
                            GameAssets.A2Z2_Chest1.actions.remove('E - Open Chest')
                            startPos = 'Chest'
                            break
                        else:
                            GameAssets.A2Z2_Chest1.actions.remove('E - Open Chest')
                            startPos = 'Chest'
                            break
                           
                    elif GameAssets.Player.positionENC == GameAssets.A2Z2_Chest2:
                        ChestCode = input('Enter Code: ')
                        if ChestCode == '9abc3':
                            printc('-ACCEPTED-', 'bold green')
                            sleep(0.7)
                            GameAssets.Player.add_item(GameAssets.arcane_rune)
                            GameAssets.Player.add_item(GameAssets.longSword)
                            GameAssets.A2Z2_Chest2.actions.remove('E - Open Chest')
                            break
                        else:
                            printc('-DENIED-', 'bold red')
                            sleep(0.7)
                            break

                elif 'E - Collect Firewood' in Actions:
                    firewood_minigame()
                    type('Firewood collected!\n', 'bold green')
                    sleep(1)
                    clrline()
                    startPos = 'Forest'
                    GameAssets.A2Z2_House.actions.append('E - Interact')
                    GameAssets.A2Z2_Forest.actions.remove('E - Collect Firewood')
                    break
            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue

#---------------------------
CRD_A2Z2_ulckSQ2_lcklvr = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTlck,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,2) : GameAssets.A2Z2_e,
    (3,2) : GameAssets.A2Z2_f,
    (3,3) : GameAssets.A2Z2_g,
    (3,4) : GameAssets.A2Z2_Forest,
    (4,3) : GameAssets.A2Z2_lvr,
    (2,4) : GameAssets.A2Z2_Chest2,
    (2,-1): GameAssets.A2Z2_End
}

def game_A2Z2_ulckSQ2_lcklvr():
    global player_position
    player_position = (3,1)
    global startPos
    startPos = 'House'
    GameAssets.Player.positionENC = GameAssets.A2Z2_House
    GameAssets.Player.positionDEC = 'A2Z2_House'
    GameAssets.A2Z2_House.actions.remove('E - Interact')
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z2_ulckSQ2_lcklvr
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                    if action == 'E - Continue to Zone 3':
                        printc(f'{action}', 'bold green')
                        Actions.append(action)
                    else:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z2_ulckSQ2_lcklvr, player_position)
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
                if 'E - Continue to Zone 3' in Actions:
                    if GameAssets.Player.activeSQ != 'None':
                        type('You cannot exit a Zone with an active sidequest.\n')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        clrlines(2)
                        break
                    else:
                        return

                elif 'E - Interact' in Actions:
                    if 'E - Collect Firewood' not in Actions and GameAssets.Player.activeSQ != 'None':
                        GameAssets.NPC_Mika.interact(2)
                        GameAssets.SQ2.complete_sq(GameAssets.Player)
                        startPos = 'House'
                        break
                    elif 'E - Collect Firewood' not in Actions and GameAssets.Player.activeSQ == 'None':
                        type('MIKA: ', 'bold white')
                        type('The code is 9abc3!\n')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        clrlines(2)
                        break
                           
                elif 'E - Open Chest' in Actions:
                    ChestCode = input('Enter Code: ')
                    if ChestCode == '9abc3':
                        printc('-ACCEPTED-', 'bold green')
                        sleep(0.7)
                        GameAssets.Player.add_item(GameAssets.arcane_rune)
                        GameAssets.Player.add_item(GameAssets.longSword)
                        GameAssets.A2Z2_Chest2.actions.remove('E - Open chest')
                        break
                    else:
                        printc('-DENIED-', 'bold red')
                        sleep(0.7)
                        break

                elif 'E - Pull Lever' in Actions:
                    GameAssets.Player.positionENC = GameAssets.A2Z2_lvr
                    GameAssets.Player.positionDEC = 'A2Z2_lvr'
                    GameAssets.A2Z2_lvr.actions.remove('E - Pull Lever')
                    game_A2Z2_ulckSQ2_ulcklvr()
                    return
                
                elif 'E - Collect Firewood' in Actions:
                    firewood_minigame()
                    type('Firewood collected!\n', 'bold green')
                    sleep(1)
                    clrline()
                    startPos = 'Forest'
                    GameAssets.A2Z2_House.actions.append('E - Interact')
                    GameAssets.A2Z2_Forest.actions.remove('E - Collect Firewood')
                    break
            else:
                startPos = GameAssets.Player.positionENC.name
                break  
        continue
#-------------------


CRD_A2Z2_lckSQ2 = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTlck,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,-1): GameAssets.A2Z2_End
}

def game_A2Z2_lckSQ2():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start'
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z2_lckSQ2
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                    if action == 'E - Continue to Zone 3':
                        printc(f'{action}', 'bold green')
                        Actions.append(action)
                    else:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z2_lckSQ2, player_position)
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
                if 'E - Interact' in Actions:
                    GameAssets.SQ2.start_sq(GameAssets.Player)
                    GameAssets.NPC_Mika.interact(1)
                    game_A2Z2_ulckSQ2_lcklvr()
                    return
                
                if 'E - Continue to Zone 3' in Actions:
                    return
            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue


#-------------------------------------------------ZONE 3
CRD_A2Z3_ALT = {
    (0,0) : GameAssets.A2Z3_Start,
    (0,-1) : GameAssets.A2Z3_3,
    (0,-2) : GameAssets.A2Z3_secret,
    (-1,-1): GameAssets.A2Z3_2,
    (-2,-1): GameAssets.A2Z3_1,
    (1,-1) : GameAssets.A2Z3_4,
    (2,-1) : GameAssets.A2Z3_5lck
}

def game_A2Z3_ALT():
    global player_position
    player_position = (0,-1)
    global startPos
    startPos = 'Switch 3'
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z3_ALT
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
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z3_ALT, player_position)
                Actions = []
            
            elif key == 'S' or key == 's':
                if GameAssets.Player.positionENC == GameAssets.A2Z3_3:
                    #secret ending
                    return
                
                else:
                    player_position = move_player(key, CRD_A2Z3_ALT, player_position)
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

            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue
#---------------------------------
CRD_A2Z3_ulckGT = {
    (0,0) : GameAssets.A2Z3_Start,
    (0,-1) : GameAssets.A2Z3_3,
    (-1,-1): GameAssets.A2Z3_2,
    (-2,-1): GameAssets.A2Z3_1,
    (1,-1) : GameAssets.A2Z3_4,
    (2,-1) : GameAssets.A2Z3_5ulck,
    (3,-1) : GameAssets.A2Z3_a,
    (3,-2) : GameAssets.A2Z3_Chest,
    (4,-1) : GameAssets.A2Z3_End
}

def game_A2Z3_ulckGT(startPosition, playerCoords):
    global player_position
    player_position = playerCoords
    global startPos
    startPos = startPosition
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z3_ulckGT
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                    for action in GameAssets.Player.positionENC.actions:
                        if action == 'E - Continue to Zone 4':
                            printc(f'{action}', 'bold green')
                            Actions.append(action)
                        else:
                            printc(f'{action}', 'bold')
                            Actions.append(action)
                    clrlines(len(Actions))

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z3_ulckGT, player_position)
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
                    A2Z3Chest = open_chest()
                    if A2Z3Chest:
                        GameAssets.Player.add_item(GameAssets.BandAid)
                        GameAssets.A2Z3_Chest.actions.remove('E - Open Chest')
                        startPos = 'Chest'
                        break
                    else:
                        GameAssets.A2Z3_Chest.actions.remove('E - Open Chest')
                        startPos = 'Chest'
                        break
                elif 'E - Continue to Zone 4' in Actions:
                    return

            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue

#----------------------------------
CRD_A2Z3_lckGT = {
    (0,0) : GameAssets.A2Z3_Start,
    (0,-1) : GameAssets.A2Z3_3,
    (-1,-1): GameAssets.A2Z3_2,
    (-2,-1): GameAssets.A2Z3_1,
    (1,-1) : GameAssets.A2Z3_4,
    (2,-1) : GameAssets.A2Z3_5ulck
}

def game_A2Z3_lckGT():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start'
    global Actions
    Actions = []
    global sequence
    sequence = random.sample(range(1, 6), 5)
    global secret_sequence
    secret_sequence = []
    global userseq
    userseq = []
    global index
    index = 0
    while True:
        clr()
        map = Area2_map.A2Z3_lckGT
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []

        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                printc(f'{userseq}', 'bold green')
                clrlines(len(Actions)+1)

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key,CRD_A2Z3_lckGT, player_position)
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
                if 'E - Activate' in Actions:
                    if GameAssets.Player.positionDEC == 'A2Z3_1':
                        userseq.append(1)
                        secret_sequence = []
                        startPos = 'Switch 1'
                        if userseq[index] == sequence[index]:
                            if userseq == sequence:
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5ulck.actions.remove('E - Activate')
                                game_A2Z3_ulckGT(startPos, player_position)
                                return
                            
                            else:
                                sleep(0.2)
                                index+=1
                                break
                        else:
                            printc(f'{userseq}', 'bold red')
                            sleep(0.5)
                            userseq = []
                            index = 0
                            break
                            
                    elif GameAssets.Player.positionDEC == 'A2Z3_2':
                        userseq.append(2)
                        secret_sequence = []
                        startPos = 'Switch 2'
                        if userseq[index] == sequence[index]:
                            if userseq == sequence:
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5ulck.actions.remove('E - Activate')
                                game_A2Z3_ulckGT(startPos, player_position)
                                return
                            else:
                                sleep(0.2)
                                index+=1
                                break
                        
                        else:
                            printc(f'{userseq}', 'bold red')
                            sleep(0.5)
                            userseq = []
                            index = 0
                            break

                    if GameAssets.Player.positionDEC == 'A2Z3_3':
                        userseq.append(3)
                        secret_sequence.append(3)
                        if secret_sequence == [3,3,3,3,3]:
                                rainbow_type('A Tunnel reveals itself...\n', 0.1)
                                sleep(0.3)
                                clr()
                                sleep(0.5)
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5lck.actions.remove('E - Activate')
                                game_A2Z3_ALT()
                                GameAssets.Player.secret_acheived = True
                                return
                        
                        startPos = 'Switch 3'
                        if userseq[index] == sequence[index]:
                            if userseq == sequence:
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5ulck.actions.remove('E - Activate')
                                game_A2Z3_ulckGT(startPos, player_position)
                                return 

                            
                            else:
                                sleep(0.2)
                                index+=1
                                break
                        else:
                            printc(f'{userseq}', 'bold red')
                            sleep(0.5)
                            userseq = []
                            index = 0
                            break
                            

                    if GameAssets.Player.positionDEC == 'A2Z3_4':
                        userseq.append(4)
                        secret_sequence = []
                        startPos = 'Switch 4'
                        if userseq[index] == sequence[index]:
                            if userseq == sequence:
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5ulck.actions.remove('E - Activate')
                                game_A2Z3_ulckGT(startPos, player_position)
                                return
                            else:
                                sleep(0.2)
                                index+=1
                                break
                            
                        else:
                            printc(f'{userseq}', 'bold red')
                            sleep(0.5)
                            userseq = []
                            index = 0
                            break

                    if GameAssets.Player.positionDEC == 'A2Z3_5':
                        userseq.append(5)
                        secret_sequence = []
                        startPos = 'Switch 5'
                        if userseq[index] == sequence[index]:
                            if userseq == sequence:
                                GameAssets.A2Z3_1.actions.remove('E - Activate')
                                GameAssets.A2Z3_2.actions.remove('E - Activate')
                                GameAssets.A2Z3_3.actions.remove('E - Activate')
                                GameAssets.A2Z3_4.actions.remove('E - Activate')
                                GameAssets.A2Z3_5ulck.actions.remove('E - Activate')
                                game_A2Z3_ulckGT(startPos, player_position)
                                return
                            else:
                                sleep(0.2)
                                index+=1
                                break
                            
                        else:
                            printc(f'{userseq}', 'bold red')
                            sleep(0.5)
                            userseq = []
                            index = 0
                            break
            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue


#-----------------------
#--------------------------------------------------ZONE 4

CRD_A2Z4 = {
    (0,0) : GameAssets.A2Z4_Start,
    (1,0) : GameAssets.A2Z4_bb
}

def game_A2Z4():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start'
    global Actions
    Actions = []
    while True:
        clr()
        map = Area2_map.A2Z4
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
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A2Z4, player_position)
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
                if 'E - Take Artifact' in Actions:
                    bb = bossBattle(GameAssets.chaser_hunter)
                    if bb == 'DEFEATED':
                        return
                    elif bb == 'UNDEFEATED':
                         GameAssets.chaser_hunter.HP = 200
                         break

            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue

ld(5)
game_A2Z1()
ld(5)
game_A2Z2_lckSQ2()
ld(5)
game_A2Z3_lckGT()
ld(5)
game_A2Z4()
GameAssets.Player.complete_area(GameAssets.Area2)
