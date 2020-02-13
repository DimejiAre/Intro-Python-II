class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def on_take(self):
        return f"\nYou have picked up {self.name}"
    
    def on_drop(self):
        return f"\nYou have dropped {self.name}"