import pygame
import disk
from player import Player

"""
This will quite literally be the board within the connect 4 game.
The model houses all the disks.


"""
class Model:
    
    def __init__(self):
        """
        intialized the framework of the game, setting 0 as a space in the frame
        without a disk
        """
        self.commands = c4_commands(); #added a command queue
        self.frame = []
        for i in range(7):
            this.frame.append([0, 0, 0, 0, 0, 0, 0])
    
    def game_over(self, player):
        """
        returns true when a player wins the game.
        This function checks if the player placed four 
        chips vertically, horizontally, or diagonally.
        """
        for height_idx in range (5,-1,-1):
            for position in range(4):
                if [player.get_player_number()]*4 == self.frame[height_idx][position:position+4]:
                    return True
        for length_idx in range (0,7,1):
            for position in range (4):
                if (player.get_player_number() == self.frame[position][length_idx] == self.frame[position+1][length_idx] == 
                    self.frame[position+2][length_idx] == self.frame[position+3][length_idx]):
                    return True
        for position in range (3):
            for height_idx in range(0,4,1):
                if (player.get_player_number() == self.frame[position][height_idx] == self.frame[position+1][height_idx+1] == 
                    self.frame[position+2][height_idx+2] == self.frame[position+3][height_idx+3]):
                    return True
        for position in range (3):
            for length_idx in range(3,7,1):
                if (player.get_player_number() == self.frame[position][length_idx] == self.frame[position+1][length_idx-1] == 
                    self.frame[position+2][length_idx-2] == self.frame[position+3][length_idx-3]):
                    return True
        return False        
    
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