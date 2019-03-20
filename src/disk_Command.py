from c4model import Model

class diskCommand(c4_commands):
    
    def __init__(self, model, color):
        self.color = color
        self.model = model
        
    def get_color(self):
        return self.color
    
    def execute(self, column):
        """
        Create a disk with the given x,y coordinates and color.
        Typically will call a strategy design pattern to actually create the
        disk.
        """
        
        if (is_filled() == False):
            for row in range (5,-1,-1):
                if self.frame[row][column] == None:
                    self.frame[row][column] = Disk(point(row, column), self.current_player)
                    self.available_slots -= 1
                    self.model.turn() #how to call this as a function of model (so that player is static)
                    return True
        return False