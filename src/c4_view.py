import pygame
#import c4_model
#import c4
#import disk

"""
This is the view which contains all of the visuals that the user will see. 
It has a model and the GUI (stage) that the user will see.
"""
#Define constants
SIZE = 100
WIDTH = SIZE * 6
HEIGHT = SIZE* 7 + SIZE

class View:
    
    def __init__(self):
        #self.model = model
        pygame.init()
        create_stage()
        
    def get_model():
        return model
    
    def create_stage():
        """
        All our GUI stuff that involves creating the GUI will go here.
        """
        stage = pygame.display.set_mode([600, 800])
                
    
        
        
