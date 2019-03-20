import pygame
#import disk
from player import Player
from point import Point

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
        #self.commands = c4_commands(); #added a command queue
        self.current_player = 1
        self.available_slots = 42
        self.frame = []
        for i in range(7):
            self.frame.append([None]*7)
    
    def game_over(self, disk):
        """
        returns true when a player wins the game.
        This function checks if the player placed four 
        chips vertically, horizontally, or diagonally.
        """
        x_coord = disk.getPoint().getX()
        y_coord = disk.getPoint().getY()
        consecutive_disks = [0,0,0,0,0,0,0,0]
        
        for shift in range (1, 4, 1):
            if(self.frame[x_coord-shift][y_coord] == disk):
                consecutive_disks[0] += 1
            if(self.frame[x_coord+shift][y_coord] == disk):
                consecutive_disks[1] += 1
            if(self.frame[x_coord][y_coord-shift] == disk):
                consecutive_disks[2] += 1
            if(self.frame[x_coord][y_coord+shift] == disk):
                consecutive_disks[3] += 1
            if(self.frame[x_coord+shift][y_coord+shift] == disk):
                consecutive_disks[4] += 1
            if(self.frame[x_coord+shift][y_coord-shift] == disk):
                consecutive_disks[5] += 1
            if(self.frame[x_coord-shift][y_coord+shift] == disk):
                consecutive_disks[6] += 1
            if(self.frame[x_coord-shift][y_coord-shift] == disk):
                consecutive_disks[7] += 1
                
        if(3 in consecutive_disks):
            return True
        return False        
    
    def insert_disk(self, column):
        """
        inserts a player's disk on the frame and updates 
        it. It will require the player number and the column 
        the player chooses to place his/her disk.
        """
        if (is_filled() == False):
            for row in range (5,-1,-1):
                if self.frame[row][column] != None:
                    self.frame[row+1][column] = Disk(point(row, column), self.current_player)
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
