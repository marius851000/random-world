from rpg import *

class graphic:
	def __init__(self):
		self.game = rpg()
		self.game.generateWorld()
		self.game.out()
		print(self.game.start())
		playing = True
		while playing:
			print(self.game.input([input(),True]))#True : time pass, False : command without time advance