from room import Room
from player import Player
from item import Item

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons","Money"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""","nill"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""","Gold"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""","Coal"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""","Treasure"),
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





#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome to this crazy game!  Enter a name for you player...')
name = input('>>')
player = Player(name, room['outside'],None)


def current_room(player):
    print(f'{player.name} is in {player.current_room}')
    if player.current_room.items == 'no items':
        print('this room has no items')
    else:
        print(f'this room has a{player.current_room.items}')
        print(
            'What would you like to do? [GET] pick up [N] North [S] South [E] East [W] West [Q] Quit ')
        playerInput = input(">>").upper()


playerInput = ''
while playerInput != 'Q':
    current_room(player)
    print(playerInput)
    print('--------------------')
    print(player.inventory)
    print(
        'Choose your next move: [N] North [S] South [E] East [W] West [Q] Quit')
    playerInput = input(">>").upper()
    print("IM HERE")
    if playerInput == 'N' or playerInput == 'S' or playerInput == 'E' or playerInput == 'W':
        if playerInput == "N" and player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
        elif playerInput == "E" and player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
        elif playerInput == "S" and player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
        elif playerInput == "W" and player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
        else:
            print("You can't move in that direction"),
    elif playerInput == 'GET':
         player.collect(current_room.item)
         print(player.inventory,'HERER')
        
         print(f'You just picked up a {playerInput}')
    elif playerInput == "Q":
        print('You ended the game')
    
 

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