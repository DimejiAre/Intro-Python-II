# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def add_item_inventory(self, item):
        self.inventory.append(item)
        return ""
    
    def remove_item_inventory(self,item_name):
        for item in self.inventory:
            if item_name == item.name:
                self.inventory.remove(item)
        return f"item has been removed"

    def view_inventory(self):
        output = "\nYour Inventory: \n"
        if len(self.inventory) > 0:
            for item in self.inventory:
                output += f"{item.name}, {item.description}\n"
            return output
        else:
            return f"Your Inventory is empty"
    
    def get_item_name(self, item_name):
        for item in self.inventory:
            if item_name == item.name:
                return item
            else:
                return False
            
