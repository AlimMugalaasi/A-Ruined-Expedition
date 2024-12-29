import sys,os
# Getting the parent directory of the current folder (so i can import Functions)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

import questionary, GameAssets
os.system('clear')
from Functions import get_key, clrline, printc, clr, type, sleep, open_chest, clrlines, nav
from ExtraFunctions import move_player
import Area1_map

#-----------------------------------------------------------AREA 1 SEQUENCE (i.e GAMEPLAY)

#----------------------ZONE 1
CRD_Charlie_House = {
    (0,0) : GameAssets.Charlie_House_Door,
    (1,0) : GameAssets.Charlie_House_a,
    (1,1) : GameAssets.Charlie_House_Desk,
    (2,0) : GameAssets.Charlie_House_Bed
}   


def game_Charlie_House():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Door'
    global Actions
    Actions = []
    GameAssets.Player.positionENC = GameAssets.Charlie_House_Door
    GameAssets.Player.positionDEC = GameAssets.Charlie_House_Door.name
    while True:
        clr()
        map = Area1_map.Charlie_House
        printc(map)
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        Actions = []
        
        while True:
            Actions = []
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        Actions.append(action)
                clrlines(len(Actions))

            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_Charlie_House, player_position)
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
                if 'E - Read Note' in Actions:
                    if not GameAssets.Player.ReadNote:
                        clr()
                        with open('Note.txt', 'r') as file:
                            for line in file:
                                type(line.strip(),None)
                                print(' ')
                                questionary.press_any_key_to_continue().ask()
                                clrline()
                                print(' ')
                            player_position = (1,1)
                            startPos = ('Desk')
                            GameAssets.Player.ReadNote = True
                            break
                    elif GameAssets.Player.ReadNote:
                        type('I need to find out who wrote this...\n')
                        questionary.press_any_key_to_continue().ask()
                        clrlines(2)

                elif 'E - Check Under Bed' in Actions:
                    if GameAssets.Bridge_key_A1Z1.name not in GameAssets.Player.inventoryDEC:
                        GameAssets.Player.add_item(GameAssets.Bridge_key_A1Z1)
                        type('YOU: ', 'bold')
                        type('Really? out of all places, this guy leaves the key to a public bridge under the bed?\n')
                        questionary.press_any_key_to_continue().ask()
                        player_position = (2,0)
                        startPos = ('Bed')
                        break

                    else:
                        player_position = (2,0)
                        startPos = ('Bed')
                        break
                elif 'E - Exit' in Actions:
                    GameAssets.Player.positionENC = GameAssets.A1Z1_House
                    GameAssets.Player.positionDEC = GameAssets.A1Z1_House.name
                    return
        continue

#---------------------------------------------------------------------------


CRD_A1Z1_ulckSQ1 = {
    (0,0) : GameAssets.A1Z1_Start,
    (1,0) : GameAssets.A1Z1_a,
    (1,1) : GameAssets.A1Z1_House,
    (2,0) : GameAssets.A1Z1_b,
    (3,0) : GameAssets.A1Z1_End,
    (2,-1) : GameAssets.A1Z1_Chest
}

def game_A1Z1_ulckSQ1():
    global player_position
    player_position = (1,0)
    global startPos
    startPos = 'A'
    GameAssets.Player.positionENC.actions = []
    global Actions
    Actions = []
    while True:
        clr()
        map = Area1_map.A1Z1_ulckSQ1
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
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, CRD_A1Z1_ulckSQ1, player_position)
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
                if 'E - Enter House' in Actions:
                        type('You cannot do that right now!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrlines(2)

                elif 'E - Open Chest' in Actions:
                    if 'Sheild' in GameAssets.Player.inventoryDEC:
                        break
                    else:
                        A1Z1Chest = open_chest()
                        if A1Z1Chest:
                            GameAssets.Player.add_item(GameAssets.shield)
                            GameAssets.A1Z1_Chest.actions = []
                            GameAssets.Player.positionENC.actions = []
                            startPos = 'Chest'
                            break
                        else:
                            GameAssets.A1Z1_Chest.actions = []
                            GameAssets.Player.positionENC.actions = []
                            startPos = 'Chest'
                            break
                elif 'E - Continue to Zone 2' in Actions:
                    return
        continue
#-------------------------------------------------------------
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
    global Actions
    Actions = []
    while True:
        clr()
        map = Area1_map.A1Z1_lckSQ1
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
                player_position = move_player(key, CRD_A1Z1lckSQ1, player_position)
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
                            GameAssets.Player.add_item(GameAssets.spear)
                            GameAssets.SQ1.complete_sq(GameAssets.Player)
                            return
                        else:
                            if CRD_A1Z1lckSQ1[player_position].name == '[!]':
                                GameAssets.NPC_Charlie.interact(3)
                                break
                elif 'E - Enter House' in Actions:
                    if GameAssets.Player.item_equippedDEC == "Charlie's House Key":
                        game_Charlie_House()
                        player_position = (1,1)
                        startPos = 'House'
                        break

                    elif "Charlie's House Key" not in GameAssets.Player.inventoryDEC:
                        type('You need a ')
                        type('key ', 'bold yellow')
                        type('to do that!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrlines(2)

                    elif GameAssets.Player.item_equippedDEC != "Charlie's House Key":
                        type('You need to ')
                        type('equip ', 'blue')
                        type('the key to use it!\n')
                        questionary.press_any_key_to_continue().ask()
                        clrlines(2)
        continue

#-----------------------ZONE 2




game_A1Z1lckSQ1()
game_A1Z1_ulckSQ1()


    
#NEXT STEPS
#fix the bug which causes the actions in A1Z1_ulckSQ1 to print twice when an item is dropped
#Zone 1 will (officially) be done once that happens
#Design + code zone 2