from Functions import printc, clr, type, ld, clrline, sleep, clrlines, no_HP
import questionary, pyfiglet
from NPCInteractions import Charlie , Anonymous_Civilian, Zexrash
#-------------------------------------------------------PLAYER

class player:
    def __init__(self, name, position):
        self.name = name
        self.positionENC = position
        self.positionDEC = position
        self.current_area = 'A1'
        self.current_zone = 'Z1'
        self.number_of_bandaids = 0
        self.inventoryENC = []
        self.inventoryDEC = ['<--BACK', 'EQUIPPED']
        self.inventoryMaxCapacity = 10
        self.item_equippedDEC = 'None'
        self.item_equippedENC = 'None'
        self.armour_equippedDEC = []
        self.armour_equippedENC = []
        self.total_equipped = ['<--BACK']
        self.HP = 100
        self.Alive = True
        self.completed_areas = []
        self.activeSQ = 'None'
        self.stored_action = 'None'
        self.dropped_items = []
        self.fighting = False
        self.drop_item_able = True
        #-------------------------NECESSARY ONE-TIME ATTRIBUTES
        self.ReadNote = False
        self.A2Z1CRT_opened = False
    
    def open_inventory(self):
        while True:
            clr()
            printc(f'[underline green bold italic]INVENTORY[/underline green bold italic]           HP: [bold]{self.HP}[/bold]')
            item_select = questionary.select("Select an item to see further options. Select EQUIPPED to see options for equipped items.\n", choices=self.inventoryDEC, qmark='>').ask()
            if item_select =='<--BACK':
                break
            elif item_select == 'EQUIPPED':
                unequip_select = questionary.select("Select an Item to unequip it: ", choices=self.total_equipped, qmark='>').ask()
                if unequip_select == '<--BACK':
                    continue
                else:
                    unequip_confirm = questionary.confirm(f'Unequip {unequip_select}?').ask()
                    if unequip_confirm:
                        self.unequip_item(unequip_select)
                        printc(f'Item unequipped: [bold green]{unequip_select}[/bold green]')
                        questionary.press_any_key_to_continue().ask()
                        continue
            else:
                for itemENC in self.inventoryENC:
                    if itemENC.name == item_select:
                        itemENC.give_details()
                        print(' ')

                options_choice = questionary.select('Options: ', choices=['<--BACK', 'Equip/Use item', 'Drop item']).ask()

                if options_choice == '<--BACK':
                    continue
#EQUIPPING BANDAIDS-----
                elif options_choice == 'Equip/Use item':
                    if item_select.startswith('BandAid'):
                        item_confirm = questionary.confirm(f"Use a Band-Aid?").ask()
                        if item_confirm:
                            if self.HP == 100:
                                printc('HP is already at max. Your item was not used.', 'bold yellow')
                                questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                                continue
                            else:
                                self.equip_item(item_select)
                                printc(f'Used: [bold white]BandAid[/bold white] ---> [bold green]+10 HP[/bold green]')
                                questionary.press_any_key_to_continue().ask()
                                continue
                        else:
                            continue


                    for itemENC in self.inventoryENC:
                        if itemENC.name == item_select:
#ITEMS AND WEAPONS-----
                            if itemENC.category == 'item' or itemENC.category == 'weapon':
                                if len(self.inventoryDEC) >= self.inventoryMaxCapacity:
                                    printc("Inventory space is at max capacity. (10) Try dropping unwanted items!\n", 'bold yellow')
                                    questionary.press_any_key_to_continue().ask()
                            
                                else:
                                    item_confirm = questionary.confirm(f"Equip {item_select}?").ask()
                                    if item_confirm:
                                        self.equip_item(item_select)
                                        printc(f'Item equipped: [bold green]{item_select}[/bold green]')
                                        questionary.press_any_key_to_continue().ask()
                                        continue
                                    else:
                                        continue
