# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def handle_command(self, cmd):
        direction = f"{cmd}" + "_to"
        if getattr(self.room, direction) is not None:
            self.room = getattr(self.room, direction)
        else:
            print("\nYou can't go in that direction")