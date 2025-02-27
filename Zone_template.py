import GameAssets, questionary
from Functions import printc, type, clrline, clr, get_key, clrlines, nav
from ExtraFunctions import move_player

def game_COORDINATE_SYSTEM_WITHOUT_CRD_PART():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = '''START POSITION'''
    global Actions
    Actions = []
    while True:
        clr()
        map = '''Map in Areax_map'''
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
                player_position = move_player(key, '''CRD_COORDINATE SYSTEM''', player_position)
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
                if 'E - ACTION' in Actions:
                    #Action code goes here
                    break

            else:
                startPos = GameAssets.Player.positionENC.name
                break
        continue


#Opening chest template

'''
elif 'E - Open Chest' in Actions:
    else:
        AXZYChest = open_chest()
        if AXZXChest:
            GameAssets.Player.add_item(GameAssets.''item'')
            GameAssets.AXZY_Chest.actions.remove('E - Open Chest')
            startPos = 'Chest'
            #break
        else:
            GameAssets.AXZY_Chest.actions.remove('E - Open Chest')
            startPos = 'Chest'
            #break

'''

#'continue to zone X' template
'''
(while True)
    if GameAssets.Player.positionDEC != 'None':
        for action in GameAssets.Player.positionENC.actions:
            if action == 'E - Continue to Zone X':
                printc(f'{action}', 'bold green')
                Actions.append(action)
            else:
                printc(f'{action}', 'bold')
                Actions.append(action)
        clrlines(len(Actions))

'''