#OTHER HEALTH ITEMS--------                                     
                            elif itemENC.category == 'health':
                                item_confirm = questionary.confirm(f"Equip {item_select}?").ask()
                                if item_confirm:
                                    if self.fighting:
                                        if self.HP == 100:
                                            printc("HP is already at max. You won't be able to equip this item.", 'bold yellow')
                                            questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                                            continue
                                        else:
                                            self.equip_item(item_select)
                                            questionary.press_any_key_to_continue().ask()
                                            continue
                                    else:
                                        type('You can only use this item in battle!\n', 'bold yellow')
                                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                                        clrlines(2)
                                        continue
                                else:
                                    continue
#ARMOUR ITEMS-------------------                           
                            elif itemENC.category == 'armour':
                                if len(self.armour_equippedDEC) >=3:
                                    printc('Cannot equip more than 3 items of armour. Please Unequip one first!', 'bold red')
                                    questionary.press_any_key_to_continue().ask()
                                    continue
                                else:
                                    item_confirm = questionary.confirm(f"Equip {item_select}?").ask()
                                    if item_confirm:
                                        self.equip_item(item_select)
                                        printc(f'Equipped: [bold white]{item_select}[/bold white] ---> [bold green]Protection {itemENC.healthProt}[/bold green]')
                                        questionary.press_any_key_to_continue().ask()
                                        continue
                                    else:
                                        continue
