from rpg import *
from ville import *
from batiment import *

def CategorieBatimentDansVille(ville):
	maison = []
	hebergement = []
	magasin = []
	prison = []
	mairie = []
	for loop in ville.batiment:
		if loop.categorie == "maison":
			maison.append(loop)
		elif loop.categorie == "hebergement":
			hebergement.append(loop)
		elif loop.categorie == "magasin":
			magasin.append(loop)
		elif loop.categorie == "prison":
			prison.append(loop)
		elif loop.categorie == "mairie":
			mairie.append(loop)
		else:
			pass
	
	retour = {"maison":maison,
	"hebergement":hebergement,
	"magasin":magasin,
	"prison":prison,
	"mairie":mairie}
	return retour

class graphic:
	def __init__(self):
		self.game = rpg()
		self.game.generateWorld()
		self.game.out()
		print(self.game.start())
		playing = True
		while playing:
			entre = input("->")
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
				print(CategorieBatimentDansVille(resultat["city"]))
		else:
			print("vous n'êtes pas dans une ville.")