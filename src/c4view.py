import pygame
import c4model
#import c4
#import disk

"""
This is the view which contains all of the visuals that the user will see. 
It has a model and the GUI (stage) that the user will see.
"""
#Define Dimension constants
SIZE = 100
NUMB_COLUMNS = 7
NUMB_ROWS = 6
WIDTH = SIZE * NUMB_COLUMNS
HEIGHT = (SIZE * NUMB_ROWS) + SIZE
RADIUS = (SIZE//2-10)

#Define Color Constants
BLUE = (0,0,255)
BLACK = (0,0,0)

class View:
    
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.stage = self.create_stage()
        
                
    def get_model():
        return model

    def draw_stage(self, stage):
        for col in range(NUMB_COLUMNS):
            for row in range(NUMB_ROWS):
                pygame.draw.rect(stage, BLUE, [col*SIZE, row*SIZE + SIZE, SIZE, SIZE])
                pygame.draw.circle(stage, BLACK, (col*SIZE+SIZE//2, row*SIZE + 3*SIZE//2), RADIUS)   
        pygame.display.update()

                
    def create_stage(self):
        """
        All our GUI stuff that involves creating the GUI will go here.
        """
        stage = pygame.display.set_mode([700, 800])
        self.draw_stage(stage)
        return stage
    
    
        
        
