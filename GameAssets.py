from ExtraFunctions import printc, clr, sleep
import questionary

class player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.current_area = 'A1'
        self.current_zone = 'Z1'
        self.inventory = ['CLOSE']
        self.inventoryMaxCapacity = 25 #not final
        self.item_equipped = None
        self.HP = 100
        self.Alive = True
        self.completed_areas = []
        self.completed_zones = []
        self.Win = False
        self.activeSQ = 'SQ1'


    def move(self, position):
        self.position = position
    
    def open_inventory(self):
        while True:
            clr()
            printc('INVENTORY', 'underline green bold italic')
            item_select = questionary.select("Select An item to equip it, or select CLOSE to close inventory\n", choices=self.inventory, qmark='>').ask()
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

        print(self.item_equipped)
        #ADD options to unequip items (you can do this by maybe an option on the list)

    def equip_item(self, item):
        if self.item_equipped == None:
            self.item_equipped = item
            self.inventory.remove(item)

        else:
            self.inventory.append(self.item_equipped)
            self.item_equipped = item
            self.inventory.remove(item)

Player = player('John', 'A1egsr')

Player.open_inventory()
