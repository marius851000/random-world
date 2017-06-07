from rpg import *
from ville import *
from batiment import *
from quantificateur import quantifie


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

def rendu(resultat):
	for loop in resultat['change']:
		pass
	if resultat['city'] != None:#si dans une ville
		if resultat['batiment'] != None:#si dans un batiment
			print("vous vous trouvez dans un batiment")
		else:#si dans la place de la ville
			categorie = CategorieBatimentDansVille(resultat["city"])
			quantMaison = len(categorie["maison"])
			quantHebergment = len(categorie["hebergement"])
			quantMagasin = len(categorie["magasin"])
			quantPrison = len(categorie["prison"])
			quantMairie = len(categorie["mairie"])
			print("Vous êtes dans une ville avec :")
			print(quantifie(quantMaison, False)+" maison,")
			print(quantifie(quantHebergment, True)+" hebergement,")
			print(quantifie(quantMagasin, True)+" magasin,")
			print(quantifie(quantPrison, False)+" prison,")
			print(quantifie(quantMairie, False)+" mairie,")

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
			rendu(resultat)
		else:
			print("vous n'êtes pas dans une ville.")