from ExtraFunctions import printc, clr, sleep, type, ld, clrline
import questionary

class player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.current_area = 'A1'
        self.current_zone = 'Z1'
        self.inventoryENC = []
        self.inventoryDEC = ['CLOSE']
        self.inventoryMaxCapacity = 25 #not final
        self.item_equippedDEC = None
        self.item_equippedENC = None
        self.armour_equippedDEC = None
        self.armour_equippedENC = None
        self.HP = 100
        self.Alive = True
        self.completed_areas = []
        self.completed_zones = []
        self.activeSQ = None


    def move(self, position):
        self.position = position
    
    def open_inventory(self):
        while True:
            clr()
            printc('INVENTORY', 'underline green bold italic')
            item_select = questionary.select("Select An item to equip it, or select CLOSE to close inventory\n", choices=self.inventoryDEC, qmark='>').ask()
            if item_select =='CLOSE':
                break
            
            else:
                item_confirm = questionary.confirm(f"Equip {item_select}?").ask()
                if item_confirm:
                    self.equip_item(item_select)
                    printc(f'Item equipped: [bold green]{item_select}[/bold green]')
                    questionary.press_any_key_to_continue().ask()
                    continue
                else:
                    continue

        print(self.item_equippedDEC) # FOR TESTING ONLY

    def equip_item(self, item):
        for itemENC in self.inventoryENC:
            if itemENC.name == item:
                if itemENC.category != 'armour':
                    if self.item_equippedDEC == None:
                        self.item_equippedDEC = itemENC.name
                        self.item_equippedENC = itemENC
                        self.inventoryENC.remove(itemENC)
                        self.inventoryDEC.remove(itemENC.name)

                    else:
                        self.inventoryDEC.append(self.item_equippedDEC)
                        self.inventoryENC.append(self.item_equippedENC)
                        self.item_equippedDEC = itemENC.name
                        self.item_equippedENC = itemENC
                        self.inventoryENC.remove(itemENC)
                        self.inventoryDEC.remove(itemENC.name)

                elif itemENC.category == 'armour':
                    if self.armour_equippedDEC == None:
                        self.armour_equippedDEC = itemENC.name
                        self.armour_equippedENC = itemENC
                        self.inventoryENC.remove(itemENC)
                        self.inventoryDEC.remove(itemENC.name)

                    else:
                        self.inventoryDEC.append(self.armour_equippedDEC)
                        self.inventoryENC.append(self.armour_equippedENC)
                        self.armour_equippedDEC = itemENC.name
                        self.armour_equippedENC = itemENC
                        self.inventoryENC.remove(itemENC)
                        self.inventoryDEC.remove(itemENC.name)
                for itemtest in self.inventoryENC:
                    print(itemtest.name)
            else:
                continue

    def unequip_item(self, item):
        for itemENC in self.inventoryENC:
            if itemENC == item:
                self.inventory.append(itemENC.name)
                if itemENC.category == 'armour':
                    self.armour_equippedDEC = None
                else:
                    self.item_equippedDEC = None

            else:
                continue


    def add_item(self, item):
        self.inventoryENC.append(item)
        printc(f'[bold green]New item: {item.name}[/bold green]')
        #WHEN EQUIPPING ARMOUR IT SHOULD SAY WHAT EFFECT IT HAS
        self.inventoryDEC.append(item.name)
        print(' ')
        questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()
        clrline()
        clrline()
        clrline()
    
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
        if len(self.armour_equippedDEC) > 0:
            damage_decrease = 0
            for armour in self.armour_equippedDEC:
                damage_decrease += armour.healthProt

            damage -= damage_decrease
            self.HP -= damage

        else:
            self.HP -= damage
        if self.HP <= 0:
            self.Alive = False

        self.kill_check()
        pass

    def heal(self, health):
        self.HP += health

    def update_active_SQ(self, SQ):
        self.activeSQ = SQ


class item:
    def __init__(self, name, category):
        self.name = name
        self.category = 'item'

class armour(item):
    def __init__(self, name, category, healthProt):
        super().__init__(name, category)
        self.healthProt = healthProt
        self.category = 'armour'
        

class weapon(item):
    def __init__(self, name, category, damage):
        super().__init__(name, category)
        self.damage = damage
        self.category = 'weapon'

class area:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    # def start(self): (Not needed i believe)

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