#DROPPING ITEMS-----------------------   
                elif options_choice == 'Drop item':
                    if not self.drop_item_able:
                        printc('You cannot drop an item here.', 'bold yellow')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        continue

                    if self.fighting:
                        printc('You cannot drop an item whilst in battle!', 'bold yellow')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        continue
                    elif item_select.startswith('BandAid'):
                        printc('You cannot drop this item.\n', 'bold red')
                        questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
                        continue
                    else:
                        drop_confirm = questionary.confirm(f"Drop {item_select}?").ask()
                        if drop_confirm:
                            self.drop_item(item_select)
                            printc(f"{item_select} dropped in position '{self.positionENC.name}'.")
                            questionary.press_any_key_to_continue().ask()
                            continue
                        else:
                            continue

    def equip_item(self, item):
        if 'BandAid' in item:
            for itemDEC in self.inventoryDEC:
                if itemDEC.startswith('BandAid'):
                    self.heal(10)
                    if self.number_of_bandaids > 0:
                        self.number_of_bandaids -= 1

                        for i, inventory_item in enumerate(self.inventoryDEC):
                            if inventory_item.startswith('BandAid'):
                                if self.number_of_bandaids == 0:
                                    self.inventoryDEC.pop(i)
                                else:
                                    self.inventoryDEC[i] = f'BandAid ×{self.number_of_bandaids}'
                                break
                        
                    else: #Code shouldnt go here
                        printc('[bold yellow]No BandAids left to use![/bold yellow]')
                        questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
        else:
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    if itemENC.category == 'item' or itemENC.category == 'weapon' or itemENC.category == 'health':
                        if self.item_equippedDEC == 'None':
                            self.item_equippedDEC = itemENC.name
                            self.item_equippedENC = itemENC
                            self.inventoryENC.remove(itemENC)
                            self.inventoryDEC.remove(itemENC.name)
                            self.total_equipped.append(self.item_equippedDEC)

                        else:
                            self.inventoryDEC.append(self.item_equippedDEC)
                            self.inventoryENC.append(self.item_equippedENC)
                            self.total_equipped.remove(self.item_equippedDEC)
                            self.item_equippedDEC = itemENC.name
                            self.item_equippedENC = itemENC
                            self.inventoryENC.remove(itemENC)
                            self.inventoryDEC.remove(itemENC.name)
                            self.total_equipped.append(self.item_equippedDEC)

                    elif itemENC.category == 'armour':
                        self.armour_equippedENC.append(itemENC)
                        self.armour_equippedDEC.append(itemENC.name)
                        self.total_equipped.append(itemENC.name)
                        self.inventoryENC.remove(itemENC)
                        self.inventoryDEC.remove(itemENC.name)

                else:
                    continue

    def unequip_item(self, item):
        for armourENC in self.armour_equippedENC:
            if armourENC.name == item:
                self.inventoryENC.append(armourENC)
                self.inventoryDEC.append(armourENC.name)
                self.total_equipped.remove(armourENC.name)
                self.armour_equippedENC.remove(armourENC)
                self.armour_equippedDEC.remove(armourENC.name)
                return

        if self.item_equippedENC.category != 'None':    
            self.inventoryENC.append(self.item_equippedENC)
            self.inventoryDEC.append(self.item_equippedDEC)
            self.total_equipped.remove(self.item_equippedDEC)
            self.item_equippedENC = 'None'
            self.item_equippedDEC = 'None'
        
    def remove_item(self, item):
        if self.item_equippedDEC == 'None':
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    self.inventoryENC.remove(itemENC)
                    self.inventoryDEC.remove(itemENC.name)
        else:
            self.unequip_item(self.item_equippedDEC)
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    self.inventoryENC.remove(itemENC)
                    self.inventoryDEC.remove(itemENC.name)

    def drop_item(self, item):
        if self.item_equippedDEC == 'None':
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    self.inventoryENC.remove(itemENC)
                    self.inventoryDEC.remove(itemENC.name)
                    self.positionENC.actions.append(f'T - Pick up {itemENC.name}')
                    self.dropped_items.append(itemENC)
        else:
            self.item_equippedDEC = 'None'
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    self.inventoryENC.remove(itemENC)
                    self.inventoryDEC.remove(itemENC.name)
                    self.positionENC.actions.append(f'T - Pick up {itemENC.name}')
                    self.dropped_items.append(itemENC)
                    
            
        
        

    def add_item(self, item):
        if item.name == 'BandAid':
            if self.number_of_bandaids == 0:
                self.number_of_bandaids = 1
                self.inventoryDEC.append(f'BandAid ×{self.number_of_bandaids}')
            else:
                self.number_of_bandaids += 1
                for i, inventory_item in enumerate(self.inventoryDEC):
                    if inventory_item.startswith('BandAid'):
                        self.inventoryDEC[i] = f'BandAid ×{self.number_of_bandaids}'
                        break

            printc(f'[bold green]+1 BandAid[/bold green]')
            print(' ')
            questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
            clrline()
            clrline()
            clrline()


        else:
            for drop in self.dropped_items:
                if drop.name == item.name:
                    self.dropped_items.remove(drop)
                    
                    for pos in self.positionENC.actions:
                        if 'T - Pick up'in pos:
                            if item.name in pos:
                                self.positionENC.actions.remove(pos)
            self.inventoryENC.append(item)
            printc(f'[bold green]New item: {item.name}[/bold green]')
            self.inventoryDEC.append(item.name)
            print(' ')
            questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
            clrline()
            clrline()
            clrline()

                
    def win(self):
        #WIN SEQENCE - PROGRAMME IS QUIT FROM HERE
        pass

    def kill_check(self):
        if self.Alive == False:
            no_HP()
            sleep(2)
        else:
            return 'ALIVE'
        

    def take_damage(self, damage):
        if len(self.armour_equippedENC) > 0:
            damage_decrease = 0
            for armour in self.armour_equippedENC:
                damage_decrease += armour.healthProt

            damage -= damage_decrease
            self.HP -= damage

        else:
            self.HP -= damage
        if self.HP <= 0:
            self.Alive = False

        killCheck = self.kill_check()
        if killCheck == 'ALIVE':
            return 'ALIVE', damage
        else:
            return 'DEAD'
    
    def attack(self):
        if self.item_equippedENC.category == 'health':
            if self.item_equippedENC.single_use:
                self.heal(self.item_equippedENC.health)
                type(f'{self.name} used {self.item_equippedDEC}! (+{self.item_equippedENC.health}HP)', 'bold green')
                sleep(1)
                healed = self.item_equippedENC.health
                self.remove_item(self.item_equippedDEC)
                return 'HEALED' , healed
            
            else:
                self.heal(self.item_equippedENC.health)
                type(f'{self.name} used {self.item_equippedDEC}! (+{self.item_equippedENC.health}HP)', 'bold green')
                sleep(1)
                return 'HEALED' , self.item_equippedENC.health

        elif self.item_equippedENC.category == 'weapon':
            if self.item_equippedENC.single_use:
                type(f'{self.name}')
                type(f' used {self.item_equippedENC.name}!\n', 'bold purple')
                sleep(1)
                attacked = self.item_equippedENC.damage
                self.remove_item(self.item_equippedDEC)
                return 'ATTACKED', attacked
            
            else:
                type(f'{self.name}')
                type(f' used {self.item_equippedENC.name}!\n', 'bold purple')
                sleep(1)
                return 'ATTACKED', self.item_equippedENC.damage
        
        else:
            type(f'You cannot use this item as it is not a weapon!\n')
            questionary.press_any_key_to_continue('Press any key to dismiss...').ask()
            return 'NO ATTACK'


    def heal(self, health):
        self.HP += health
        if self.HP > 100:
            self.HP = 100

    def update_active_SQ(self, SQ):
        self.activeSQ = SQ

    def complete_area(self, area):
        clr()
        pyfiglet.print_figlet(" A R E A", font="slant", colors='green')
        sleep(0.7)
        pyfiglet.print_figlet(" COMPLETE !", font="slant", colors='green')
        sleep(1)
        self.completed_areas.append(area.name)
        self.current_area = 'None'
        print(' ')
        questionary.press_any_key_to_continue().ask()
        ld(7)

    def new_area(self, area):
        self.current_area = area.name


