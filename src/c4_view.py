import pygame
import c4_model
import c4
import disk

import time
import random

"""
This is the view which contains all of the visuals that the user will see. 
It has a model and the GUI (stage) that the user will see.
"""
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0, 0, 255)

light_red = (245, 0, 0)
light_green = (0, 245, 0)
light_blue = (0, 0, 245)

screenDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('C4: A Connect 4 Game')
clock = pygame.time.Clock()

def print_text(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()   


class view:

    def __init__(self, model, stage):
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
    
    def make_button(text,x, y, width, height, original_color, active_colour):
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
                    
            gameDisplay.fill(black)
            
            largeText = pygame.font.Font('freesansbold.ttf',115)
           
            TextSurface, TextRectangle = print_text("C4: A Connect 4 Game", largeText)
            TextRectangle.center = ((display_width / 2),(display_height / 2))
            screenDisplay.blit(TextSurface, TextRectangle)
           
            # start button
            make_button("Start!", 100, 500, 100, 70, green, light_green)
              
            # help button
            make_button("Help", 300, 500, 100, 70, blue, light_blue)
              
            # exit button  
            make_button("Exit", 500, 500, 100, 70, red, light_red)               
                     
            
            pygame.display.update()
            clock.tick(15)            
            
start_screen()