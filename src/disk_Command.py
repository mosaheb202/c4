class diskCommand:
    
    def __init__(self, color):
        self.color = color;
        
    def get_color(self):
        return self.color
    
    def execute():
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
                    turn()
                    return True
        return False        