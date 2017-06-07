from ville import *
import random

class rpg:
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
	
	def generateOut(self):
		player = { "city":self.place,
		"batiment" : self.batiment,
		"change" : self.change}
		return player
	
	def start(self):
		self.place = self.ville[0]
		self.batiment = None
		self.change = ["gameStarted"]
		play = True
		player = self.generateOut()
		return player
	
	def input(self,command):
		self.change=[]
		timeAdvance = command[1]
		commande = command[0]
		splitted = commande.split(" ")
		player = self.generateOut()
		return player
		