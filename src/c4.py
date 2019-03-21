import pygame
import time
import random
from time import sleep
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
        Loads the text onto the screen.
        """
        
        text_surface = font.render(text, True, WHITE)
        return text_surface, text_surface.get_rect()
    
    def make_button(self, text, x, y, width, height, original_color, active_colour, func):
        """
        Creates a button with text and postion x, y on the GUI. The button is a rectangle, so
        it has its own width, height, color and active color that it turns lighter when the user
        hovers over it. The button also performs the function that is passed in when clicked.
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
            
    def make_column(self, text, x, y, width, height, original_color, active_colour, func, column):
        """
        Creates a button with text and postion x, y on the GUI. The button is a rectangle, so
        it has its own width, height, color and active color that it turns lighter when the user
        hovers over it. The button also performs the function that is passed in when clicked.
        """
        
        user_mouse = pygame.mouse.get_pos()
        user_click = pygame.mouse.get_pressed()
    
        #If the user hovers over the button, show some activity by changing color.
        if x + width > user_mouse[0] > x and y + height > user_mouse[1] > y:
            pygame.draw.rect(screen_display, active_colour,(x, y, width, height))
            
            #If the user clicks the button, execute the function func.
            if user_click[0] == 1 and func != None:
                func(column)
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
        # loop makes sure that events are being processed.
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
        
    #def wait(self, time_start):
            #"""
            #A function that allows the view to wait for the transition of screens
            #"""
            #if time_start - pygame.time.get_ticks() > 500:
                #return False
            #return True
        
    def draw_stage(self):
        """
        Draws the game board and keeps the users on the screen
        until the user closes the game.
        """
        screen_display.fill(BLUE)
        
        #time_start = pygame.time.get_ticks()
        
        #while self.wait(time_start):
            #print("buffering")
            
        sleep(0.2) #Need to sleep in order for the click to open this screen doesn't also click on this screen
        
        start = True
        while start:
            self.make_button("<", 5, 5, 30, 40, RED, LIGHT_RED, self.start)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                    
            for col in range(NUMB_COLUMNS):
                #self.make_button("Back", col, 50, 50, None, None, self.add_disk)
                #for row in range(NUMB_ROWS):
                self.add_column(col)
                disks = self.model.column_amount(col)
                print(disks)
                for row in range(0, NUMB_ROWS - disks):
                    pygame.draw.circle(screen_display, BLACK, (col*SIZE + SIZE, row*SIZE + SIZE//2), RADIUS)
                for row in range(0, disks + 1):
                    disk = self.model.get_disk(col, 6-row) #All of the values that we get should be disks.
                    if disk != None:
                        p = disk.get_player().get_player_number()
                        if p == 1:
                            color = GREEN
                        else:
                            color = RED
                    else:
                        color = WHITE
                        print('None')
                    pygame.draw.circle(screen_display, color, (col*SIZE + SIZE, (6-row)*SIZE + SIZE//2), RADIUS)                    
                    
            #if self.model.update():
                    
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
    
    def add_disk(self, column):
        """
        Will add a disk to the model when a column is clicked, then the model will return and call draw_stage.
        """
        sleep(0.2)
        self.model.insert_disk(column)
        #self.draw_stage()
        
    def add_column(self, col):
        """
        Update current stage to have 7 columns for actual game play.
        These columns are where the players will click in order to drop a disk.
        """
        x = col*SIZE + SIZE//2
        self.make_column("", x, 0, 100, 800, BLUE, LIGHT_BLUE, self.add_disk, col)
    
    def update_game(self):
        """
        Update the view by calling on the Model.
        """
        pass
    
    def game_quit(self):
        pygame.quit()
        quit()

if __name__ == '__main__':
    game = C4()
    game.start()
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
