#AREA 2 --- 'VOID DEPTHS'
import os, sys

# Getting the parent directory of the current folder to import Extrafunctions
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Functions import printc

import GameAssets

A2Z1 = '''                              AREA 2:                                                                                   
                             THE VOID                                   [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]
                              DEPTHS                                                                                    
                                                                        [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]
                                                                                                                        
                                                                        │                                               
                                                                                                                        
               [bold green]START[/bold green]├──────────────A                                    │                      
                                   │                                                                                    
-----------------------------------┼------------------------------------│-------------------------                     
                                   │                           #& %                                                     
                                   │                          &%&#$#    │                                               
                                   B─────────C─────────D        #$      │                                               
                                             │         │        │       │                                               
                                             │         │        │       │                                               
                                             │         │        │       │                                               
                                             ┴         E────────F───────G                                               
                                           [bold yellow]CHEST[/bold yellow]                        │                    
                                                                        │                                               
                                                                        │                                               
                                                                        H─────────I─────────┤►                          
                                                                                  │                                     
                                                                                  │                                     
                                                                                  │                                     
                                                                                 #% &                                   
                                                                               % #@&&                                   
                                                                               # %&# %                                  
'''

A2Z1_lckCRT = '''
                                  [bold magenta]CRATE[/bold magenta]
                                    ┬  
                                    │  
                                    │  
                                    │  
                                        
                                    │  
                                        
                                    │  
                                        
                                    [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]  
'''

A2Z2_lckSQ2 = '''
                                                              [bold green]+###  &#+###%%%%+[/bold green]                    
                                                            [bold green]++&&&&#&%###+####%%#+[/bold green]                  
                                                           [bold green]##%#&+%#%#%&&##%#+####[/bold green]                 
                                                               [bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]%#&+%[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]#%&&#[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                    
                                                               [bold rgb(150,75,0)]||  || ||  || ||[/bold rgb(150,75,0)]                    
                                                                   [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]  [white]│[/white]  [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                       
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       G──────┤[bold blue]LEVER[/bold blue]               
                                                                       │                           
                                               E───────────────────────F                           
                                               │                                                   
                                               │                                                   
                                               │                                                   
    ----------------------------------------───────------------------------------------------------
                                               │                                                   
                                               │        ┌ ┐                                        
                                               │         [bold red]![/bold red]                                         
                                               │        └ ┘                                        
                                               │       ┌──┬─┐                                      
                                               │       │┌┐│ │                                      
                                               D──────┤││││ │                                      
                                               │       ¯¯¯¯¯¯                                      
                                               │                                                   
                                               │                                                   
[bold green]START[/bold green]├────────────A────────────────────────────C                                                   
                  │                            │                        
                  [bold red]│[/bold red]                            │                                               
                  [bold red]/[/bold red]                            │                                                 
                  [bold red]│[/bold red]                            │                                                
                  │                            │                           
                  B──────┤[bold yellow]CHEST[/bold yellow]                │
                                               ┴
                                               ▼                                                                            
'''

CRD_A2Z2_lckSQ2 = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTlck,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,-1): GameAssets.A2Z2_End
}

A2Z2_ulckSQ2_lcklvr = '''
                                                              [bold green]+###  &#+###%%%%+[/bold green]                    
                                                            [bold green]++&&&&#&%###+####%%#+[/bold green]                  
                                                           [bold green]##%#&+%#%#%&&##%#+####[/bold green]                 
                                                               [bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]%#&+%[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]#%&&#[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                    
                                                               [bold rgb(150,75,0)]||  || ||  || ||[/bold rgb(150,75,0)]                    
                                                                   [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]  [white]│[/white]  [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                       
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       G──────┤[bold blue]LEVER[/bold blue]               
                                                                       │                           
                                               E───────────────────────F                           
                                               │                                                   
                                               │                                                   
                                           \   │   [white]/[/white]                                               
    ----------------------------------------\  │  [white]/------------------------------------------------[/white]
                                               │                                                   
                                               │        ┌ ┐                                        
                                               │         [bold red]![/bold red]                                         
                                               │        └ ┘                                        
                                               │       ┌──┬─┐                                      
                                               │       │┌┐│ │                                      
                                               D──────┤││││ │                                      
                                               │       ¯¯¯¯¯¯                                      
                                               │                                                   
                                               │                                                   
[bold green]START[/bold green]├────────────A────────────────────────────C                                                   
                  │                            │                        
                  [bold red]│[/bold red]                            │                                               
                  [bold red]/[/bold red]                            │                                                 
                  [bold red]│[/bold red]                            │                                                
                  │                            │                           
                  B──────┤[bold yellow]CHEST[/bold yellow]                │
                                               ┴
                                               ▼                                                          
'''

