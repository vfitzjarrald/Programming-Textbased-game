import sys
from datetime import datetime


DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'

SCREEN_WIDTH = 80

now = datetime.now()




if now.minute == (30 or 31 or 32 or 33 or 34 or 35):
	worldRooms = {
    '?': {
	    
        DESC: 'Your home room is MS 302, it is creepy, your teacher is sleeping. You want to escape.',
			  NORTH: 'Studio',
			  GROUND: ['Sock', 'README Note']},
        
		'? ': {
	    
        DESC: 'The studio is the passage way to almost every room in the building. Your friend calls you "try to go to an e..........?" Your cell phone turns off...... ',
			  NORTH: 'PAC',
		  	EAST: 'SC Room',
		  	SOUTH: 'Home Room',
			  WEST: 'Girls Toilet',
			  GROUND: ['MacBook', 'Audio Recorder']},
        
		'?  ': {
	    
		  	DESC: 'The PAC... You see actors... They are practicing...',
		  	SOUTH: 'Studio',
		  	WEST: 'Deli',
		  	EAST: 'GYM',
			  GROUND: ['Paper Clip']},
        
		'?   ': {
	    
		  	DESC: 'The delightful smell of junk fills the air, making you hungry. You drool... The baker has a knife in his hand, he drops it',
		  	EAST: 'PAC',
		  	SHOP: ['Brownie', 'Hot Dog', 'Pizza'],
			  GROUND: ['Shop Howto', 'Knife']},
        
		'?    ': {
	    
		  	DESC: 'The student government of the school.. You think they are mean and selfish. Screw them!',
		  	NORTH: 'GYM',
		   	WEST: 'Studio',
		  	EAST: 'Boys Toilet',
		  	GROUND: ['Paper', 'Pencil', 'Sign']},
        
		'?     ': {
	    
			  DESC: 'Your phone rings, you have a message. "YOU ARE ALMOST THERE BUT BEWARE I AM GOING TO GET YOU!!" You start to hurry.',
			  NORTH: 'Elevator',
			  SOUTH: 'SC Room',
		  	GROUND: ['Key', 'Soccer Ball']},
        
		'?      ': {
	    
			  DESC: 'There is a sign "t_iselev_t_r_etsyo_outoft_esc_ool" It seems like some words got erased. You see another sign. "You need a key to escape".....',
			  DOWN: 'Outside',
			  UP: '2nd Floor Lobby',
			  SOUTH: 'GYM',
			  GROUND: []},
        
		'?       ': {
	    
        DESC: 'You are out of the school, but still inside the gate. You are still not done...',
			  SOUTH: 'Elevator',
			  NORTH: 'Front Gate',
			  GROUND: []},
        
		'?        ': {
	    
        DESC: 'YOU MADE IT TO THE FRONT, YOU ARE RUNNING!!!.........YOU GET CAUGHT',
        NORTH: 'Home Room',
        GROUND: []},
        
		'?         ': {
	    
	    	DESC: 'YOU WALK IN TO A ROOM.... YOUR EYESIGHT GETS BLURRY....YOU DIE...',
	    	NORTH: 'Home Room',
	    	GROUND: []},
	    
		'?          ': {
	    
	     	DESC: 'You are on the 2nd floor',
	    	NORTH: 'Art Room',
	     	SOUTH: 'Elevator',
	    	EAST: 'Library',
	    	GROUND: []},
	    
		'?           ': {
		
	  		DESC: 'The brightest place at the school...Disgusting...',
	  		NORTH: 'Computer Room',
	  		SOUTH: '2nd Floor Lobby',
		  	GROUND: ['Paint Brush']},
		
		'?            ': {
		
	  		DESC: 'You can hear a video playing inside.',
		  	WEST: 'Girls Toilet',
		  	SOUTH: 'Art Room',
		  	EAST: 'CCT',
		  	GROUND: ['Charger']},
		
		'?             ': {
		
		  	DESC: 'The main "MANAGER" of the school. They are lazy...',
		  	WEST: 'Computer Room',
			  SOUTH: 'Office',
		  	NORTH: 'Boys Toilet',
			  GROUND: ['SD CARD']},
		
		'?              ': {
		
			  DESC: 'You can hear the people typing away on there computers.',
			  NORTH: 'CCT',
			  EAST: 'Pool',
			  SOUTH: 'Spanish',
			  GROUND: ['Coins']},
		
        
		'?               ': {
	    
	    	DESC: 'The place where there used to be water.',
	    	WEST: 'Office',
	    	EAST: 'Locker Room',
	    	NORTH: 'Girls Toilet',
	    	GROUND: ['Goggles']},
		
		'?                ': {
	    
	    	DESC: 'SMELLS LIKE SWEAT',
	    	WEST: 'Pool',
	    	NORTH: 'Boys Toilet',
	    	GROUND: []},
	    
		'?                 ': {
		
			  DESC: 'THE PLACE EVERYONE HATES',
			  NORTH: 'Office',
			  SOUTH: 'Library',
			  GROUND: []},
		
		'?                  ': {
	    
    		DESC: 'THE BOOKS OF "KNOWLEDGE" SIT THERE UNTOUCHED.',
    		NORTH: 'Spanish',
    		SOUTH: 'Girls Toilet',
    		WEST: 'Lobby',
    		EAST: 'Hallway',
    		GROUND: ['BOOK']},
    	
		'?                   ': {
	    
    		DESC: 'A Long and spooky hallway stands before you',
    		NORTH: 'Girls Toilet',
    		SOUTH: 'Boys Toilet',
    		EAST: 'Chinese Room',
    		WEST: 'Library',
    		GROUND: []},
    	
		'?                    ': {
	    
	    	DESC: "YOU OPEN OUT THER DOOR YOU ESCAPED!!!",
	    	WEST: 'Girls Toilet',
    		SOUTH: 'Boys Toilet',
    		NORTH: 'Hallway',
    		EAST: 'Door',
    		GROUND: []},	
    	
		'?                     ': {
	    
	      DESC: "YOU OPEN OUT THER DOOR YOU ESCAPED!!!",
			  GROUND: []},
    
		'?                      ': {
	    
	      DESC: 'HOW DARE YOU!!!',
	      NORTH: 'Home Room',
    	  GROUND: []},
		}
