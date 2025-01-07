#AREA 1 --- 'SHADOW PLAINS'
import os, sys

# Getting the parent directory of the current folder to import Extrafunctions
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Functions import printc, type

#KEY:
#   A1 - Area 1
#   Z1 - Zone 1
#   lck/ulck - Barrier side quest locking/unlocking path
#   SQ - Side Quest
#   GT - Gate

A1Z1_lckSQ1 = '''
                                                                    
                           HOUSE                                                     
         AREA 1:             ┬                                                       
      SHADOW PLAINS          │      ┌ ┐                                              
                             │       [bold red]![/bold red]                                               
                             │      └ ┘                                              
         [bold green]START[/bold green]├──────────────A──────────  ─  ─  ─  ─  ─────B────────────┤►           
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                                           ┴                         
                                                         [bold yellow]CHEST[/bold yellow]                                                                                                                                                
    '''
   
  
    
A1Z1_ulckSQ1 = '''
                                                                    
                           HOUSE                                                     
         AREA 1:             ┬                                                       
      SHADOW PLAINS          │                                                    
                             │                                                   
                             │                                                   
         [bold green]START[/bold green]├──────────────A─────────────────────────────B────────────┤►           
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                                           ┴                         
                                                         [bold yellow]CHEST[/bold yellow]                                                       
    '''

   
  
Charlie_House = '''
    
                                                     
                      DESK                       
                        ┬                        
                        │                        
                        │                 
 DOOR ►├────────────────A───────────────┤BED
    '''                          

A1Z2_lckGT12 = '''
                                                     F───────────────┤[bold blue]LEVER 2[/bold blue]               
                                                     │                          
                                                     │                          
                                                     │                          
                                                     │                          
                   B───────C─────────────────────────E                          
                   │       │                                                    
                   │       │                                                    
                   │       │                 [bold red]1[/bold red]                [bold red]2[/bold red]                 
[bold green]START[/bold green]├─────────────A       D────────────────[bold red]─/─[/bold red]───────G──────[bold red]─/─[/bold red]──────────────┤►
                           │                          │                         
                           │                          │                         
                           │                          │                         
                           ┴                          │                         
                         [bold blue]LEVER 1[/bold blue]                      ┴                         
                                                    [bold yellow]CHEST[/bold yellow]                  
'''
A1Z2_lckGT1 = '''
                                                     F───────────────┤[bold purple]LEVER 2[/bold purple]               
                                                     │                          
                                                     │                          
                                                     │                          
                                                     │                          
                   B───────C─────────────────────────E                          
                   │       │                                                    
                   │       │                                                    
                   │       │                 [bold red]1[/bold red]                [bold green]2[/bold green]                 
[bold green]START[/bold green]├─────────────A       D────────────────[bold red]─/─[/bold red]───────G──────[bold green]───[/bold green]──────────────┤►
                           │                          │                         
                           │                          │                         
                           │                          │                         
                           ┴                          │                         
                         [bold blue]LEVER 1[/bold blue]                      ┴                         
                                                    [bold yellow]CHEST[/bold yellow]                  
'''                                                            
A1Z2_lckGT2 = '''
                                                     F───────────────┤[bold blue]LEVER 2[/bold blue]               
                                                     │                          
                                                     │                          
                                                     │                          
                                                     │                          
                   B───────C─────────────────────────E                          
                   │       │                                                    
                   │       │                                                    
                   │       │                 [bold green]1[/bold green]                [bold red]2[/bold red]                 
[bold green]START[/bold green]├─────────────A       D────────────────[bold green]───[/bold green]───────G──────[bold red]─/─[/bold red]──────────────┤►
                           │                          │                         
                           │                          │                         
                           │                          │                         
                           ┴                          │                         
                         [bold purple]LEVER 1[/bold purple]                      ┴                         
                                                    [bold yellow]CHEST[/bold yellow]                  
'''
A1Z2_ulckGT12 = '''
                                                     F───────────────┤[bold purple]LEVER 2[/bold purple]               
                                                     │                          
                                                     │                          
                                                     │                          
                                                     │                          
                   B───────C─────────────────────────E                          
                   │       │                                                    
                   │       │                                                    
                   │       │                 [bold green]1[/bold green]                [bold green]2[/bold green]                 
[bold green]START[/bold green]├─────────────A       D────────────────[bold green]───[/bold green]───────G──────[bold green]───[/bold green]──────────────┤►
                           │                          │                         
                           │                          │                         
                           │                          │                         
                           ┴                          │                         
                         [bold purple]LEVER 1[/bold purple]                      ┴                         
                                                    [bold yellow]CHEST[/bold yellow]                  
'''                                                         

A1Z3_lckGT = '''
                   B────────────M────────────D              
                   │                         │              
                   │                         │              
                   │                         │              
                   │                         │              
                   │     [bold yellow]CHEST[/bold yellow]├──────────────E─[bold red]─/─[/bold red]─────────F
                   │                                       │
[bold green]START[/bold green]├─────────────A                                       │
                   │                                       │
                   │                                       │
                   │                                       │
                   │                      ┌ ┐              │
                   │                       [bold red]![/bold red]               │
                   │                      └ ┘              │
                   C─────────────────────────┤[bold blue]LEVER[/bold blue]        │
                                                           │
                                                           ┴
                                                           ▼
'''

A1Z3_ulckGT = '''
                   B────────────M────────────D              
                   │                         │              
                   │                         │              
                   │                         │              
                   │                         │              
                   │     [bold yellow]CHEST[/bold yellow]├──────────────E─[bold green]───[/bold green]─────────F
                   │                                       │
[bold green]START[/bold green]├─────────────A                                       │
                   │                                       │
                   │                                       │
                   │                                       │
                   │                                       │
                   │                                       │
                   │                                       │
                   C─────────────────────────┤[bold purple]LEVER[/bold purple]        │
                                                           │
                                                           ┴
                                                           ▼
'''
A1Z4 = '''
                                [bold red]┌  ┐[/bold red]  
                                 [bold red]!![/bold red]   
                                [bold red]└  ┘[/bold red]  
[bold green]START[/bold green]├───────────A──────────────────┤►
                 │                    
                 │                    
                 │                    
                 │                    
                 │                    
                 │                    
                 │                    
                 ┴                    
               [bold yellow]CHEST[/bold yellow]                  
'''
