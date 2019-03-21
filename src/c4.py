import pygame
import time
import random
from c4model import Model

"""
This is the class which actually runs the game.
It serves the purpose of being a hybrid of the view/controller.
"""
#Initialize Pygame
pygame.init()

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
HELP_MENU_IMAGE = pygame.image.load('c4helpmenu.png')

screen_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class C4:

    def __init__(self):
        """
        Initialize the model and view to start up the game
        """
        self.model = Model()
        #self.view = View(self.model)
        self.start()
        
    def print_text(self, text, font):
        """
        Loads the text onto the surface.
        """
        
        text_surface = font.render(text, True, WHITE)
        return text_surface, text_surface.get_rect()
    
    def make_button(self, text, x, y, width, height, original_color, active_colour, func):
        """
        Creat a button with text and postion x,y. The button is rectangle, so
        it has its own width, height, color, and color that it turns into when
        highlighted. Perform the function func when pressed.
        """
        
        user_mouse = pygame.mouse.get_pos()
        user_click = pygame.mouse.get_pressed()
    
        #If the user hovers over the button, show some activity by changing color.
        if x + width > user_mouse[0] > x and y + height > user_mouse[1] > y:
            pygame.draw.rect(screen_display, active_colour,(x, y, width, height))
            
            #If the user clicks the button, execute the function func.
            if user_click[0] == 1 and func != None:
                func()
        else:
            pygame.draw.rect(screen_display, original_color, (x, y, width, height))
        
        
        #textsize = (height * width)//350
        small_text = pygame.font.Font("freesansbold.ttf", 20)                       
        text_surface, text_rectangle = self.print_text(text, small_text)
        text_rectangle.center = ((x + (width / 2)), (y + (height / 2)))
        screen_display.blit(text_surface, text_rectangle)
            
                                    
    def start(self):
        """
        Displays the start menu at upon the start of the game.
        """
        #This loop makes sure that events are being processed.
        start = True
        
        while start:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            screen_display.fill(BLACK)
    
            large_text = pygame.font.Font('freesansbold.ttf', 64)
                                                                
            text_surface, text_rectangle = self.print_text("C4: A Connect 4 Game", large_text)
            text_rectangle.center = ((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
            screen_display.blit(text_surface, text_rectangle)
    
            # start button
            self.make_button("Start!", 150, 450, 100, 70, GREEN, LIGHT_GREEN, self.draw_stage)
                                                                    
            # help button
            self.make_button("Help", 350, 450, 100, 70, BLUE, LIGHT_BLUE, self.help_menu)
                                                                    
            # exit button
            self.make_button("Exit", 550, 450, 100, 70, RED, LIGHT_RED, self.game_quit)
                                                                        
                                                                        
            pygame.display.update()
            clock.tick(15)
            
    def draw_stage(self):
        """
        Draws the game board and keeps the users on the screen
        until the user closes the game.
        """
        screen_display.fill(BLUE)
        
        start = True
        while start:
            self.make_button("Back", 5, 5, 50, 50, RED, LIGHT_RED, self.start)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                    
            for col in range(NUMB_COLUMNS):
                for row in range(NUMB_ROWS):
                    pygame.draw.circle(screen_display, BLACK, (col*SIZE + SIZE, row*SIZE + SIZE//2), RADIUS)
                    
            pygame.display.update()
        
    def help_menu(self):
        """
        Displays the help screen that explains the game's rules
        at the click of a button.
        """
        
        start = True
        while start:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            screen_display.fill(BLACK)
            
            #Back Button
            screen_display.blit(HELP_MENU_IMAGE, (0,50))
            self.make_button("Back", 0, 50, 100, 50, RED, LIGHT_RED, self.start)
            pygame.display.update()
        
    def game_quit(self):
        pygame.quit()
        quit()

if __name__ == '__main__':
    #c4 = C4()
    #running = False
    #player = c4.model.current_player
    
    #while(running == False):
        #for event in pygame.event.get(): #buffer so game waits for players
            #print(event)
            #if event.type == pygame.QUIT:
                #pygame.display.quit()
                #running = True
                #break

            #if player%2 == 1: #player 1
                ##player 1 drops his disk
                ##checks for game over
                #break

            #elif player%2 == 0: #player 2
                ##player 2 drops his disk
                ##checks for game over
                #break

            #player += 1
    #print("Game is done if this is printed")

    #Comment main out to see GUI if there is errors.
    game = C4()
    c4.start()
    
        
