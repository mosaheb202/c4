import pygame
from c4model import Model
from c4view import View

"""
This is the class which actually runs the game.

"""


class C4:
    def start():
        #model = model()
        model = Model
        v = View(model)
        stage = v.create_stage()

if __name__ == '__main__':
    C4.start()
    

class c4:
    def __init__():
        view = View()
        
        
        
