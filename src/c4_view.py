import pygame
import c4_model
import c4
import disk

"""
This is the view which contains all of the visuals that the user will see. 
It has a model and the GUI (stage) that the user will see.
"""

class view:
    pygame.init()
    
    def __init__(model, stage):
        self.model = model
        create_stage(stage) 
        
    def get_model():
        return model
    
    def create_stage(stage):
        """
        All our GUI stuff that involves creating the GUI will go here.
        """
        stage = pygame.display.set_mode([1000, 800])
        #The Surface we can draw to.
        
    
        
        