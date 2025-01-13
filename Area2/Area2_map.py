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

A2Z3_lckGT = '''
                      [bold green]START[/bold green]                                      
                        ┬                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
 1───────────2──────────3───────────4──────────5──[bold red]─/─[/bold red]──A────────┤►
 │           │          │           │          │       │         
 │           │          │           │          │       │         
 │           │          │           │          │       ┴         
 │           │          │           │          │     [bold yellow]CHEST[/bold yellow]       
 ┴           ┴          ┴           ┴          ┴                 
┌─┐         ┌─┐        ┌─┐         ┌─┐        ┌─┐                
└─┘         └─┘        └─┘         └─┘        └─┘                              
'''

A2Z3_ulckGT = '''
                      [bold green]START[/bold green]                                      
                        ┬                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
 1───────────2──────────3───────────4──────────5──[bold green]───[/bold green]──A────────┤►
 │           │          │           │          │       │         
 │           │          │           │          │       │         
 │           │          │           │          │       ┴         
 │           │          │           │          │     [bold yellow]CHEST[/bold yellow]       
 ┴           ┴          ┴           ┴          ┴                 
[bold green]┌─┐[/bold green]         [bold green]┌─┐[/bold green]        [bold green]┌─┐[/bold green]         [bold green]┌─┐[/bold green]        [bold green]┌─┐[/bold green]                
[bold green]└─┘[/bold green]         [bold green]└─┘[/bold green]        [bold green]└─┘[/bold green]         [bold green]└─┘[/bold green]        [bold green]└─┘[/bold green]                              
'''

A2Z3_ALT = '''
                      [bold green]START[/bold green]                                      
                        ┬                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
                        │                                        
 A───────────B──────────C───────────D──────────E──[bold red]─/─[/bold red]──F────────┤►
 │           │          │           │          │       │         
 │           │          │           │          │       │         
 │           │          │           │          │       ┴         
 │           │          │           │          │     [bold yellow]CHEST[/bold yellow]       
 ┴           ┴          │           ┴          ┴                 
┌─┐         ┌─┐        ┌│┐         ┌─┐        ┌─┐                
└─┘         └─┘        └│┘         └─┘        └─┘                
                        │                                        
                        │                                        
                                                                 
                        [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]                                        
                                                                 
                        [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]                                        
                                                                 
                        [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]                                        
'''
os.system('clear')

CRD_A2Z3_ALT = {
    (0,0) : GameAssets.A2Z3_Start,
    (0,-1) : GameAssets.A2Z3_3,
    (0,-2) : GameAssets.A2Z3_secret,
    (-1,-1): GameAssets.A2Z3_2,
    (-2,-1): GameAssets.A2Z3_1,
    (1,-1) : GameAssets.A2Z3_4,
    (2,-1) : GameAssets.A2Z3_5lck
}

CRD_A2Z3_ulckGT = {
    (0,0) : GameAssets.A2Z3_Start,
    (0,-1) : GameAssets.A2Z3_3,
    (-1,-1): GameAssets.A2Z3_2,
    (-2,-1): GameAssets.A2Z3_1,
    (1,-1) : GameAssets.A2Z3_4,
    (2,-1) : GameAssets.A2Z3_5ulck,
    (3,-1) : GameAssets.A2Z3_a,
    (3,-2) : GameAssets.A2Z3_Chest,
    (4,-1) : GameAssets.A2Z3_End
}