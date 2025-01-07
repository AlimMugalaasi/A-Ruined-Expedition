#AREA 2 --- 'VOID DEPTHS'
import os, sys

# Getting the parent directory of the current folder to import Extrafunctions
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from Functions import printc

import GameAssets

A2Z1 = '''
               AREA 2:                                                         
              THE VOID                                   [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]                     
               DEPTHS                                                          
                                                         [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]                     
                                                                               
                                                         │                     
                                                                               
[bold green]START[/bold green]├──────────────A                                    │                     
                    │                                                          
                    │                                    │                     
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
CRD_A2Z1 = {
    (0,0) : GameAssets.A2Z1_Start,
    (1,0) : GameAssets.A2Z1_a,
    (1,-1) : GameAssets.A2Z1_b,
    (2,-1) : GameAssets.A2Z1_c,
    (2,-2) : GameAssets.A2Z1_Chest,
    (3,-1) : GameAssets.A2Z1_d,
    (3,-2) : GameAssets.A2Z1_e,
    (4,-2) : GameAssets.A2Z1_f,
    (5,-2) : GameAssets.A2Z1_g,
    (5,-3) : GameAssets.A2Z1_h,
    (6,-3) : GameAssets.A2Z1_i
}

CRD_A2Z1_CRT = {
    (0,0) : GameAssets.A2Z1_Crate
}

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

A2Z1_ulckCRT = '''
                                  [bold green]CRATE[/bold green]
                                    ┬  
                                    │  
                                    │  
                                    │  
                                        
                                    │  
                                        
                                    │  
                                        
                                    [bold rgb(128,128,128)]│[/bold rgb(128,128,128)]  
'''

os.system('clear')


#Zone 1 maps completed
#CRDs made
#Make the sequences for Z1