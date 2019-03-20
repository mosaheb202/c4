import pygame
import time
import random
#from c4model import Model

"""
This is the class which actually runs the game.
It serves the purpose of being a hybrid of the view/controller.
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
BLUE = (0,0,200)
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0,200,0)
LIGHT_RED = (245, 0, 0)
LIGHT_GREEN = (0, 245, 0)
LIGHT_BLUE = (0, 0, 245)
WHITE = (255,255,255)

#Define Image and Display Constants
pygame.init()

#The global screen display is defined here.
screen_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('C4: A Connect 4 Game')
clock = pygame.time.Clock()  

HELP_MENU_IMAGE = pygame.image.load('c4helpmenu.png')

pygame.init()

def print_text(text, font):
    text_surface = font.render(text, True, WHITE)
    return text_surface, text_surface.get_rect()

def make_button(text, x, y, width, height, original_color, active_colour, func):
    user_mouse = pygame.mouse.get_pos()
    user_click = pygame.mouse.get_pressed()

    # if user hovers over button
    if x + width > user_mouse[0] > x and y + height > user_mouse[1] > y:
        pygame.draw.rect(screen_display, active_colour,(x, y, width, height))
        
        if user_click[0] == 1 and func != None:
            func()
    else:
        pygame.draw.rect(screen_display, original_color, (x, y, width, height))
    
    
    small_text = pygame.font.Font("freesansbold.ttf", 20)                        
    text_surface, text_rectangle = print_text(text, small_text)
    text_rectangle.center = ((x + (width / 2)), (y + (height / 2)))
    screen_display.blit(text_surface, text_rectangle)
        
                                
def start_screen():
                                    
    start = True
                                        
    while start:
        for event in pygame.event.get():
            # print(event)                                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen_display.fill(BLACK)

        large_text = pygame.font.Font('freesansbold.ttf', 64)
                                                            
        text_surface, text_rectangle = print_text("C4: A Connect 4 Game", large_text)
        text_rectangle.center = ((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
        screen_display.blit(text_surface, text_rectangle)

        # start button
        make_button("Start!", 150, 450, 100, 70, GREEN, LIGHT_GREEN, draw_stage)
                                                                
        # help button
        make_button("Help", 350, 450, 100, 70, BLUE, LIGHT_BLUE, help_menu)
                                                                
        # exit button
        make_button("Exit", 550, 450, 100, 70, RED, LIGHT_RED, game_quit)
                                                                    
                                                                    
        pygame.display.update()
        clock.tick(15)
        
def draw_stage():
    
    screen_display.fill(BLUE)
    
    start = True
    while start:
        for event in pygame.event.get():
            # print(event)                                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
                
        for col in range(NUMB_COLUMNS):
            for row in range(NUMB_ROWS):
                #pygame.draw.rect(screen_display, BLUE, [col*SIZE, row*SIZE + SIZE, SIZE, SIZE])
                pygame.draw.circle(screen_display, BLACK, (col*SIZE + SIZE, row*SIZE + SIZE//2), RADIUS)
            
        pygame.display.update()

def help_menu():
    start = True
    while start:
        for event in pygame.event.get():
            # print(event)                                    
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        screen_display.fill(BLACK)        
        screen_display.blit(HELP_MENU_IMAGE, (0,50))
        pygame.display.update()
    
def game_quit():
    pygame.quit()
    quit()

#WE CAN LINK STUFF BELOW. REMINDER TO UNCOMMENT THE TOP IMPORTS ONCE DISK
#IS FIXED.

start_screen()
    
        
