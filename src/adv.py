from room import Room
from player import Player
from item import Item
from lightsource import Lightsource

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
to north. The smell of gold permeates the air.""", False),

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

# items

item = {
    'coin': Item("coin", "20 Gold coins"),
    'sword': Item("sword", "For slaying Ogres"),
    'lamp': Lightsource("lamp", "lightsource"),
    'pendant': Item("pendant", "crystal pendant")
}

# add items to rooms
room['foyer'].add_item_room(item['lamp'], item['pendant'])
room['overlook'].add_item_room(item['coin'])
room['narrow'].add_item_room(item['sword'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

print(f"\nWelcome to Adventure Game!!!")

name = input("\nEnter your player name: ")
player = Player(name, 'outside')
current_room = room[player.current_room]
print(f"\nHello! {name}, Current Room: {player.current_room}")
print(f"{current_room.view_items_room()}")

while True:
    decision = input("Enter Command:\n\n1)Enter direction to move\n(n=North,s=South,e=East,w=West)\n2)Pick or Drop an item\n(take <item>, drop <item>)\n3)Enter i to check inventory\n4)Enter c to view current room\n5)Enter q to quit\n\n:")
    action = decision.split(' ')

    if (len(action) > 1) and (action[0] == 'take' or action[0] == 'get'):
        item = current_room.check_item_room(action[1])
        if item:
            print(item.on_take())
            player.add_item_inventory(item)
            current_room.remove_item_room(item.name)
        else:
            print("\nThis item is not in this room")
    elif len(action) > 1 and (action[0] == 'drop'):
        item = player.get_item_name(action[1])
        if item:
            print(item.on_drop())
            player.remove_item_inventory(item.name)
            current_room.add_item_room(item)
        else:
            print("\nThis item is not in your inventory")
    else:
        if decision is "s" and hasattr(current_room, 's_to'):
            current_room = current_room.s_to
            if current_room.is_light or player.get_item_name('lamp'):
                print(f"\nCurrent {current_room} \n")
                print(f"{current_room.view_items_room()}")
        elif decision is "n" and hasattr(current_room, 'n_to'):
            current_room = current_room.n_to
            if current_room.is_light or player.get_item_name('lamp'):
                print(f"\nCurrent {current_room} \n")
                print(f"{current_room.view_items_room()}")
        elif decision is "e" and hasattr(current_room, 'e_to'):
            current_room = current_room.e_to
            if current_room.is_light or player.get_item_name('lamp'):
                print(f"\nCurrent {current_room} \n")
                print(f"{current_room.view_items_room()}")
            else:
                print(f"\nThis room is pitch black, perhaps get a light source")
        elif decision is "w" and hasattr(current_room, 'w_to'):
            current_room = current_room.w_to
            if current_room.is_light or player.get_item_name('lamp'):
                print(f"\nCurrent {current_room} \n")
                print(f"{current_room.view_items_room()}")
        elif decision is "i":
            print(player.view_inventory())
        elif decision is "c":
            if current_room.is_light or player.get_item_name('lamp'):
                print(f"\nCurrent {current_room} \n")
                print(f"{current_room.view_items_room()}")
            else:
                print(f"\nThis room is pitch black, perhaps get a light source")
        elif decision is "q":
            print(f"Thank you for playing!")
            break
        else:
            print("Dead End!! There is no room in this direction\n")

    