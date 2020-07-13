from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# purse = 

room['foyer'].item.append("purse")
room['overlook'].item.append("flowers")
room['narrow'].item.append("laptop")
room['treasure'].item.append("necklace")


#
# Main
#
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
item=['flowers', 'purse', 'laptop', 'book']

newPlayer = input("Welcome! Enter Player name: ")
player1 = Player(newPlayer, room['outside'])

print(f"Let's play... {player1.current_room.current_description}")

# for str in textwrap.wrap(player1.current_room.current_description):
#     print(str)

valid_commands = ("n", "s", "e", "w", "q")
item_commands = ("get", "drop")

while True:
    valid_commands = input("Enter which way you'd like to travel: ")
    if valid_commands == 'q':
        print("Thanks for playing, see you next time!")
        exit()
    elif valid_commands == "n":
        try: 
            player1.current_room = player1.current_room.n_to
            print("Current Room: ", player1.current_room, "- " + player1.current_room.current_description)
        except:
            print("Try another direction")
    elif valid_commands == "s":
        try: 
            player1.current_room = player1.current_room.s_to
            print("Current Room: ", player1.current_room, "- " + player1.current_room.current_description)
        except:
            print("Try another direction")
    elif valid_commands == "e":
        try: 
            player1.current_room = player1.current_room.e_to
            print("Current Room: ", player1.current_room, "- " + player1.current_room.current_description)
        except:
            print("Try another direction")
    elif valid_commands == "w":
        try: 
            player1.current_room = player1.current_room.w_to
            print("Current Room: ", player1.current_room, "- " + player1.current_room.current_description)
        except:
            print("Try another direction")
    elif valid_commands != ("n", "s", "e", "w"):
        print("Please enter a direction to travel:'n', 's', 'e', 'w'")

    # Code to pick up items in different rooms
    # this code isn't the prettiest, I'll work on it more later
    item_commands = input("Enter 'get' or 'drop' for items: ")
    print(f"Player: {player1.name}, " "is in the " f"{player1.current_room.name}.")
    if item_commands == "get" and valid_commands == "n":
        print(f"{player1.name} is carrying {player1.item} ", item[0])
    elif item_commands == "get" and valid_commands == "s":
        print(f"{player1.name} is carrying {player1.item} a", item[1])
    elif item_commands == "get" and valid_commands == "e":
        print(f"{player1.name} is carrying {player1.item} a", item[2])
    elif item_commands == "get" and valid_commands == "w":
        print(f"{player1.name} is carrying {player1.item} a", item[3])
    elif item_commands == "drop":
        print("You've dropped the item")
else:
    print("Please try again with different command \n")

