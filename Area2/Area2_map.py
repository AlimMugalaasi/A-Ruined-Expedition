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
                         [bold blue]LEVER[/bold blue]                 │       ┌──┬─┐                                      
                           ┬                   │       │┌┐│ │                                      
                           │                   D──────┤││││ │                                      
                           │                   │       ¯¯¯¯¯¯                                      
                           │                   │                                                   
                           │                   │                                                   
[bold green]START[/bold green]├────────────A────────B───────────────────C                                                   
                  │                                                                                
                  [bold red]│[/bold red]                                                                                
                  [bold red]/[/bold red]                                                                                
                  [bold red]│[/bold red]                                                                                
                  │                                                                                
                   ──[bold red]─/─[/bold red]─┤[bold yellow]CHEST[/bold yellow]                                                                    
'''

os.system('clear')
printc(A2Z2_lckSQ2)

#Zone 1 maps completed
#CRDs made
#Make the sequences for Z1