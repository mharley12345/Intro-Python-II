from room import Room
from player import Player
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

outside =  room['outside']
foyer =    room['foyer']
overlook = room['overlook']
narrow   = room['narrow']
treasure = room['treasure']


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to =  treasure
treasure.s_to = narrow

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

options = {1: 'n', 2: 's', 3: 'e', 4: 'w', 9: 'q'}
player1 = Player('player1', 'outside', 'foyer', 'null', 'null', 'null')



location = player1.location
def user_choices():
     choice = input('[1] n [2] s [3] e [4] w [9] q\n ')
     text_file = open("history.txt", "w")
     text_file.write(str(choice))
     for i in choice:
       if choice == '1' and player1.location == outside:
          player1.location = f"{foyer}" 
         
          player1.s_to = outside
          player1.e_to = narrow
          player1.n_to = overlook
          return  location == f"{foyer}"
       elif choice == '2' and player1.location == foyer:
            player1.location = outside
         
            player1.s_to = "null"
            player1.e_to ="null"
            player1.n_to = foyer
            return   location == outside
       elif choice == '3' and player1.location == foyer:
          
          
            player1.w_to = foyer  
            player1.n_to = treasure
            return   print(narrow)
       elif choice == '1' and player1.location == narrow:
            return   location == f"{narrow}"
     get_current_room()

     text_file.close()
     return options[int(choice)]
    
def get_current_room():


    
     print(outside)
      
     player1.s_to = outside
     player1.n_to = overlook
     player1.e_to = narrow
     player1.w_to = 'null'   
    
 

  
     
 
        
     
       
       
               
get_current_room()   
while user_choices != "q":
   
    get_user_choice = user_choices()


   
