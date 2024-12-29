from Functions import clrline, printc
import GameAssets

#The purpose of Extra functions was to avoid problems with circular imports.
#------------------------------------------------------

#Moving the player around a map

def move_player(direction, coordinate_sys, player_position):
    x, y = player_position
    if direction == "W" or direction =='w':
        if coordinate_sys[player_position].options == 'ALL':
            new_position = (x, y + 1)
        else:
            for char in coordinate_sys[player_position].options:
                if char == 'W':
                    new_position = (x, y + 1)

    elif direction == "A" or direction =='a':
        if coordinate_sys[player_position].options == 'ALL':
            new_position = (x - 1, y)
        else:
            for char in coordinate_sys[player_position].options:
                if char == 'A':
                    new_position = (x - 1, y)

    elif direction == "S" or direction =='s':
        if coordinate_sys[player_position].options == 'ALL':
            new_position = (x, y - 1)
        else:
            for char in coordinate_sys[player_position].options:
                if char == 'S':
                    new_position = (x, y - 1)

    elif direction == "D" or direction =='d':
        if coordinate_sys[player_position].options == 'ALL':
            new_position = (x + 1, y)
        else:
            for char in coordinate_sys[player_position].options:
                if char == 'D':
                    new_position = (x + 1, y)

    else:
        return player_position

    if new_position in coordinate_sys:
        player_position = new_position
        clrline()
        printc(f"Position: [bold]{coordinate_sys[new_position].name}[/bold]")
        GameAssets.Player.positionENC = coordinate_sys[new_position]
        GameAssets.Player.positionDEC = coordinate_sys[new_position].code
        return player_position
    else:
        return player_position
    

    