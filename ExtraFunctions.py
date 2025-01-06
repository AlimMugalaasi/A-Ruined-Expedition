from Functions import clrline, printc, clr, sleep, rainbow_type, get_key, type
import GameAssets, pyfiglet, questionary, random

#The purpose of Extra functions was to avoid problems with circular imports. (involving GameAssets)
#------------------------------------------------------

#Moving the player around a map

def move_player(direction, coordinate_sys, player_position):
    global new_position
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
    
#when the player dies

def player_death():
    clr()
    pyfiglet.print_figlet(" G A M E", font="slant", colors='red')
    sleep(0.7)
    pyfiglet.print_figlet(" O V E R", font="slant", colors='red')
    sleep(1)

    retryORquit = questionary.select("\n", choices=['Retry from last Zone', 'Quit', ''], qmark='').ask()
    if retryORquit == 'Retry from last Zone':
        GameAssets.Player.Alive = True
        GameAssets.Player.HP = 100
        return 'RETRY'

    elif retryORquit == 'Quit':
        quit()

#Boss battle animations

def bb_startAnim(boss):
    printc('''
           



 

     [bold green]❤[/bold green]      
                
           
          
''')
    sleep(0.5)
    clr()
    sleep(0.3)
    printc('''
           




              
      [bold green]❤[/bold green]           

           
                   
''')
    sleep(1)
    clr()
    printc('''

           
                                                             [bold red]!![/bold red]


                           
             
      [bold green]❤[/bold green]               
      
           
               
''')
    sleep(0.3)
    clr()
    printc('''
           




             
     [bold green]❤[/bold green]               

                  
 
''')    
    sleep(0.3)
    clr()
    printc('''

           
                                                             [bold red]!![/bold red]


                           
             
     [bold green]❤[/bold green]    
         
           

''')
    sleep(1)
    type(f'{boss} ', 'bold red')
    type('challenges you to a Duel!\n')
    sleep(2)


def playertakeDamage():
    clr()
    printc('''


                                                             [bold red]!![/bold red]


                           
             
     [bold red]❤[/bold red]    
         
           
           
''')
    sleep(0.3)
    clr()
    printc('''

           
                                                             [bold red]!![/bold red]


                           
             
     [bold green]❤[/bold green]    
         
           

''')
    sleep(0.3)
    clr()
    printc('''


                                                             [bold red]!![/bold red]


                           
             
     [bold red]❤[/bold red]    
         
           
           
''')
    sleep(0.3)
    clr()
    printc('''


                                                             [bold red]!![/bold red]


                           
             
     [bold green]❤[/bold green]    
         
           
           
''')
    sleep(0.3)

def bosstakeDamage():
    clr()
    printc('''


                                                             [bold yellow]!![/bold yellow]


                           
             
     [bold green]❤[/bold green]    
         
           
           
''')
    sleep(0.3)
    clr()
    printc('''

           
                                                             [bold red]!![/bold red]


                           
             
     [bold green]❤[/bold green]    
         
           
           
''')
    sleep(0.3)
    clr()
    printc('''


                                                             [bold yellow]!![/bold yellow]


                           
             
     [bold green]❤[/bold green]    
         
           
           
''')
    sleep(0.3)
    clr()
    printc('''


                                                             [bold red]!![/bold red]


                           
             
     [bold green]❤[/bold green]    
         
           
           
''')

def bb_normal(boss, player):
    printc(f'''

           
                                                             [bold red]!![/bold red]


                                                        [bold white]HP: {boss.HP}/100[/bold white]
             
     [bold green]❤[/bold green]              
                 

 [bold white]HP: {player.HP}/100[/bold white]
''')    

#boss battle code

def bossBattle(Boss):
    GameAssets.Player.fighting = True
    clr()
    bb_startAnim(Boss.name)
    clr()
    bb_normal(Boss, GameAssets.Player)

    Player = GameAssets.Player
    global starts
    starts = random.choice([Player, Boss])
    type(f'{starts.name} ' , 'bold')
    type('takes the first strike!\n')
    sleep(1)

    turn = starts
    while True:
        clr()
        bb_normal(Boss, Player)
        if turn == Boss:
            attack_choice = random.choice(Boss.attacks)
            attack = Boss.attack(attack_choice)
            try:
                test = attack * 2
            except TypeError:
                turn = Player
            else:
                global player_damage
                player_damage = GameAssets.Player.take_damage(attack)
                turn = Player
            finally:
                if 'ALIVE' in player_damage:
                    if player_damage[1] == 0:
                        continue

                    elif player_damage[1] <= 10:
                        playertakeDamage()
                        type("It's not so effective...\n", 'bold yellow')
                        sleep(1)
                        turn = Player
                        continue
                                 
                    elif player_damage[1] <= 20:
                        playertakeDamage()                       
                        type("It's pretty effective!\n", 'bold green')
                        sleep(1)
                        turn = Player
                        continue
                        
                    
                    elif player_damage[1] <= 49:
                        playertakeDamage()                       
                        type("It's really effective!\n", 'bold green')
                        sleep(1)
                        turn = Player
                        continue
                        

                    elif player_damage[1] <=100:
                        playertakeDamage()
                        rainbow_type("It's super effective!\n")
                        sleep(1)
                        turn = Player
                        continue

                    continue
                elif player_damage == 'DEAD':
                    Player.fighting = False
                    pd = player_death()
                    if pd == 'RETRY':
                        return 'UNDEFEATED'
                    


        elif turn == Player:
            printc('TIPS:', 'bold')
            print('Equip an item and then press F to attack using it.')
            print('Equipping any health item other than a BandAid will use up a turn once F is pressed.')
            print('BandAids can be used at any time.')
            print('Up to 3 items of armour (that is not single-use) can be equipped at a time (along with your weapon) to decrease inflicted damage.\n\n ') 

            printc('F - Attack', 'bold')
            printc('I - Open inventory\n', 'bold')
            type(f'How will {Player.name} fight back?\n')
            key = get_key()
            if key == 'I' or key == 'i':
                GameAssets.Player.open_inventory()
                continue

            elif key == 'F' or key == 'f':
                if Player.item_equippedDEC == 'None':
                    type("You need to equip an item to attack!\n", 'bold')
                    questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                    continue
                player_attack = Player.attack()
                if 'ATTACKED' in player_attack:
                    hit = Boss.take_damage(player_attack[1])

                    if str(hit) == 'PLAYER WIN':
                        Player.fighting = False
                        bosstakeDamage()
                        clr()
                        bb_normal(Boss, Player)
                        type(f'You defeated {Boss.name}!\n', 'bold green')
                        sleep(1)
                        questionary.press_any_key_to_continue().ask()
                        Player.HP = 100
                        return 'DEFEATED'

                    else:
                        if hit <= 10:
                            bosstakeDamage()
                            type("It's not so effective...\n", 'bold yellow')
                            sleep(1)
                            turn = Boss
                            continue
                            
                        
                        elif hit <= 20:
                            bosstakeDamage()
                            type("It's pretty effective!\n", 'bold green')
                            sleep(1)
                            turn = Boss
                            continue
                            
                        
                        elif hit <= 49:
                            bosstakeDamage()
                            type("It's really effective!\n", 'bold green')
                            sleep(1)
                            turn = Boss
                            continue
                            

                        elif hit <=100:
                            bosstakeDamage()
                            rainbow_type("It's super effective!\n", 0.03)
                            sleep(1)
                            turn = Boss
                            continue
    