from ExtraFunctions import printc, clr, sleep, type, ld, clrline
import questionary

#-------------------------------------------------------PLAYER

class player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.current_area = 'A1'
        self.current_zone = 'Z1'
        self.inventoryENC = []
        self.inventoryDEC = ['<--BACK', 'EQUIPPED']
        self.inventoryMaxCapacity = 25 #not final
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


    def move(self, position):
        self.position = position
    
    def open_inventory(self):
        while True:
            clr()
            printc('INVENTORY', 'underline green bold italic')
            item_select = questionary.select("Select An item to see further options. Select EQUIPPED to see options for equipped items.\n", choices=self.inventoryDEC, qmark='>').ask()
            if item_select =='<--BACK':
                break
            elif item_select == 'EQUIPPED':
                unequip_select = questionary.select("Select an Item to unequip it", choices=self.total_equipped, qmark='>').ask()
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

                elif options_choice == 'Equip/Use item':
                    for itemENC in self.inventoryENC:
                        if itemENC.name == item_select:

                            if itemENC.category == 'item' or itemENC.category == 'weapon':

                                if len(self.inventoryDEC) >= self.inventoryMaxCapacity:
                                    printc(f'Cannot equip more than {self.inventoryMaxCapacity} items of armour. Please Unequip one first!', 'bold red')
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


                            elif itemENC.category == 'health':
                                item_confirm = questionary.confirm(f"Use {item_select}?").ask()
                                if item_confirm:
                                    self.equip_item(item_select)
                                    printc(f'Used: [bold white]{item_select}[/bold white] ---> [bold green]+{itemENC.health}HP[/bold green]')
                                    questionary.press_any_key_to_continue().ask()
                                    continue
                                else:
                                    continue
                            
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
                    #drop_confirm = questionary.confirm(f"Drop {item_select}?").ask()
                        #if drop_confirm:
                            #self.drop_item(item_select)
                            #printc(f'{item_select} dropped in position {position of where it was dropped}.')
                            #questionary.press_any_key_to_continue().ask()
                            #continue
                        #else:
                            #continue
                    continue

        print(self.item_equippedDEC) # FOR TESTING ONLY

    def equip_item(self, item):
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
        #add item back to both inventory ENC and DEC (do NOT use self.add_item, do it manually)
        #remove equipped items from self.item_equippedENC and DEC (by making them equal to 'None')
        #remove equipped armour from armour equipped list
        pass

    def add_item(self, item):
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
        if player.activeSQ == None:
            player.update_active_SQ(self.code)
            self.active = True

        else:
            return 'SQ_ERROR'
        
    def complete_sq(self, player):
        self.complete = True
        self.active = False
        player.activeSQ = None

#-------------------------------------------------------ENTITIES

clr()

player1 = player('Jake', None)

item1 = weapon('Sword', 'weapon', 20)
item2 = weapon('CrossBow', 'weapon', 40)
item3 = weapon('Spear', 'weapon', 15)
item4 = item('key5', 'item')
item5 = item('key6', 'item')
item6 = armour('Iron Chestplate', 'armour', 10)
item7 = armour('Sheild', 'armour', 15)


player1.add_item(item1)
player1.add_item(item2)
player1.add_item(item3)
player1.add_item(item4)
player1.add_item(item5)
player1.add_item(item6)
player1.add_item(item7)

player1.open_inventory()