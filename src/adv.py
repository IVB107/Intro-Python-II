from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'dungeon': Room("Lower Dungeon", """You have entered the Lower Dungeon. It's very dark except for a single torch on the east wall, illuminating the exits to the north, south and west."""),

    'tower': Room("Grand Tower", """You've made your way to the Grand Tower. At the top is a door that leads east, the bottom leads south to somewhere unknown..."""),

    'tunnel': Room("Secret Tunnel", """What's this? Some sort of hidden tunnel. As you notice a dim light to the south, you notice heavy footsteps quickly approaching behind you!"""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['dungeon']
room['dungeon'].w_to = room['foyer']
room['dungeon'].n_to = room['narrow']
room['narrow'].s_to = room['dungeon']
room['overlook'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['overlook']
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = room['tower']
room['tower'].w_to = room['narrow']
room['tower'].s_to = room['tunnel']
room['tunnel'].n_to = room['tower']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def change_rooms(player_input):
    current_location = None
    for nickname, info in room.items():
        if info.name == player.current_room:
            current_location = nickname
    print(f"The player selected to go {player_input} from {current_location}")

directions = ["n", "s", "e", "w"]

print(f"\nDescription: {player.room.description}")

while True:
    print(f"\nYour Location: {player.room.name}")
    print(f"\nDescription: {player.room.description}")
    command = input("\nSelect your next move: ")
    # print(f"\nWhat would you like to do?")
    if command == "q":
        print(f"\nSee ya later!\n")
        break
    elif command in directions:
        # print(f"You clicked {command}! Well done, you get a cookie.\n")
        change_rooms(command)
        # Logic to move in that direction
    elif command == "help":
        print("No help available right now, sorry bud.\n")
        # Output strings in the format [selection] - "description"
        # eg: "n" - Move north
    else:
        print(f"\nInvalid selection - please try again, or type \"help\" for more options.\n")