CRD_A2Z2_ulckSQ2_lcklvr = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTlck,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,2) : GameAssets.A2Z2_e,
    (3,2) : GameAssets.A2Z2_f,
    (3,3) : GameAssets.A2Z2_g,
    (3,4) : GameAssets.A2Z2_Forest,
    (4,3) : GameAssets.A2Z2_lvr,
    (2,4) : GameAssets.A2Z2_Chest2,
    (2,-1): GameAssets.A2Z2_End
}

A2Z2_ulckSQ2_ulcklvr = '''
                                                              [bold green]+###  &#+###%%%%+[/bold green]                    
                                                            [bold green]++&&&&#&%###+####%%#+[/bold green]                  
                                                           [bold green]##%#&+%#%#%&&##%#+####[/bold green]                 
                                                               [bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]%#&+%[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)][bold green]#%&&#[/bold green][bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                    
                                                               [bold rgb(150,75,0)]||  || ||  || ||[/bold rgb(150,75,0)]                    
                                                                   [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]  [white]│[/white]  [bold rgb(150,75,0)]||[/bold rgb(150,75,0)]                       
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       │                           
                                                                       G──────┤[bold purple]LEVER[/bold purple]               
                                                                       │                           
                                               E───────────────────────F                           
                                               │                                                   
                                               │                                                   
                                           \   │   [white]/[/white]                                               
    ----------------------------------------\  │  [white]/------------------------------------------------[/white]
                                               │                                                   
                                               │        ┌ ┐                                        
                                               │         [bold red]![/bold red]                                         
                                               │        └ ┘                                        
                                               │       ┌──┬─┐                                      
                                               │       │┌┐│ │                                      
                                               D──────┤││││ │                                      
                                               │       ¯¯¯¯¯¯                                      
                                               │                                                   
                                               │                                                   
[bold green]START[/bold green]├────────────A────────────────────────────C                                                   
                  │                            │                        
                  [bold green]│[/bold green]                            │                                               
                  [bold green]│[/bold green]                            │                                                 
                  [bold green]│[/bold green]                            │                                                
                  │                            │                           
                  B──────┤[bold yellow]CHEST[/bold yellow]                │
                                               ┴
                                               ▼                                                                                                                                                   
'''

CRD_A2Z2_ulckSQ2_ulcklvr = {
    (0,0) : GameAssets.A2Z2_Start,
    (1,0) : GameAssets.A2Z2_a,
    (1,-1): GameAssets.A2Z2_GTulck,
    (1,-2) : GameAssets.A2Z2_b,
    (2,-2) : GameAssets.A2Z2_Chest1,
    (2,0) : GameAssets.A2Z2_c,
    (2,1) : GameAssets.A2Z2_d,
    (3,1) : GameAssets.A2Z2_House,
    (2,2) : GameAssets.A2Z2_e,
    (3,2) : GameAssets.A2Z2_f,
    (3,3) : GameAssets.A2Z2_g,
    (3,4) : GameAssets.A2Z2_Forest,
    (4,3) : GameAssets.A2Z2_lvr,
    (2,4) : GameAssets.A2Z2_Chest2,
    (2,-1): GameAssets.A2Z2_End
}

os.system('clear')
printc(A2Z2_lckSQ2)

#Zone 1 maps completed
#CRDs made
#Make the sequences for Z1


#ADDD THE GATES