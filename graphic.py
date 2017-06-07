from rpg import *

class graphic:
	def __init__(self):
		self.game = rpg()
		self.game.generateWorld()
		self.game.out()
		print(self.game.start())
		playing = True
		while playing:
			entre = input()
			resultat = self.game.input([entre,True])#True : time pass, False : command without time advance
			if resultat['ok'] == False:
				print("votre entré est incorrecte")
			self.rendu(resultat)
	
	def rendu(self, resultat):
		print(resultat)