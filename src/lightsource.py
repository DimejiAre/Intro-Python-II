from item import Item

class Lightsource(Item):
    def __init__(self, name, description):
        super().__init__(name,description)
    
    def on_drop(self):
        return f"Is it wise to drop your source of light?"