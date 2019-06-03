# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
    def __str__(self):
        return_str =  f"\n--------------------\n\nLocation: {self.name}"
        return_str += f"\n\nDescription: {self.description}"
        # return_str += f"\n\nItems: {self.items}"
        return_str += f"\n\nExits: [{self.get_exits()}]"
        return return_str
    def list_items(self):
        print(f"\nItems: {self.items}")
    def get_exits(self):
        exits = []
        for direction in ["n", "s", "e", "w"]:
            attr = f"{direction}" + "_to"
            if getattr(self, attr) is not None:
                exits.append(f"{direction}")
        return ", ".join(exits)
    def add_item(self, name, description):
        self.items.append(Item(f"{name}", f"{description}"))