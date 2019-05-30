# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def handle_command(self, cmd):
        # commands = ["n", "s", "e", "w"]
        if cmd == "n":
            if self.room.n_to is not None:
                self.room = self.room.n_to
            else:
                print("You can't go in that direction.")
        if cmd == "s":
            if self.room.s_to is not None:
                self.room = self.room.s_to
            else:
                print("You can't go in that direction.")
        if cmd == "e":
            if self.room.e_to is not None:
                self.room = self.room.e_to
            else:
                print("You can't go in that direction.")
        if cmd == "w":
            if self.room.w_to is not None:
                self.room = self.room.w_to
            else:
                print("You can't go in that direction.")