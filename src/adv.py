from room import Room
from player import Player
from item import Item

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

foyer =  room['foyer']
outside = room['outside']
overlook = room['overlook']
narrow = room['narrow']
treasure = room['treasure']

room['outside'].items.extend(
    [Item("key", "Rusty looking key"), Item("torch", "9000 Lumens Torch")])
room['foyer'].items.append(
    Item("scrap", "scrap of paper, it has something written:Find the teasure"))
room['overlook'].items.append(Item("binocular", "provides 100x zoom"))
room['narrow'].items.append(
    Item("ash", "pile of ash, probably someone set a fire"))
room['treasure'].items.extend([Item("crown", "rusty looking crown"), Item(
    "dagger", "it may deliver 5000x damage only if it had better handle")])



#
# Main
#
player = Player("Mike", room['outside'])
# Make a new player object that is currently in the 'outside' room.
def roomItems():
    if len(player.current_room.items) > 0:
        print('There are some items here:\n')
        for item in player.current_room.items:
            print(f"{item.getItemName()}")


def playerInventory():
    if len(player.inventory) > 0:
        print(f"{player}'s Inventory: ")
        for item in player.inventory:
            print(f"{item.getItemName()}")


def inventory():
    while True:
        playerInventory()
        interact = input(
            "Would you like to pick up items or look at your inventory? (e.g. 'take sword' or drop sword' or 'i' to see inventory) or 'move' to move on: ")
        if interact == 'move':
            break
        elif interact == 'i':
            print('players inventory: blah blah \n')
        elif len(interact.split(' ')) > 1:
            action = interact.split(" ")[0]
            itemName = interact.split(" ")[1]

            roomItems = [item.getItemName()
                         for item in player.current_room.getRoomItems()]
            playerItems = [item.getItemName()
                           for item in player.inventory]
            if action == "get" or action == "take":
                if itemName in roomItems:
                    player.addItem(
                        player.current_room.getRoomItems()[roomItems.index(itemName)])
                    player.current_room.removeItem(player.current_room.getRoomItems()[
                                                   roomItems.index(itemName)])
                else:
                    print(f"Item you have entered '{itemName}' doesn't exist")
            elif action == "drop":
                if itemName in playerItems:
                    player.current_room.addItem(
                        player.inventory[playerItems.index(itemName)])
                    player.removeItem(
                        player.inventory[playerItems.index(itemName)])
                else:
                    print(f"Item you have entered '{itemName}' doesn't exist")
        else:
            print("\n\nPlease select the correct input\n\n")


def adventure_game():
    print("\nWelcome to the Adventure Game\n")
    print(f"\nWelcome {player}!\n")
    print(f"\n{player} is {player.current_room}\n")
    print(f"\n{player.current_room.getDesc()}\n")
    roomItems()
    while True:

        command = input(
            "\nEnter move commands --> n, e, s, w OR interact with room and your inventory with 'i' & q to quit the game: ")

        if command == ('n' or 'e' or 's' or 'w'):
            print(f"\nYou have entered {command!r}\n")
        elif command == 'i':
            inventory()
            # Do inventory management function -> interact with room or inventory
        elif command == 'q':
            print("Exiting game")
            break
        else:
            print("\n\nPlease select the correct input\n\n")

        if command == 'n':
            print("Lets go to the North Door\n")
            if player.current_room.n_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.n_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}\n")
                print(f"\n{player.current_room.getDesc()}\n")
                roomItems()

        if command == 's':
            print("Lets go to the South Door\n")
            if player.current_room.s_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.s_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")
                print(f"\n{player.current_room.getDesc()}\n")
                roomItems()
        if command == 'e':
            print("Lets go to the East Door\n")
            if player.current_room.e_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.e_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")
                print(f"\n{player.current_room.getDesc()}\n")
                roomItems()

        if command == 'w':
            print("Lets go to the West Door\n")
            if player.current_room.w_to == None:
                print(
                    f"Oops, there is no Door here, {player} will remain in {player.current_room}")
            else:
                player.current_room = player.current_room.w_to
                print("Going through the Door\n")
                print(f"{player}'s room is {player.current_room}")
                print(f"\n{player.current_room.getDesc()}\n")
                roomItems()


if __name__ == '__main__':
    adventure_game()
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