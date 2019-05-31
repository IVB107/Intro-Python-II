from room import Room
from player import Player
from item import Item

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

# Define Items

rock = Item("rock", "Great for bashing stuff.")
torch = Item("torch", "Don't burn yourself!")
key = Item("key", "I wonder what this is used for...")
potion = Item("potion", "Good for your health! (+10 HP)")
plumbus = Item("plumbus", "Have you ever seen how these things are made?")
coin = Item("coin", "Currency of the Derp Empire. (+10 Derps)")
dagger = Item("dagger", "This looks like it could do some damage!")
rope = Item("rope", "Never know when you'll need some rope, I guess.")

room['outside'].items.append(rock)
room['outside'].items.append(potion)
room['foyer'].items.append(torch)
room['dungeon'].items.append(key)
room['dungeon'].items.append(coin)
room['narrow'].items.append(potion)
room['overlook'].items.append(plumbus)
room['tower'].items.append(coin)
room['tunnel'].items.append(dagger)
room['treasure'].items.append(rope)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("IVB", room['outside'])

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

commands = ["n", "s", "e", "w"]
print(player.room)

while True:
    command = input("\nSelect your move: ")
    if command == "q":
        print(f"\nGoodbye.\n")
        break
    elif command in commands:
        player.handle_command(command)
        player.room.get_exits()
    elif command == "items":
        player.room.list_items()
    elif command == "grab":
        item = input("\nItem to pick up: ")
        player.grab_item(item)
    elif command == "drop":
        item = input("\nItem to lose: ")
        player.drop_item(item)
        # drop an item from your inventory
    elif command == "inventory":
        player.list_inventory()
    elif command == "help":
        print("\nNo help available right now, sorry bud.")
    else:
        print(f"\nInvalid selection - Try again, or type \"help\" for more options.\n")