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
#   SQ1 - Side Quest

A1Z1_lckSQ1 = '''
                                                                    
                           HOUSE                                                     
                             ┬                                                       
                             │      ┌ ┐                                              
                             │       [bold red]![/bold red]                                               
                             │      └ ┘                                              
         [bold green]START[/bold green]├──────────────A──────────  ─  ─  ─  ─  ─────B────────────┤►           
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                             [bold yellow]CHEST[/bold yellow]├────────┘                         
                                                                                     
                                                                 
    '''
    
def A1Z1_ulckSQ1():
    printc('''
                                                                    
                           HOUSE                                                     
                             ┬                                                       
                             │      ┌ ┐                                              
                             │       [bold red]![/bold red]                                               
                             │      └ ┘                                              
         [bold green]START[/bold green]├──────────────A─────────────────────────────B────────────┤►           
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                                           │                         
                                             [bold yellow]CHEST[/bold yellow]├────────┘                         
                                                                                     
                                                                 
    ''')
    

def A1Z1_House():
    print('''
    
                                                     
                      DESK                       
                        ┬                        
                        │                        
                        │                 BED    
 DOOR ►├────────────────A───────────────┤        
                                          DRAWER 
                                                 
    
    ''')
                                                                                  
                                                                                  
                                                                                  
                                                                                  
                                                                                  