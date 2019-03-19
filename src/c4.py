import pygame
from c4model import Model
from c4view import View

"""
This is the class which actually runs the game.

"""


class C4:

    def __init__(self):
        """
        Initialize the model and view to start up the game
        """
        self.model = Model()
        self.view = View(self.model)
        self.start(self.view)
        
    def start(self, v):
        """
        Starts up the game bringing up the start screen
        """
        #model = Model()
        #view = View(model)
        stage = v.create_stage() #TODO: initialize start screen and link
                                 #stage to start screen 

if __name__ == '__main__':
    c4 = C4()
    running = False
    player = c4.model.current_player
    
    while(running == False):
        for event in pygame.event.get(): #buffer so game waits for players
            print(event)
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = True
                break

            if player%2 == 1: #player 1
                #player 1 drops his disk
                #checks for game over
                break
                #continue
            elif player%2 == 0: #player 2
                #player 2 drops his disk
                #checks for game over
                break
                #continue

            player += 1
            #player = player % 2
    print("Game is done if this is printed")
    
        
        
        
