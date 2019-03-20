#from c4_model import Model

class Commands:
    def __init__(self):
        self.command_queue = []
        
    def add_command(self, command):
        """
        Add a command to the command queue
        """
        self.command_queue.append(command)
        
    def remove_command(self, command):
        """
        Remove a command from the command queue
        """
        self.command_queue.pop()
        
    def empty(self):
        """
        empty out the command queue
        """
        self.command_queue = []
        
    def operate_all(self):
        """
        Executes each command within the command_queue
        """
        for disk in self.command_queue:
            disk.execute()
            
    