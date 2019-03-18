import pygame
import c4_view
import c4
import disk
from player import Player
from point import Point

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
        self.current_player = 1
        self.available_slots = 42
        self.frame = []
        for i in range(7):
            this.frame.append([None, None, None, None, None, None, None])
    
    def game_over(self, disk):
        """
        returns true when a player wins the game.
        This function checks if the player placed four 
        chips vertically, horizontally, or diagonally.
        """
        x_coord = disk.getPoint().getX()
        y_coord = disk.getPoint().getY()

        for i in range (1, 4, 1):
            if(self.frame[x_coord-i][y_coord] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord+i][y_coord] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord][y_coord-i] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord][y_coord+i] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord+i][y_coord+i] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord+i][y_coord-i] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord-i][y_coord+i] != disk):
                return False
        for i in range (1, 4, 1):
            if(self.frame[x_coord-i][y_coord-i] != disk):
                return False
        return True        
    
    def insert_disk(self, column):
        """
        inserts a player's disk on the frame and updates 
        it. It will require the player number and the column 
        the player chooses to place his/her disk.
        """
        if (is_filled() == False):
            for row in range (5,-1,-1):
                if self.frame[row][column] == None:
                    self.frame[row][column] = Disk(point(row, column), self.current_player)
                    self.available_slots -= 1
                    turn()
                    return True
        return False 
    
    def is_filled(self):
        if self.available_slots == 0:
            return True
        return False
    
    def turn():
        self.current_player = 3 - current_player    
