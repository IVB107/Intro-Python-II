# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
    def list_inventory(self):
        if len(self.inventory) != 0:
            print(f"\nInventory: {self.inventory}")
        else:
            print("\nThere is nothing in your inventory")
    def handle_command(self, cmd):
        direction = f"{cmd}" + "_to"
        if getattr(self.room, direction) is not None:
            self.room = getattr(self.room, direction)
            print(self.room)
        else:
            print("\nYou can't go in that direction")
    def grab_item(self, item):
        if self.room.items is not None:
            for option in self.room.items:
                if item == option.name:
                    self.inventory.append({option.name: option.description})
                    print(f"\nInventory: {self.inventory}")
                    return self.room.items.remove(option)
            else:
                print(f"\nCouldn't find item \"{item}\".")
        else:
            print("No items in this room.")
    def drop_item(self, item):
        for thing in self.inventory:
            key_value = [[name, description] for name, description in thing.items()][0]
            print(f"KEY_VALUE: {key_value}")
            if item == key_value[0]:
                self.inventory.remove(thing)
                print(f"\nDropped: {item}")
                self.room.add_item(key_value[0], key_value[1])
