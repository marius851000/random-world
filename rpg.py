from ville import *
import random

class RPG:
	def __init__(self):
		self.worldIsLoaded = False
	
	def generateWorld(self):
		self.nombreDeVille = random.randrange(20,50)
		print("nombre de ville : "+str(self.nombreDeVille))
		self.ville = []
		for loop in range(self.nombreDeVille):
			self.ville.append(ville(categorie="random"))
	
	def start(self):
		pass