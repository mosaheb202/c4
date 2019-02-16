import c4_model
from point import Point

"""
A Disk class which has a point object to reference where on the grid
the disk is placed as well as a colour attribute for the View to
display to the user. 
"""

class Disk:

    # Constructor to set the colour, point object and dropped status
    def __init__(self, color, point):
        self.color = color
        self.point = point
        self.dropped = False

    # Function to get the colour of the disk
    def getColor(self):
    	return self.color

    # Function to set the colour of the disk
    def setColor(self, color):
    	self.color = color

    # Function to check of disk is dropped
    def isDropped(self):
    	return self.dropped

    # Function to change the status of a disk when dropped
    def changeDiskStatus(self):
    	if (self.dropped is False):
    		self.dropped = True
    	

 