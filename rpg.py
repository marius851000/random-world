from ville import *
import random

class RPG:
	def __init__(self):
		self.worldIsLoaded = False
	
	def generateWorld(self):
		self.nombreDeVille = random.randrange(20,50)
		self.ville = []
		for loop in range(self.nombreDeVille):
			self.ville.append(ville(categorie="random"))
	
	def out(self):
		for loop in self.ville:
			loop.out()
			
	def start(self):
		self.place = self.ville[0]
		self.batiment = None
		play = True
		while play:
			entree = input("->")
			splited = entree.split(" ")
			if splitted[0] == "goToCity":
				if self.place == self.ville[int(splitted[1])]:
					print("vous etes deja dans cette ville")
				elif self.batiment != None:
					print("vous devez d'abors sortir du batiment.")
				
				