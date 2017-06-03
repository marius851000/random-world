from rpg import *

class graphic:
    def __init__(self):
		self.game = RPG()
		self.game.generateWorld()#creer un monde et le charge
		self.game.start()#commence la partie