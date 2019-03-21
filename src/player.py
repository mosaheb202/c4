import c4model
from point import Point

"""
A Player class contains the information about the player. The information
about the player include the player's number and the colour of disk.
"""

class Player:

    def __init__(self, number, color_disk):
        self.number = number
        self.color = color_disk
        self.numDisks = num_disks 
    
    def get_player_number(self):
        """
        Returns the player number
        """
        return self.number
    
    def set_player_number(self, number):
        """
        Sets the player number
        """
        self.number = number
        
    def get_color_disk(self):
        """
        Returns the disk colour
        """
        return self.color
    
    def set_color_disk(self, color_disk):
        """
        Sets the disk colour
        """
        self.color = color_disk
    
    