#-------------------------------------------------------ITEMS

class item:
    def __init__(self, name, single_use=False):
        self.name = name
        self.category = 'item'
        self.single_use = single_use

    def give_details(self):
            if not self.single_use:
                printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold yellow]item[/bold yellow]')
            else:
                printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold yellow]item[/bold yellow]')


class armour(item):
    def __init__(self, name, healthProt, single_use=False):
        super().__init__(name, single_use=False)
        self.healthProt = healthProt
        self.category = 'armour'
        self.single_use = single_use
        
    def give_details(self):
        if not self.single_use:
            printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold blue]Armour[/bold blue]    PROTECTION: [bold green]{self.healthProt}[/bold green]')
        else:
            printc(f'ITEM: [bold white]{self.name} (SINGLE USE)[/bold white]     CATEGORY: [bold blue]Armour[/bold blue]    PROTECTION: [bold green]{self.healthProt}[/bold green]')


class weapon(item):
    def __init__(self, name, damage, single_use=False):
        super().__init__(name, single_use=False)
        self.damage = damage
        self.category = 'weapon'
        self.single_use = single_use

    def give_details(self):
        if not self.single_use:
            printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold red]Weapon[/bold red]    DAMAGE: [bold green]{self.damage}[/bold green]')
        else:
            printc(f'ITEM: [bold white]{self.name} (SINGLE USE)[/bold white]     CATEGORY: [bold red]Weapon[/bold red]    DAMAGE: [bold green]{self.damage}[/bold green]')

class health(item):
    def __init__(self, name, health, single_use=False):
        super().__init__(name, single_use=False)
        self.health = health
        self.category = 'health'
        self.single_use = single_use
        
    def give_details(self):
        if not self.single_use:
            printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold magenta]Health[/bold magenta]    HEALTH: [bold green]+{self.health}[/bold green]')
        else:
            printc(f'ITEM: [bold white]{self.name} (SINGLE USE)[/bold white]     CATEGORY: [bold magenta]Health[/bold magenta]    HEALTH: [bold green]+{self.health}[/bold green]')

#-------------------------------------------------------AREAS & NAVIGATION

class area:
    def __init__(self, name):
        self.name = name

class side_quest:
    def __init__(self, code):
        self.code = code
        self.active = False
        self.complete = False

    def start_sq(self, player):
        if player.activeSQ == 'None':
            player.update_active_SQ(self.code)
            self.active = True

        else:
            return 'SQ_ERROR'
        
    def complete_sq(self, player):
        self.complete = True
        self.active = False
        player.activeSQ = 'None'

#-------------------------------------------------------ENTITIES & BOSSES

class entity:
    def __init__(self, name, position):
        self.name = name
        self.poition = position
        self.approachable = True

    def complete(self):
        self.approachable = False
        
class NPC(entity):
    def __init__(self, name, position, interactions):
        super().__init__(name, position)
        self.interactions = interactions

    def interact(self, interact_number):
        self.interactions[interact_number-1]()

