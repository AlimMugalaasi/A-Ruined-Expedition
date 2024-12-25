from Functions import printc, clr, sleep, type, ld, clrline
import questionary
import NPCInteractions.Charlie as Charlie
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
        self.completed_zones = []
        self.activeSQ = 'None'
        self.stored_action = 'None'
        #-------------------------NECESSARY ONE-TIME ATTRIBUTES
        self.ReadNote = False
    
    def open_inventory(self):
        while True:
            clr()
            printc('INVENTORY', 'underline green bold italic')
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
                                    printc(f'Cannot carry more than {self.inventoryMaxCapacity} items. Please drop/use one first!', 'bold red')
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
                                item_confirm = questionary.confirm(f"Use {item_select}?").ask()
                                if item_confirm:
                                    self.equip_item(item_select)
                                    printc(f'Used: [bold white]{item_select}[/bold white] ---> [bold green]+{itemENC.health}HP[/bold green]')
                                    questionary.press_any_key_to_continue().ask()
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
    
                elif options_choice == 'Drop item':
                    #DONT ALLOW TO DROP A BANDAID
                    #drop_confirm = questionary.confirm(f"Drop {item_select}?").ask()
                        #if drop_confirm:
                            #self.drop_item(item_select) - will have to remove from inventory ENC + DEC
                            #printc(f'{item_select} dropped in position {position of where it was dropped}.')
                            #questionary.press_any_key_to_continue().ask()
                            #continue
                        #else:
                            #continue
                    continue

    def equip_item(self, item):
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

        for itemENC in self.inventoryENC:
            if itemENC.name == item:
                if itemENC.category == 'item' or itemENC.category == 'weapon':
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

                elif itemENC.category == 'health':  
                        self.heal(itemENC.health)
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
            self.item_equippedDEC = 'None'
            for itemENC in self.inventoryENC:
                if itemENC.name == item:
                    self.inventoryENC.remove(itemENC)
                    self.inventoryDEC.remove(itemENC.name)
            
        
        

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
            #if len(self.inventoryDEC) >= self.inventory_max_capacity:
                self.inventoryENC.append(item)
                printc(f'[bold green]New item: {item.name}[/bold green]')
                self.inventoryDEC.append(item.name)
                print(' ')
                questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
                clrline()
                clrline()
                clrline()
            #else:
                '''
                self.drop_item(item)
                printc(f'[bold red]Dropped item: {item.name} (Inventory at max capacity)[/bold red]')
                self.inventoryENC.append(item)
                printc(f'[bold green]New item: {item.name}[/bold green]')
                self.inventoryDEC.append(item.name)
                print(' ')
                questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
                clrline()
                clrline()
                clrline()
                '''
    def win(self):
        #WIN SEQENCE - PROGRAMME IS QUIT FROM HERE
        pass

    def kill_check(self):
        if self.Alive == False:
            #DEATH SEQUENCE - PROGRAMME IS QUIT FROM HERE(or respawn)
            pass

        else:
            return
        

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

        self.kill_check()

    def heal(self, health):
        self.HP += health
        if self.HP > 100:
            self.HP = 100

    def update_active_SQ(self, SQ):
        self.activeSQ = SQ

#-------------------------------------------------------ITEMS

class item:
    def __init__(self, name, category):
        self.name = name
        self.category = 'item'

    def give_details(self):
            printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold yellow]item[/bold yellow]')
            

class armour(item):
    def __init__(self, name, category, healthProt):
        super().__init__(name, category)
        self.healthProt = healthProt
        self.category = 'armour'
        
    def give_details(self):
        printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold blue]Armour[/bold blue]    PROTECTION: [bold green]{self.healthProt}[/bold green]')
        

class weapon(item):
    def __init__(self, name, category, damage):
        super().__init__(name, category)
        self.damage = damage
        self.category = 'weapon'

    def give_details(self):
        printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold red]Weapon[/bold red]    DAMAGE: [bold green]{self.damage}[/bold green]')

class health(item):
    def __init__(self, name, category, health):
        super().__init__(name, category)
        self.health = health
        self.category = 'health'

    def give_details(self):
        printc(f'ITEM: [bold white]{self.name}[/bold white]     CATEGORY: [bold magenta]Health[/bold magenta]    HEALTH: [bold green]+{self.health}[/bold green]')

#-------------------------------------------------------AREAS & NAVIGATION

def complete_area(self, area):
        clr()
        type('AREA COMPLETE!', 'bold green')
        self.completed_areas.append(area.name)
        self.current_area = None
        print(' ')
        questionary.press_any_key_to_continue().ask()
        ld()

def new_area(self, area):
    self.current_area = area.code


class area:
    def __init__(self, name, code):
        self.name = name
        self.code = code

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

#---------------------------------------------------------POSITION

class position:
    def __init__(self, name, code, actions):
        self.name = name
        self.code = code
        self.actions = actions
        self.dropped_items = []

#---------------------------------------------------------LOADING ALL ASSETS
Player = player('ALIM', 'None') #PLAYER NAME TST

#------AREA 1-------#
 
#POSITONS----------------
A1Z1_Start = position('Start', 'A1Z1-Start', [])
A1Z1_House = position('House', 'A1Z1-House', ['E - Enter House'])
A1Z1_a = position('A', 'A1Z1-A', [])
A1Z1_BridgeLCK = position('[!]', 'A1Z1-BridgeLCK', ['E - Interact'])
A1Z1_b = position('B', 'A1Z1-B', [])
A1Z1_c = position('C', 'A1Z1-C', [])
A1Z1_Chest = position('Chest', 'A1Z1-Chest', ['E - Open Chest'])

Charlie_House_Door = position('Door', 'Charlie_House_Door', ['E - Exit'])
Charlie_House_a = position('A', 'Charlie_House_a', [])
Charlie_House_Desk = position('Desk', 'Charlie_House_Desk', ['E - Read Note'])
Charlie_House_Bed = position('Bed', 'Charlie_House_Bed', ['E - Check Under Bed'])

#SIDE QUESTS--------------
SQ1 = side_quest('SQ1')

#ITEMS------------------
Charlie_House_key = item("Charlie's House Key", 'item')
Bridge_key_A1Z1 = item("Bridge Key", 'item')
spear = item('Spear', 'weapon')

#NPCs---------------------
NPC_Charlie = NPC('Charlie', 'Bridge', [Charlie.interaction1, Charlie.interaction2, Charlie.interaction3])


