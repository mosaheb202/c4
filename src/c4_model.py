import pygame
import c4_view
import c4
import disk
from player import Player

"""
This will quite literally be the board within the connect 4 game.
The model houses all the disks.


"""
class model:
    
    def __init__(self):
        """
        intialized the framework of the game, setting 0 as a space in the frame
        without a disk
        """
        self.commands = c4_commands(); #added a command queue
        self.frame = []
        for i in range(7):
            this.frame.append([0, 0, 0, 0, 0, 0, 0])
    
    def game_over(self):
        """
        returns True if the game is one by a player.
        Should work based on the spacing of disks?
        """
        pass
    
    def insert_disk(self, player, column):
        """
        inserts a player's disk on the frame and updates 
        it. It will require the player number and the column 
        the player chooses to place his/her disk.
        """
        for i in range (5,-1,-1):
            if self.frame[i][column] == 0:
                if player.get_player_number() == 1:
                    self.frame[i][column] = 1;
                    return True
                else:
                    self.frame[i][column] = 2;
                    return True
        return False        
