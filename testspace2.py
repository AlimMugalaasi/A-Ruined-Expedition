
'''
if itemENC.name == 'BandAid':
                        self.heal(itemENC.health)
                        if self.number_of_bandaids > 0:
                            self.number_of_bandaids -= 1

                            for i, inventory_item in enumerate(self.inventoryDEC):
                                if inventory_item.startswith('BandAid'):
                                    if self.number_of_bandaids == 0:
                                        self.inventoryDEC.pop(i)
                                    else:
                                        self.inventoryDEC[i] = f'BandAid ×{self.number_of_bandaids}'
                                    break
                            
                        else: #Code shouldnt go here i believe
                            printc('[bold yellow]No BandAids left to use![/bold yellow]')
                            questionary.press_any_key_to_continue(message='Press any key to dismiss...').ask()

'''