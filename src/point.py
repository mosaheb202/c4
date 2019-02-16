"""
A Point class which will be used to store positions of
each disk object. This class allows the programmer to get
both x and y coordinates as well as changing them. This helps
when a disk is being placed in any position by the user.
"""

class Point:
    def __init__(self, x, y): # Constructor to set x and y coordinates
        self.x = x
        self.y = y

    def __str__(self): # Function to output coordinates for user
        return "("+ str(self.x) +","+ str(self.y) +")"

    def getX(self): # Function to get the x coordinate
        return self.x

    def getY(self): # Function to get the y coordinate
        return self.y

    def changeXY(self, newX, newY): # Function to change x and y coordinates
        if(newX is not None and newY is not None):
            self.x = newX
            self.y = newY
        elif(newX is not None):
            self.x = newX
        elif(newY is not None):
            self.y = newY
