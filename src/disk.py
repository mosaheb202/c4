from point import Point
from player import Player

"""
A Disk class which has a point object to reference where on the grid
the disk is placed as well as a colour attribute for the View to
display to the user. 
"""

class Disk:
	def __init__(self, point, player):
		
		if player == 1:
			self.player = Player(1)
		else:
			self.player = Player(2)
		self.point = point
		self.dropped = False
	
	def get_player(self):
		"""
		Returns the current player
		"""
		return self.player
	
	def get_color(self):
		"""
		returns the color of the current player
		"""
		return self.player.get_color()
	
    
	def set_color(self, color):
		"""
		Sets the current colour
		"""
		self.color = color
	
	def get_point(self):
		"""
		Returns the current point
		"""
		return self.point


	def is_dropped(self):
		"""
		Returns if the disk is dropped
		"""
		return self.dropped
    

	def change_disk_status(self):
		"""
		Returns if the disk is dropped
		"""
		if (self.dropped is False):
			self.dropped = True
		
	def __eq__(self, other):
		"""
		Returns if players are the same
		"""
		if other == None:
			return False
		if self.player.get_player_number() == other.player.get_player_number():
			return True
		return False
