import GameAssets, questionary
from Functions import printc, type, clrline, clr, get_key

#This Zone template was a thing I developed to have a quick way to make a coordinate system for any map.
#Of course, at first I tried just making it a function but too many things had to be different inside the funtion (specifically different
#things that would happen when you press E for example) that I couldn't rely soley on parameters. This template made the job much easier
#And quicker because alot of it is the same for every map and it is only the keybinds I have to change.

def game_COORDINATE_SYSTEM_WITHOUT_CRD_PART():
    global player_position
    player_position = (0,0)
    global startPos
    startPos = 'Start' #<-- usually this
    global Action
    Action = 'None'
    while True:
        map = '''Map in Areax_map'''
        printc(map)
        printc("-WASD to move-\n", 'bold')
        printc('[bold]I[/bold] - Open inventory\n')
        printc(f'Position: [bold]{startPos}[/bold]')
        
        while True:
            if GameAssets.Player.positionDEC != 'None':
                for action in GameAssets.Player.positionENC.actions:
                        printc(f'{action}', 'bold')
                        clrline()
                        Action = action
            key = get_key()
            if key == 'W' or key == 'w' or key == 'A' or key == 'a' or key == 'S' or key == 's' or key == 'D' or key == 'd':
                player_position = move_player(key, '''CRD_COORDINATE SYSTEM''', player_position)
                
            elif key == 'I' or key == 'i':
                startPos == GameAssets.Player.positionENC.name
                GameAssets.player.open_inventory(GameAssets.Player)
                clr()
                break
            elif key == 'E' or key == 'e':
                if Action == 'E - Interact':
                    #if an NPC interaction happens here, then code for that interaction goes here. note that some interactions
                    #happen without having to press E (in that case some sort of position check system for that Zone is required)
                        return
                elif Action == 'E - ANY OTHER ACTION':
                    #if any other action happens here, the code for that action goes here. Delete if not needed.
                    return
        continue