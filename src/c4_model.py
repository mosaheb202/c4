import pygame
import c4_view
import c4
import disk

"""
This will quite literally be the board within the connect 4 game.
The model houses all the disks.


"""
class model:
    
    def __init__():
        """
        intialized the framework of the game, setting 0 as a space in the frame
        without a disk
        """
        this.commands = c4_commands(); #added a command queue
        this.frame = []
        for i in range(7):
            this.frame.append([0, 0, 0, 0, 0, 0, 0])
    
    def game_over():
        """
        returns True if the game is one by a player.
        Should work based on the spacing of disks?
        """
        pass
    
    def insert_disk():
        """
        inserts the given disk into the frame
        disk object should be a argument for this method
        """
        pass
