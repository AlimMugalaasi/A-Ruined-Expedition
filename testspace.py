from Functions import printc, sleep, clr, type, get_key
import GameAssets, random
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
                GameAssets.Player.take_damage(attack)
                turn = Player
            finally:
                continue
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
                player_attack = Player.attack()
                if 'ATTACKED' in player_attack:
                    hit = Boss.take_damage(player_attack[1])
                    try:
                        typecheck = hit*2
                    
                    except TypeError:
                        #PLAYER WIN BATTLE ANIM
                        return
                    
                    else:
                        if hit <= 10:
                            type("It's not so effective...", 'bold yellow', 0.1)
                            sleep(1)
                        
                        elif hit <= 20:
                            type("It's somewhat effective...") #add speed and colour and finsih rest


            

            
bossBattle(GameAssets.Zexrash)


