import random

class personnage():
	def __init__(self,sexe=None,age=None,living=True,marriedTo=None, mother=None, Father=None, liveIn=None):
		self.living = living
		
		self.sexe = sexe
		if self.sexe == None:
			temp=random.randrange(0,2)
			if temp == 0:
				self.sexe="homme"
			else:
				self.sexe="femme"
		
		self.age = age#ameliorer cela
		if self.age == None:
			self.age = random.randrange(0,70)
		
		self.living = living
		self.marriedTo = marriedTo
		self.mother = mother
		self.liveIn = liveIn
	
	def out(self):
		st=self.sexe + " ager de " + str(self.age) + ","
		if self.marriedTo == None:
			st=st+" qui n'est pas marrie."
		else:
			if self.marriedTo.living == False:
				if self.sexe == "homme":
					st=st+" qui est veuf."
				else:
					st=st+" qui est veuve."
			else:
				st=st+" qui est marrie."
		print("        "+st)

def genererFamille(batiment):
	temp = random.randrange(0,3)#0=pere mort
	if temp == 1:
		pere = personnage(sexe="homme", age=random.randrange(25,60), living=False)
	else:
		pere = personnage(sexe="homme", age=random.randrange(25,60), living=True, liveIn=batiment)
	temp = random.randrange(0,3)#0=mere mort
	if temp == 1:
		mere = personnage(sexe="femme", age=random.randrange(25,60), living=False, marriedTo=pere)
	else:
		mere = personnage(sexe="femme", age=random.randrange(25,60), living=True, marriedTo=pere, liveIn=batiment)
	pere.marriedTo = mere
	if random.randrange(0,3):#si 0 alors pas d'enfin sinon enfant
		pass
	aRetourner = []
	if mere != None:
		aRetourner.append(mere)
	if pere != None:
		aRetourner.append(pere)
		
	for loop in aRetourner:
		loop.out()
	
	return aRetourner