else:
	worldRooms = {
    'Home Room': {
	    
        DESC: 'Your home room is MS 302, it is creepy, your teacher is sleeping. You want to escape.',
			  NORTH: 'Studio',
		    GROUND: ['Sock', 'README Note']},
        
		'Studio': {
	    
        DESC: 'The studio is the passage way to almost every room in the building. Your friend calls you "try to go to an e..........?" Your cell phone turns off...... ',
			  NORTH: 'PAC',
			  EAST: 'SC Room',
			  SOUTH: 'Home Room',
			  WEST: 'Girls Toilet',
			  GROUND: ['MacBook', 'Audio Recorder']},
        
		'PAC': {
	    
			DESC: 'The PAC... You see actors... They are practicing...',
			SOUTH: 'Studio',
			WEST: 'Deli',
			EAST: 'GYM',
			GROUND: ['Paper Clip']},
        
		'Deli': {
	    
			DESC: 'The delightful smell of junk fills the air, making you hungry. You drool... The baker has a knife in his hand, he drops it',
			EAST: 'PAC',
			SHOP: ['Brownie', 'Hot Dog', 'Pizza'],
			GROUND: ['Shop Howto', 'Knife']},
        
		'SC Room': {
	    
			DESC: 'The student government of the school.. You think they are mean and selfish. Screw them!',
			NORTH: 'GYM',
			WEST: 'Studio',
			EAST: 'Boys Toilet',
			GROUND: ['Paper', 'Pencil', 'Sign']},
        
		'GYM': {
	    
			DESC: 'Your phone rings, you have a message. "YOU ARE ALMOST THERE BUT BEWARE I AM GOING TO GET YOU!!" You start to hurry.',
			NORTH: 'Elevator',
			SOUTH: 'SC Room',
			GROUND: ['Key', 'Soccer Ball']},
        
		'Elevator': {
	    
			DESC: 'There is a sign "t_iselev_t_r_etsyo_outoft_esc_ool" It seems like some words got erased. You see another sign. "You need a key to escape".....',
			DOWN: 'Outside',
			UP: '2nd Floor Lobby',
			SOUTH: 'GYM',
			GROUND: []},
        
		'Outside': {
	    
        	DESC: 'You are out of the school, but still inside the gate. You are still not done...',
			SOUTH: 'Elevator',
			NORTH: 'Front Gate',
			GROUND: []},
        
		'Front Gate': {
	    
        	DESC: 'YOU MADE IT TO THE FRONT, YOU ARE RUNNING!!!.........YOU GET CAUGHT',
        	NORTH: 'Home Room',
        	GROUND: []},
        
		'Boys Toilet': {
	    
	    	DESC: 'YOU WALK IN TO A ROOM.... YOUR EYESIGHT GETS BLURRY....YOU DIE...',
	    	NORTH: 'Home Room',
	    	GROUND: []},
	    
		'2nd Floor Lobby': {
	    
	    	DESC: 'You are on the 2nd floor',
	    	NORTH: 'Art Room',
	    	SOUTH: 'Elevator',
	    	EAST: 'Library',
	    	GROUND: []},
	    
		'Art Room': {
		
			DESC: 'The brightest place at the school...Disgusting...',
			NORTH: 'Computer Room',
			SOUTH: '2nd Floor Lobby',
			GROUND: ['Paint Brush']},
		
		'Computer Room': {
		
			DESC: 'You can hear a video playing inside.',
			WEST: 'Girls Toilet',
			SOUTH: 'Art Room',
			EAST: 'CCT',
			GROUND: ['Charger']},
		
		'CCT': {
		
			DESC: 'The main "MANAGER" of the school. They are lazy...',
			WEST: 'Computer Room',
			SOUTH: 'Office',
			NORTH: 'Boys Toilet',
			GROUND: ['SD CARD']},
		
		'Office': {
		
			DESC: 'You can hear the people typing away on there computers.',
			NORTH: 'CCT',
			EAST: 'Pool',
			SOUTH: 'Spanish',
			GROUND: ['Coins']},
		
        
		'Pool': {
	    
	    	DESC: 'The place where there used to be water.',
	    	WEST: 'Office',
	    	EAST: 'Locker Room',
	    	NORTH: 'Girls Toilet',
	    	GROUND: ['Goggles']},
		
		'Locker Room': {
	    
	    	DESC: 'SMELLS LIKE SWEAT',
	    	WEST: 'Pool',
	    	NORTH: 'Boys Toilet',
	    	GROUND: []},
	    
		'Spanish': {
		
			DESC: 'THE PLACE EVERYONE HATES',
			NORTH: 'Office',
			SOUTH: 'Library',
			GROUND: []},
		
		'Library': {
	    
    		DESC: 'THE BOOKS OF "KNOWLEDGE" SIT THERE UNTOUCHED.',
    		NORTH: 'Spanish',
    		SOUTH: 'Girls Toilet',
    		WEST: 'Lobby',
    		EAST: 'Hallway',
    		GROUND: ['BOOK']},
    	
		'Hallway': {
	    
    		DESC: 'A Long and spooky hallway stands before you',
    		NORTH: 'Girls Toilet',
    		SOUTH: 'Boys Toilet',
    		EAST: 'Chinese Room',
    		WEST: 'Library',
    		GROUND: []},
    	
		'Chinese Room': {
	    
	    	DESC: "YOU OPEN OUT THER DOOR YOU ESCAPED!!!",
	    	WEST: 'Girls Toilet',
    		SOUTH: 'Boys Toilet',
    		NORTH: 'Hallway',
    		EAST: 'Door',
    		GROUND: []},	
    	
		'Door': {
	    
	    	DESC: "YOU OPEN OUT THER DOOR YOU ESCAPED!!!",
			GROUND: []},
    
		'Girls Toilet': {
	    
	    	DESC: 'HOW DARE YOU!!!',
	    	NORTH: 'Home Room',
    		GROUND: []},
		}
    
    