class boss:
    def __init__(self, name, attacks):
        self.name = name
        self.HP = 100
        self.alive = True
        self.attacks = attacks

    def heal(self, health):
        self.HP += health
        if self.HP > 100:
            self.HP = 100

    def attack(self, attack):
        if attack.heal:
            self.heal(attack.damage)
            type(f'{self.name} used {attack.name}! (+{attack.damage}HP)\n', 'bold green')
            sleep(1)
            clrlines(1)
            return 0
            
        else:
            type(f'{self.name} ')
            type(f'{attack.name}!\n', 'red')
            sleep(1)
            return attack.damage
        
    def kill_check(self):
        if self.HP <= 0:
            self.alive = False
    
    def take_damage(self, damage):
        self.HP -= damage
        self.kill_check()
        if self.alive == False:
            return 'PLAYER WIN'
        else:
            return damage


class attack:
    def __init__(self, name, damage, heal=False):
        self.name = name
        self.damage = damage
        self.heal = heal
#---------------------------------------------------------POSITION

class position:
    def __init__(self, name, code, actions, options):
        self.name = name
        self.code = code
        self.actions = actions
        self.dropped_items = []
        self.options = options

#---------------------------------------------------------CREATING ALL NECESSARY INSTANCES
Player = player('ALIM', 'None') #PLAYER NAME TST
BandAid = health('BandAid', 10)

Area1 = area('Area 1')
Area2 = area('Area 2')
Area3 = area('Area 3')
Area4 = area('Area 4')
#--------------------------AREA 1--------------------------#
 
#POSITONS----------------
A1Z1_Start = position('Start', 'A1Z1_Start', [], 'ALL')
A1Z1_House = position('House', 'A1Z1_House', ['E - Enter House'], 'ALL')
A1Z1_a = position('A', 'A1Z1_A', [], 'ALL')
A1Z1_BridgeLCK = position('[!]', 'A1Z1_BridgeLCK', ['E - Interact'], 'ALL')
A1Z1_b = position('B', 'A1Z1_B', [], 'ALL')
A1Z1_Chest = position('Chest', 'A1Z1_Chest', ['E - Open Chest'],'ALL')
A1Z1_End = position('End', 'A1Z1_End', ['E - Continue to Zone 2'], 'ALL')

Charlie_House_Door = position('Door', 'Charlie_House_Door', ['E - Exit'], 'ALL')
Charlie_House_a = position('A', 'Charlie_House_a', [], 'ALL')
Charlie_House_Desk = position('Desk', 'Charlie_House_Desk', ['E - Read Note'], 'ALL')
Charlie_House_Bed = position('Bed', 'Charlie_House_Bed', ['E - Check Under Bed'], 'ALL')

A1Z2_Start = position('Start', 'A1Z2_Start', [], 'ALL')
A1Z2_a = position('A', 'A1Z2_A', [], 'WA')
A1Z2_b = position('B', 'A1Z2_B',[], 'ALL')
A1Z2_c = position('C', 'A1Z2_C', [], 'ALL')
A1Z2_d = position('D', 'A1Z2_D', [], 'WSD')
A1Z2_lvr1 = position('Lever 1', 'A1Z2_lvr1', ['E - Pull Lever'], 'ALL')
A1Z2_e = position('E', 'A1Z2_E', [], 'ADW')
A1Z2_f = position('F', 'A1Z2_F', [], 'ALL')
A1Z2_lvr2 = position('Lever 2', 'A1Z2_lvr2', ['E - Pull Lever'], 'ALL')
A1Z2_lckgt1 = position('Gate 1', 'A1Z2_lckgt1', [], 'A')
A1Z2_lckgt2 = position('Gate 2', 'A1Z2_lckgt2', [], 'A')
A1Z2_ulckgt1 = position('Gate 1', 'A1Z2_ulckgt1', [], 'AD')
A1Z2_ulckgt2 = position('Gate 2', 'A1Z2_ulckgt2', [], 'AD')
A1Z2_g = position('G', 'A1Z2_G', [], 'ADS')
A1Z2_Chest = position('Chest', 'A1Z2_Chest', ['E - Open Chest'], 'ALL')
A1Z2_End = position('End', 'A1Z2_End', ['E - Continue to Zone 3'], 'ALL')

