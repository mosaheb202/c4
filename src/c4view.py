import pygame
import c4model
#import c4
#import disk

import time
import random

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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


#Define Color Constants
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
LIGHT_RED = (245, 0, 0)
LIGHT_GREEN = (0, 245, 0)
LIGHT_BLUE = (0, 0, 245)
WHITE = (255,255,255)

pygame.init()

screenDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('C4: A Connect 4 Game')
clock = pygame.time.Clock()

def print_text(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


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

    def make_button(text, x, y, width, height, original_color, active_colour):
        user_mouse = pygame.mouse.get_pos()

        # if user hovers over button
        if x + width > user_mouse[0] > x and y + height > user_mouse[1] > y:
            pygame.draw.rect(gameDisplay, active_colour,(x, y, width, height))
        else:
            pygame.draw.rect(gameDisplay, original_color, (x, y, width, height))
                        
        smallText = pygame.font.Font("freesansbold.ttf",20)
                                
        textSurface, textRectangle = print_text(text, smallText)
        textRectangle.center = ((x + (width / 2)), (y + (height / 2)))
        gameDisplay.blit(textSurface, textRectangle)
            
                                    
    def start_screen():
                                        
    intro = True
                                            
    while intro:
        for event in pygame.event.get():
            # print(event)
                                                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                                                            
        gameDisplay.fill(BLACK)

        largeText = pygame.font.Font('freesansbold.ttf',115)
                                                                
        TextSurface, TextRectangle = print_text("C4: A Connect 4 Game", largeText)
        TextRectangle.center = ((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
        screenDisplay.blit(TextSurface, TextRectangle)

        # start button
        make_button("Start!", 100, 500, 100, 70, GREEN, LIGHT_GREEN)
                                                                    
        # help button
        make_button("Help", 300, 500, 100, 70, BLUE, LIGHT_BLUE)
                                                                    
        # exit button
        make_button("Exit", 500, 500, 100, 70, RED, LIGHT_RED)
                                                                        
                                                                        
        pygame.display.update()
        clock.tick(15)

start_screen()

    
    
        
        
