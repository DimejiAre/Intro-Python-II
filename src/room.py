# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light=True):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light

    def __str__(self):
        return f"Room: {self.name}, Description: {self.description}"

    def add_item_room(self,*args):
        for arg in args:
            self.items.append(arg)
        return f"item has been added"

    def remove_item_room(self,item_name):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
        return f"item has been removed"

    def view_items_room(self):
        output = "\nItems in the Room Are: \n"
        if len(self.items) > 0:
            for item in self.items:
                output += f"{item.name}: {item.description}\n"
            return output
        else:
            return f"No items in this room\n"

    def check_item_room(self, item_name):
        for item in self.items:
            if item_name == item.name:
                return item
        return False