worldItems = {
    'Key': {
        GROUNDDESC: 'An important Key',
        SHORTDESC: 'A Key',
        LONGDESC: 'The Key seem to be very important. I has a lot of dust on it',
        TAKEABLE: True,
        DESCWORDS: ['key', 'important']},
    'Sock': {
        GROUNDDESC: 'A Smelly sock lays on the ground',
        SHORTDESC: 'a sock',
        LONGDESC: 'A Smelly sock lays on the ground.. It looks like yours."',
        TAKEABLE: True,
        DESCWORDS: ['sock']},
    'Paper Clip': {
        GROUNDDESC: 'A silvery clip. Might come in handy',
        SHORTDESC: 'A clip',
        LONGDESC: 'A silvery clip. Might come in handy... Maybe as a.....key?',
        TAKEABLE: True,
        DESCWORDS: ['clip']},
    'Pencil': {
        GROUNDDESC: 'A pencil lies on the ground.',
        SHORTDESC: 'a pencil',
        LONGDESC: 'A pencil, engraved with the word, "DANNY"',
        TAKEABLE: True,
        DESCWORDS: ['pencil']},
    'Paper': {
        GROUNDDESC: 'A piece of paper lying on the ground',
        SHORTDESC: 'A piece of paper',
        LONGDESC: 'A piece of paper lying on the ground. Does not really seem useful.',
        TAKEABLE: True,
        DESCWORDS: ['paper', 'piece']},
    'Knife': {
        GROUNDDESC: 'The knife that the baker dropped is on the ground.',
        SHORTDESC: 'The knife',
        LONGDESC: 'The knife that the baker dropped is on the ground (Maybe on purpose). Engraved on the front: "You\'re Stupid and FAT!" You ignore it.',
        TAKEABLE: True,
        DESCWORDS: ['knife', 'baker', 'stupid']},
    'Sign': {
        GROUNDDESC: 'On the sign: "WORK IN PROGRESS',
        SHORTDESC: 'a sign',
        LONGDESC: 'On the sign: "WORK IN PROGRESS... It sound like a lie...',
        TAKEABLE: False,
        DESCWORDS: ['sign']},
    'Audio Recorder': {
        GROUNDDESC: 'An Audio Recorder lies on the ground.',
        SHORTDESC: 'An Audio Recorder',
        LONGDESC: 'An Audio Recorder lies on the ground... Maybe it had a clue?? You play it "Find a door"',
        TAKEABLE: True,
        DESCWORDS: ['audio', 'recorder', 'clue']},
    'MacBook': {
        GROUNDDESC: 'Everyones favorite device.. A MacBook is on the ground. Your hand want to touch it.',
        SHORTDESC: 'A MacBook',
        LONGDESC: 'The battery is dead but you still have hope you are eager to get out of this place.',
        TAKEABLE: True,
        DESCWORDS: ['macbook', 'dead', 'hope', 'device']},
    'Hot Dog': {
        GROUNDDESC: 'A suspicious Hot dog rests on the ground.',
        SHORTDESC: 'a Hot dog',
        LONGDESC: 'A Hot dog. It tastes like a normal hot dog.',
        EDIBLE: True,
        DESCWORDS: ['hot', 'dog']},
    'Pizza': {
        GROUNDDESC: 'A pizza rests on the ground. (Gross.)',
        SHORTDESC: 'a pizza',
        LONGDESC: 'It is a pizza. Looks like someone dropped it.',
        EDIBLE: True,
        DESCWORDS: ['pizza']},
    'Brownie': {
        GROUNDDESC: 'A Brownie rests on the ground. (Gross.)',
        SHORTDESC: 'a brownie',
        LONGDESC: 'It is a chocolate brownie.',
        EDIBLE: True,
        DESCWORDS: ['brownie']},
    'Charger': {
        GROUNDDESC: 'A Charger rests on the bleachers',
        SHORTDESC: 'a charger',
        LONGDESC: 'YOU FOUND THE CHARGER.. YOU ARE EXCITED... YOU TURN THE COMPUTER ON YOU SEE A VIDEO MESSAGE. "You have to get out of there till 12!!!!!! OR ELSE!!!!"',
        TAKEABLE: True,
        DESCWORDS: ['charger']},
    'Soccer Ball': {
        GROUNDDESC: 'A soccer ball lies on the ground',
        SHORTDESC: 'a soccer ball',
        LONGDESC: 'The soccer ball does not look useful, You kick it around.',
        DESCWORDS: ['soccer', 'ball']},
    'Paint Brush': {
        GROUNDDESC: 'A Paint Brush lies on the ground',
        SHORTDESC: 'a Paint Brush',
        LONGDESC: 'The Paint Brush does not look useful.',
        TAKEABLE: True,
        DESCWORDS: ['paint', 'brush']},
    'SD CARD': {
        GROUNDDESC: 'A SD CARD lies on the ground',
        SHORTDESC: 'a SD CARD',
        LONGDESC: 'The SD CARD might have something in it. You are closer to the end.',
        TAKEABLE: True,
        DESCWORDS: ['SD', 'CARD']},
        
    'Coins': {
        GROUNDDESC: 'A coin is shinning on the ground',
        SHORTDESC: 'Coins',
        LONGDESC: 'Maybe You can get something with the money you just picked up',
        TAKEABLE: True,
        DESCWORDS: ['coin', 'money']},
        
    'Goggles': {
        GROUNDDESC: 'A Goggle',
        SHORTDESC: 'A Goggle',
        LONGDESC: 'A GOGGLE? DEFIANTLY NOT NEEDED.',
        TAKEABLE: True,
        DESCWORDS: ['goggle']},
        
    'BOOK': {
        GROUNDDESC: 'A Book is laying on the ground',
        SHORTDESC: 'A Book',
        LONGDESC: 'The book seem to be very important. I has a lot of dust on it.... You open it "YOU ARE ALMOST THERE"',
        TAKEABLE: False,
        DESCWORDS: ['book', 'important']},


        
    'README Note': {
        GROUNDDESC: 'A note titled "README" rests on the ground.',
        SHORTDESC: 'a README note',
        LONGDESC: 'The README note reads, "Welcome to the text adventure demo. Be sure to check out the source code to see how this game is put together."',
        EDIBLE: True,
        DESCWORDS: ['readme', 'note']},
        
    'Shop Howto': {
        GROUNDDESC: 'A "Shopping HOWTO" note rests on the ground.',
        SHORTDESC: 'a shopping howto',
        LONGDESC: 'The note reads, "When you are at a shop, you can type "list" to show what is for sale. "buy <item>" will add it to your inventory, or you can sell an item in your inventory with "sell <item>". (Currently, money is not implemented in this program.)',
        EDIBLE: True,
        DESCWORDS: ['howto', 'note', 'shop']},
    }
    




