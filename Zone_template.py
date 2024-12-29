import GameAssets, questionary
from Functions import printc, type, clrline, clr, get_key, clrlines, nav
from ExtraFunctions import move_player

#This Zone template was a thing I developed to have a quick way to make a coordinate system for any map.
#Of course, at first I tried just making it a function but too many things had to be different inside the funtion (specifically different
#things that would happen when you press E for example) that I couldn't rely soley on parameters. This template made the job much easier
#And quicker because alot of it is the same for every map and it is only the keybinds I have to change.

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
        nav()
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
                if 'E - Interact' in Actions:
                    #if an NPC interaction happens here, then code for that interaction goes here. note that some interactions
                    #happen without having to press E (in that case some sort of position check system for that Zone is required)
                        return
                elif 'E - ANY OTHER ACTION' in Actions:
                    #if any other action happens here, the code for that action goes here. Delete if not needed.
                    return
        continue


#Opening chest template

'''
if 'E - Open Chest' in Actions:
    if ''item name (not item.name)'' in GameAssets.Player.inventoryDEC:
        #break
    else:
        A1Z1Chest = open_chest()
        if A1Z1Chest:
            GameAssets.Player.add_item(GameAssets.''item'')
            GameAssets.A1Z1_Chest.actions = []
            GameAssets.Player.positionENC.actions = []
            startPos = 'Chest'
            #break
        else:
            GameAssets.A1Z1_Chest.actions = []
            GameAssets.Player.positionENC.actions = []
            startPos = 'Chest'
            #break

'''