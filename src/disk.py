import c4model
from point import Point
from player import Player

"""
A Disk class which has a point object to reference where on the grid
the disk is placed as well as a colour attribute for the View to
display to the user. 
"""

class Disk:

    # Constructor to set the colour, point object and dropped status
        # Constructor to set the colour, point object and dropped status
    def __init__(self, point, player):
        #I removed self.color, because I don't know how each player will be choosing the color.
	if player == 1:
	    self.player = Player(1)
	else:
	    self.player = Player(2)
        self.point = point
        self.dropped = False

    def getPlayer(self):
	"""
	Returns the current player
	"""
	return self.player

    # Function to get the colour of the disk
    def getColor(self):
    	return self.color

    # Function to set the colour of the disk
    def setColor(self, color):
    	self.color = color

    def getPoint():
	return self.point

    # Function to check of disk is dropped
    def isDropped(self):
    	return self.dropped
    
    # Function to change the status of a disk when dropped
    def changeDiskStatus(self):
    	if (self.dropped is False):
    		self.dropped = True
		
    def __eq__(self, other):
	if self.player.get_player_number() == other.player.get_player_number():
	    return True
	return False
