from point import Point

#Define Color Constants
BLUE = (0,0,200)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)
LIGHT_RED = (245, 0, 0)
LIGHT_GREEN = (0, 245, 0)
LIGHT_BLUE = (0, 0, 245)
WHITE = (255,255,255)

"""
A Player class contains the information about the player. The information
about the player include the player's number and the colour of disk.
"""

class Player:

    def __init__(self, number):
        self.number = number
        if number == 1:
            self.color = GREEN
        else:
            self.color = RED
    
    def get_player_number(self):
        """
        Returns the player number
        """
        return self.number
    
    #def set_player_number(self, number):
        #self.number = number
        
    def get_color(self):
        return self.color
    
    #def set_color_disk(self, color_disk):
        #self.color = color_disk
    
    
