# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    def handle_command(self, cmd):
        direction = f"{cmd}" + "_to"
        if getattr(self.room, direction) is not None:
            self.room = getattr(self.room, direction)
            print(self.room)
        else:
            print("\nYou can't go in that direction")
    def grab_item(self, item):
        for option in self.room.items:
            if item == option.name:
                self.inventory.append({option.name: option.description})
                print(f"Your Inventory: {self.inventory}")
                self.room.items.remove(option)