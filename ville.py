import random
from batiment import *

class ville:
	def __init__(self,categorie):
		if categorie == "random" or categorie == None: #categorie de la ville
			temp = random.randrange(0,10)
			if temp == 0:
				self.categorie = "grand"
			elif temp < 3:
				self.categorie = "moyen"
			else:
				self.categorie = "petit"
		else:
			self.categorie = categorie
		
		if self.categorie == "grand":#nombre de batiment
			self.batimentQuant = random.randrange(20,40)
		elif self.categorie == "moyen":
		    self.batimentQuant = random.randrange(10,20)
		else:
			self.batimentQuant = random.randrange(3,10)
		self.batiment=[batiment(categorie="mairie")]
		for loop in range(self.batimentQuant):#generation des batiment
			self.batiment.append(batiment())
	
	def out(self):
		print("ville de type \""+self.categorie+"\" creer avec "+str(self.batimentQuant)+" batiment :")
		for loop in self.batiment:
			loop.out()