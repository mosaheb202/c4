import pygame
from player import Player
from point import Point
from disk import Disk

"""
This is a model class. This class is used to update and keep track of 
the connect four game board. It contains several functions which are 
used to check if the game is over or when a player is inserting a disk.

Functions:

def game_over(self, disk):
def insert_disk(self, column):
def is_filled(self):
def turn():


"""
class Model:
    
    def __init__(self):
        """
        An init function that is used to create and update the game board object.
        """
        #self.commands = c4_commands(); #added a command queue
        self.current_player = 1
        self.available_slots = 42
        self.frame = []
        self.status = True #True if the current view represents the current model
        for i in range(7):
            self.frame.append([None]*7)
        self._column_amounts = [0]*7 #holds the value for the number of disks in each column
    
    #def count_column(self, column):
        #self._column_amounts[column] = 0
        #for i in self.frame[column]:
            #if i != None:
                #self._column_amounts[column] += 1
    
    def get_disk(self, column, row):
        """
        Return the disk at column and row inside of self.frame
        """
        return self.frame[column][row]

    def column_amount(self, column):
        """
        Return the number of disks inside of a given column
        """
        return self._column_amounts[column]
    
    def get_frame(self):
        """
        Return the frame we're using."
        """
        return self.frame
    
    def game_over(self, disk):
        """
        This function checks if the disk that is inserted caused 
        a connection of four disks. If so, this results in a win 
        for the player. It checks if there is a row of four 
        horizontally, vertically, or diagonally. It returns true 
        if there is a connection of four indicating that the game 
        is over. It returns false if there is no connection of four 
        disks.
        
        """
        x_coord = disk.getPoint().getX() # Getting x and y coordinates of the passed in disk object
        y_coord = disk.getPoint().getY()
        consecutive_disks = [0,0,0,0,0,0,0,0]
        
        for shift in range (1, 4, 1): # Checking if there is a connection of four disks horizonally, vertically, or diagonally
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
                
        if(3 in consecutive_disks): # Returns true if there four disks are connected
            return True
        return False        
    
    def insert_disk(self, column):
        """
        This function inserts a disk in the column that the 
        player has chosen. It checks if there is space in 
        the specified column and then creates a disk object in 
        that position. If there is no space in the column, it 
        will return false. If it inserts a disk object successfully, 
        it returns true.
        """
        if (self.is_filled() == False): # Checks if board is not full
            for row in range (5,-1,-1): # Loops through rows to make sure there is an empty space to create a disk object
                if self.frame[row][column] == None:
                    self.frame[row][column] = Disk(Point(row, column), self.current_player)
                    self.available_slots -= 1
                    self._column_amounts[column] += 1
                    print(self._column_amounts)
                    self.turn() # Changes turn to next player once disk is 'inserted' and tells the game to update
                    return True
        return False
    
    def is_filled(self):
        """
        This function checks if the board is full. The total available 
        slots is 42 and once it reaches 0, the board is full. It returns 
        true if the available slots is 0 and returns false otherwise.
        """
        if self.available_slots == 0: # Checks if available_slots variable is 0
            return True
        return False
    
    def update(self):
        """
        update self.status
        
        NOTE: self.status is used to tell the view whether it is behind the model,
        or if it is up to date
        """
        if self.update == False:
            return True
        else:
            return False
    
    def turn(self):
        """
        This function switches the turn of the two players 
        playing the game.
        """
        self.status = False
        self.current_player = 3 - self.current_player
