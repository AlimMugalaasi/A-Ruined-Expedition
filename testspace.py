from Functions import printc, sleep, clr, type
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
            input('Player takes a turn\n')
            turn = Boss
            continue

bossBattle(GameAssets.Zexrash)