"""
These variables track where the player is and what is in their inventory.
The value in the location variable will always be a key in the world variable
and the value in the inventory list will always be a key in the worldItems
variable.
"""
location = 'Home Room' # start in town square
inventory = ['README Note', 'Sock', 'Pizza'] # start with blank inventory
showFullExits = True

import cmd, textwrap

def displayLocation(loc):
    """A helper function for displaying an area's description and exits."""
    # Print the room name.
    print(loc)
    print('=' * len(loc))

    # Print the room's description (using textwrap.wrap())
    print('\n'.join(textwrap.wrap(worldRooms[loc][DESC], SCREEN_WIDTH)))

    # Print all the items on the ground.
    if len(worldRooms[loc][GROUND]) > 0:
        print()
        for item in worldRooms[loc][GROUND]:
            print(worldItems[item][GROUNDDESC])

    # Print all the exits.
    exits = []
    for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
        if direction in worldRooms[loc].keys():
            exits.append(direction.title())
    print()
    if showFullExits:
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction in worldRooms[location]:
                print('%s: %s' % (direction.title(), worldRooms[location][direction]))
    else:
        print('Exits: %s' % ' '.join(exits))


def moveDirection(direction):
    """A helper function that changes the location of the player."""
    global location

    if direction in worldRooms[location]:
        print('You move to the %s.' % direction)
        location = worldRooms[location][direction]
        displayLocation(location)
    else:
        print('You cannot move in that direction')