A1Z3_Start = position('Start', 'A1Z3_Start', [], 'ALL')
A1Z3_a = position('A', 'A1Z3_A', [], 'WSA')
A1Z3_c = position('C', 'A1Z3_C', [], 'ALL')
A1Z3_lvr = position('Lever', 'A1Z3_lvr', ['E - Pull Lever'], 'A')
A1Z3_b = position('B', 'A1Z3_B' ,[], 'ALL')
A1Z3_d = position('D', 'A1Z3_D', [], 'ALL')
A1Z3_lcke = position('E', 'A1Z3_lckE', [], 'AW')
A1Z3_ulcke = position('E', 'A1Z3_ulckE', [], 'AWD')
A1Z3_Chest = position('Chest', 'A1Z3_Chest', ['E - Open Chest'], 'D')
A1Z3_f = position('F', 'A1Z3_F', [], 'ALL')
A1Z3_m = position('M', 'A1Z3_M', [], 'DA')
A1Z3_End = position('End', 'A1Z3_End', ['E - Continue to Zone 4'], 'WDS')

A1Z4_Start = position('Start', 'A1Z4_Start', [], 'ALL')
A1Z4_a = position('A', 'A1Z4_A', [], 'ALL')
A1Z4_Chest = position('Chest', 'A1Z4_Chest', ['E - Open Chest'], 'ALL')
A1Z4_bb = position('End', 'A1Z4_BB', ['E - Continue'], 'ALL')

A2Z1_Start = position('Start', 'A2Z1-Start', [], 'ALL')
A2Z1_a = position('A', 'A2Z1_A', [], 'ALL')
A2Z1_b = position('B', 'A2Z1_B', [], 'ALL')
A2Z1_c = position('C', 'A2Z1_C', [], 'ALL')
A2Z1_d = position('D', 'A2Z1_D', [], 'WSA')
A2Z1_e = position('E', 'A2Z1_E', [], 'SWD')
A2Z1_f = position('F', 'A2Z1_F', [], 'ALL')
A2Z1_g = position('G', 'A2Z1_G', [], 'ALL')
A2Z1_h = position('H', 'A2Z1_H', [], 'ALL')
A2Z1_i = position('I', 'A2Z1_I', [], 'ALL')
A2Z1_End = position('End', 'A2Z1_End', ['E - Continue to Zone 2'], 'ALL')
A2Z1_Chest = position('Chest', 'A2Z1_Chest', ['E - Open Chest'], 'ALL')
A2Z1_Crate = position('Crate', 'A2Z1_Crate', ['E - Read Note', 'Q - Exit'], 'S')







#SIDE QUESTS--------------
SQ1 = side_quest('SQ1')

#ITEMS------------------
Charlie_House_key = item("Charlie's House Key", 'item')
Bridge_key_A1Z1 = item("Bridge Key", 'item')
spear = weapon('Spear', 20)
shield = armour('Sheild', 10)
arcane_rune = weapon('Arcane Rune', 50, True) #SINGLE USE
knife = weapon('Knife', 11)
battle_axe = weapon('Battle axe', 22)
Medkit = health('Medkit', 30, True)

#NPCs---------------------
NPC_Charlie = NPC('Charlie', 'Bridge', [Charlie.interaction1, Charlie.interaction2, Charlie.interaction3])
NPC_anonymous_civilian = NPC('Anonymous Civilian', 'Lever', [Anonymous_Civilian.start_interaction1, Anonymous_Civilian.start_interaction2])
NPC_Zexrash = NPC('Zexrash', 'End', [Zexrash.interaction])

#--------------------------BOSS ELEMENTS
basic_attack_ZR = attack('throws a knife', 11)
medium_attack_ZR = attack('swings a battle axe', 22)
special_attack_ZR = attack('uses special attack', 30)
heal_ZR = attack('Heal', 15, True)


zexrash = boss('Zexrash', [basic_attack_ZR, medium_attack_ZR, special_attack_ZR, heal_ZR])