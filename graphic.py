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
		for loop in resultat['change']:
			pass
		
		if resultat['city'] != None:#si dans une ville
			if resultat['batiment'] != None:#si dans un batiment
				print("vous vous trouvez dans un batiment")
			else:#si dans la place de la ville
				print("vous êtes sur la place de la ville")
		else:
			print("vous n'êtes pas dans une ville.")