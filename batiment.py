import random
from personne import *

class batiment:
	def __init__(self,categorie=None):
		"""categorie:
		maison -> hebergement d'habitant -> posibilite d'hebergement, a voir avec le proprio
		logement -> maison + hebergement pour le gain
		magasin -> maison + vend des choses ( objet ou services )
		prison -> prison, n'abrite que les prisonnier
		mairie -> un par village, n'abrite personne
		"""		
		self.categorie=categorie
		if self.categorie == None:
			temp = random.randrange(0,20)
			if temp == 0:
				self.categorie = "prison"
			elif temp > 0 and temp <= 4:
				self.categorie = "hebergement"
			elif temp > 4 and temp <= 13:
				self.categorie = "magasin"
			else:
				self.categorie = "maison"
		if self.categorie == "maison" or self.categorie == "hebergement" or self.categorie == "magasin":
			self.habitants = genererFamille(self)
		else:
			self.habitants = []
	
	def out(self):
		print("    batiment de type "+self.categorie+" creer :")
		for loop in self.habitants:
			loop.out()