def getAllDescWords(itemList):
    """Returns a list of "description words" for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.extend(worldItems[item][DESCWORDS])
    return list(set(descWords))

def getAllFirstDescWords(itemList):
    """Returns a list of the first "description word" in the list of
    description words for each item named in itemList."""
    itemList = list(set(itemList)) # make itemList unique
    descWords = []
    for item in itemList:
        descWords.append(worldItems[item][DESCWORDS][0])
    return list(set(descWords))

def getFirstItemMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            return item
    return None

def getAllItemsMatchingDesc(desc, itemList):
    itemList = list(set(itemList)) # make itemList unique
    matchingItems = []
    for item in itemList:
        if desc in worldItems[item][DESCWORDS]:
            matchingItems.append(item)
    return matchingItems

class TextAdventureCmd(cmd.Cmd):
    prompt = '\n> '

    # The default() method is called when none of the other do_*() command methods match.
    def default(self, arg):
        print('I do not understand that command. Type "help" for a list of commands.')

    # A very simple "quit" command to terminate the program:
    def do_quit(self, arg):
        """Quit the game."""
        return True # this exits the Cmd application loop in TextAdventureCmd.cmdloop()

    def help_combat(self):
        print('Combat is not implemented in this program.')


    # These direction commands have a long (i.e. north) and show (i.e. n) form.
    # Since the code is basically the same, I put it in the moveDirection()
    # function.
    def do_north(self, arg):
        """Go to the area to the north, if possible."""
        moveDirection('north')

    def do_south(self, arg):
        """Go to the area to the south, if possible."""
        moveDirection('south')

    def do_east(self, arg):
        """Go to the area to the east, if possible."""
        moveDirection('east')

    def do_west(self, arg):
        """Go to the area to the west, if possible."""
        moveDirection('west')

    def do_up(self, arg):
        """Go to the area upwards, if possible."""
        moveDirection('up')

    def do_down(self, arg):
        """Go to the area downwards, if possible."""
        moveDirection('down')

    # Since the code is the exact same, we can just copy the
    # methods with shortened names:
    do_n = do_north
    do_s = do_south
    do_e = do_east
    do_w = do_west
    do_u = do_up
    do_d = do_down

    def do_exits(self, arg):
        """Toggle showing full exit descriptions or brief exit descriptions."""
        global showFullExits
        showFullExits = not showFullExits
        if showFullExits:
            print('Showing full exit descriptions.')
        else:
            print('Showing brief exit descriptions.')

    def do_inventory(self, arg):
        """Display a list of the items in your possession."""

        if len(inventory) == 0:
            print('Inventory:\n  (nothing)')
            return

        # first get a count of each distinct item in the inventory
        itemCount = {}
        for item in inventory:
            if item in itemCount.keys():
                itemCount[item] += 1
            else:
                itemCount[item] = 1

        # get a list of inventory items with duplicates removed:
        print('Inventory:')
        for item in set(inventory):
            if itemCount[item] > 1:
                print('  %s (%s)' % (item, itemCount[item]))
            else:
                print('  ' + item)

    do_inv = do_inventory


    def do_take(self, arg):
        """"take <item> - Take an item on the ground."""

        # put this value in a more suitably named variable
        itemToTake = arg.lower()

        if itemToTake == '':
            print('Take what? Type "look" the items on the ground here.')
            return

        cantTake = False

        # get the item name that the player's command describes
        for item in getAllItemsMatchingDesc(itemToTake, worldRooms[location][GROUND]):
            if worldItems[item].get(TAKEABLE, True) == False:
                cantTake = True
                continue # there may be other items named this that you can take, so we continue checking
            print('You take %s.' % (worldItems[item][SHORTDESC]))
            worldRooms[location][GROUND].remove(item) # remove from the ground
            inventory.append(item) # add to inventory
            return

        if cantTake:
            print('You cannot take "%s".' % (itemToTake))
        else:
            print('That is not on the ground.')


    def do_drop(self, arg):
        """"drop <item> - Drop an item from your inventory onto the ground."""

        # put this value in a more suitably named variable
        itemToDrop = arg.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        # find out if the player doesn't have that item
        if itemToDrop not in invDescWords:
            print('You do not have "%s" in your inventory.' % (itemToDrop))
            return

        # get the item name that the player's command describes
        item = getFirstItemMatchingDesc(itemToDrop, inventory)
        if item != None:
            print('You drop %s.' % (worldItems[item][SHORTDESC]))
            inventory.remove(item) # remove from inventory
            worldRooms[location][GROUND].append(item) # add to the ground


    def complete_take(self, text, line, begidx, endidx):
        possibleItems = []
        text = text.lower()

        # if the user has only typed "take" but no item name:
        if not text:
            return getAllFirstDescWords(worldRooms[location][GROUND])

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for item in list(set(worldRooms[location][GROUND])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(TAKEABLE, True):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def complete_drop(self, text, line, begidx, endidx):
        possibleItems = []
        itemToDrop = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)

        for descWord in invDescWords:
            if line.startswith('drop %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "drop" but no item name:
        if itemToDrop == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(text):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_look(self, arg):
        """Look at an item, direction, or the area:
"look" - display the current area's description
"look <direction>" - display the description of the area in that direction
"look exits" - display the description of all adjacent areas
"look <item>" - display the description of an item on the ground or in your inventory"""

        lookingAt = arg.lower()
        if lookingAt == '':
            # "look" will re-print the area description
            displayLocation(location)
            return

        if lookingAt == 'exits':
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    print('%s: %s' % (direction.title(), worldRooms[location][direction]))
            return

        if lookingAt in ('north', 'west', 'east', 'south', 'up', 'down', 'n', 'w', 'e', 's', 'u', 'd'):
            if lookingAt.startswith('n') and NORTH in worldRooms[location]:
                print(worldRooms[location][NORTH])
            elif lookingAt.startswith('w') and WEST in worldRooms[location]:
                print(worldRooms[location][WEST])
            elif lookingAt.startswith('e') and EAST in worldRooms[location]:
                print(worldRooms[location][EAST])
            elif lookingAt.startswith('s') and SOUTH in worldRooms[location]:
                print(worldRooms[location][SOUTH])
            elif lookingAt.startswith('u') and UP in worldRooms[location]:
                print(worldRooms[location][UP])
            elif lookingAt.startswith('d') and DOWN in worldRooms[location]:
                print(worldRooms[location][DOWN])
            else:
                print('There is nothing in that direction.')
            return
    


        # see if the item being looked at is on the ground at this location
        item = getFirstItemMatchingDesc(lookingAt, worldRooms[location][GROUND])
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        # see if the item being looked at is in the inventory
        item = getFirstItemMatchingDesc(lookingAt, inventory)
        if item != None:
            print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))
            return

        print('You do not see that nearby.')


    def complete_look(self, text, line, begidx, endidx):
        possibleItems = []
        lookingAt = text.lower()

        # get a list of all "description words" for each item in the inventory
        invDescWords = getAllDescWords(inventory)
        groundDescWords = getAllDescWords(worldRooms[location][GROUND])
        shopDescWords = getAllDescWords(worldRooms[location].get(SHOP, []))

        for descWord in invDescWords + groundDescWords + shopDescWords + [NORTH, SOUTH, EAST, WEST, UP, DOWN]:
            if line.startswith('look %s' % (descWord)):
                return [] # command is complete

        # if the user has only typed "look" but no item name, show all items on ground, shop and directions:
        if lookingAt == '':
            possibleItems.extend(getAllFirstDescWords(worldRooms[location][GROUND]))
            possibleItems.extend(getAllFirstDescWords(worldRooms[location].get(SHOP, [])))
            for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
                if direction in worldRooms[location]:
                    possibleItems.append(direction)
            return list(set(possibleItems)) # make list unique

        # otherwise, get a list of all "description words" for ground items matching the command text so far:
        for descWord in groundDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # otherwise, get a list of all "description words" for items for sale at the shop (if this is one):
        for descWord in shopDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        # check for matching directions
        for direction in (NORTH, SOUTH, EAST, WEST, UP, DOWN):
            if direction.startswith(lookingAt):
                possibleItems.append(direction)

        # get a list of all "description words" for inventory items matching the command text so far:
        for descWord in invDescWords:
            if descWord.startswith(lookingAt):
                possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_list(self, arg):
        """List the items for sale at the current location's shop. "list full" will show details of the items."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        arg = arg.lower()

        print('For sale:')
        for item in worldRooms[location][SHOP]:
            print('  - %s' % (item))
            if arg == 'full':
                print('\n'.join(textwrap.wrap(worldItems[item][LONGDESC], SCREEN_WIDTH)))


    def do_buy(self, arg):
        """"buy <item>" - buy an item at the current location's shop."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        itemToBuy = arg.lower()

        if itemToBuy == '':
            print('Buy what? Type "list" or "list full" to see a list of items for sale.')
            return

        item = getFirstItemMatchingDesc(itemToBuy, worldRooms[location][SHOP])
        if item != None:
            # NOTE - If you wanted to implement money, here is where you would add
            # code that checks if the player has enough, then deducts the price
            # from their money.
            print('You have purchased %s' % (worldItems[item][SHORTDESC]))
            inventory.append(item)
            return

        print('"%s" is not sold here. Type "list" or "list full" to see a list of items for sale.' % (itemToBuy))


    def complete_buy(self, text, line, begidx, endidx):
        if SHOP not in worldRooms[location]:
            return []

        itemToBuy = text.lower()
        possibleItems = []

        # if the user has only typed "buy" but no item name:
        if not itemToBuy:
            return getAllFirstDescWords(worldRooms[location][SHOP])

        # otherwise, get a list of all "description words" for shop items matching the command text so far:
        for item in list(set(worldRooms[location][SHOP])):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_sell(self, arg):
        """"sell <item>" - sell an item at the current location's shop."""
        if SHOP not in worldRooms[location]:
            print('This is not a shop.')
            return

        itemToSell = arg.lower()

        if itemToSell == '':
            print('Sell what? Type "inventory" or "inv" to see your inventory.')
            return

        for item in inventory:
            if itemToSell in worldItems[item][DESCWORDS]:
                # NOTE - If you wanted to implement money, here is where you would add
                # code that gives the player money for selling the item.
                print('You have sold %s' % (worldItems[item][SHORTDESC]))
                inventory.remove(item)
                return

        print('You do not have "%s". Type "inventory" or "inv" to see your inventory.' % (itemToSell))


    def complete_sell(self, text, line, begidx, endidx):
        if SHOP not in worldRooms[location]:
            return []

        itemToSell = text.lower()
        possibleItems = []

        # if the user has only typed "sell" but no item name:
        if not itemToSell:
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for inventory items matching the command text so far:
        for item in list(set(inventory)):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


    def do_eat(self, arg):
        """"eat <item>" - eat an item in your inventory."""
        itemToEat = arg.lower()

        if itemToEat == '':
            print('Eat what? Type "inventory" or "inv" to see your inventory.')
            return

        cantEat = False

        for item in getAllItemsMatchingDesc(itemToEat, inventory):
            if worldItems[item].get(EDIBLE, False) == False:
                cantEat = True
                continue # there may be other items named this that you can eat, so we continue checking
            # NOTE - If you wanted to implement hunger levels, here is where
            # you would add code that changes the player's hunger level.
            print('You eat %s' % (worldItems[item][SHORTDESC]))
            inventory.remove(item)
            return

        if cantEat:
            print('You cannot eat that.')
        else:
            print('You do not have "%s". Type "inventory" or "inv" to see your inventory.' % (itemToEat))


    def complete_eat(self, text, line, begidx, endidx):
        itemToEat = text.lower()
        possibleItems = []

        # if the user has only typed "eat" but no item name:
        if itemToEat == '':
            return getAllFirstDescWords(inventory)

        # otherwise, get a list of all "description words" for edible inventory items matching the command text so far:
        for item in list(set(inventory)):
            for descWord in worldItems[item][DESCWORDS]:
                if descWord.startswith(text) and worldItems[item].get(EDIBLE, False):
                    possibleItems.append(descWord)

        return list(set(possibleItems)) # make list unique


if __name__ == '__main__':
    print('Text Adventure Demo!')
    print('====================')
    print()
    print('(Type "help" for commands.)')
    print()
    displayLocation(location)
    TextAdventureCmd().cmdloop()
    print('Thanks for playing!')


