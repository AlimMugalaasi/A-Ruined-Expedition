from Functions import printc, sleep, clr, type, get_key, rainbow_type
import GameAssets, random, questionary
def bb_normal():
    printc('''
                                                            ┌  ┐ 
                                                             [bold red]!![/bold red] _
                                                           [white]/└  ┘/[/white]
                                                          [white]/____/[/white] 
                           
   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')
    
def bb_startAnim(boss):
    printc('''
           



 
   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')
    sleep(0.5)
    clr()
    sleep(0.3)
    printc('''
           




   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')
    sleep(1)
    clr()
    printc('''
                                                            ┌  ┐ 
                                                             [bold red]!![/bold red] _
                                                           [white]/└  ┘/[/white]
                                                          [white]/____/[/white] 
                           
   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')
    sleep(0.3)
    clr()
    printc('''
           




   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')    
    sleep(0.3)
    clr()
    printc('''
                                                            ┌  ┐ 
                                                             [bold red]!![/bold red] _
                                                           [white]/└  ┘/[/white]
                                                          [white]/____/[/white] 
                           
   ┌__┐____                
  [white]/[/white] [bold green]❤[/bold green]     [white]/[/white]                
 [white]/[/white] └  ┘  [white]/[/white]                 
[white]/_______/[/white]                  
''')
    sleep(1)
    type(f'{boss} ', 'bold red')
    type('challenges you to a Duel!\n')
    sleep(2)
    
def bossBattle(Boss):
    GameAssets.Player.fighting = True
    clr()
    bb_startAnim(Boss.name)
    clr()
    bb_normal()

    Player = GameAssets.Player
    global starts
    starts = random.choice([Player, Boss])
    type(f'{starts.name} ' , 'bold')
    type('takes the first strike!\n')
    sleep(1)

    turn = starts
    while True:
        clr()
        bb_normal()
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
                    if player_damage[1] <= 10:
                        type("It's not so effective...\n", 'bold yellow')
                        sleep(1)
                        turn = Player
                        continue
                                 
                    elif player_damage[1] <= 20:
                        type("It's pretty effective!\n", 'bold green')
                        sleep(1)
                        turn = Player
                        continue
                        
                    
                    elif player_damage[1] <= 49:
                        type("It's really effective!\n", 'bold green')
                        sleep(1)
                        turn = Player
                        continue
                        

                    elif player_damage[1] <=100:
                        rainbow_type("It's super effective!\n")
                        sleep(1)
                        turn = Player
                        continue

                    continue
                elif player_damage == 'DEAD':
                    quit()


        elif turn == Player:
            printc('TIPS:', 'bold')
            print('Equip an item and then press F to attack using it.')
            print('Equipping any health item other than a BandAid will use up a turn once F is pressed.')
            print('BandAids can be used at any time.')
            print('Up to 3 items of armour (that is not single-use) can be equipped at a time to decrease inflicted damage.\n\n ') 

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
                    input(f'{player_attack}') #TSTS
                    hit = Boss.take_damage(player_attack[1])

                    if str(hit) == 'PLAYER WIN':
                        return

                    else:
                        if hit <= 10:
                            type("It's not so effective...\n", 'bold yellow')
                            sleep(1)
                            turn = Boss
                            continue
                            
                        
                        elif hit <= 20:
                            type("It's pretty effective!\n", 'bold green')
                            sleep(1)
                            turn = Boss
                            continue
                            
                        
                        elif hit <= 49:
                            type("It's really effective!\n", 'bold green')
                            sleep(1)
                            turn = Boss
                            continue
                            

                        elif hit <=100:
                            rainbow_type("It's super effective!\n", 0.03)
                            sleep(1)
                            turn = Boss
                            continue
                        





            

GameAssets.Player.add_item(GameAssets.spear)
GameAssets.Player.add_item(GameAssets.arcane_rune)
GameAssets.Player.add_item(GameAssets.shield)
GameAssets.Player.add_item(GameAssets.BandAid)
GameAssets.Player.add_item(GameAssets.BandAid)
GameAssets.Player.add_item(GameAssets.BandAid)
bossBattle(GameAssets.Zexrash)

#make sure fighiting becomes false when battle finish
#add more fighting styles for BOSS and make it heal themselves after certain health
#try and make this last a while but remember this is the easiet bb as it is the first.
#health bars


