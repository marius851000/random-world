

def quantifie(nombre, masculin = True):
	if nombre == 0:
		if masculin:
			return "aucun"
		else:
			return "aucune"
	elif nombre == 1:
		if masculin:
			return "un"
		else:
			return "une"
	elif nombre == 2:
		return "deux"
	elif nombre <= 4:
		return "quel'que"
	elif nombre <= 8:
		return "beaucoup"
	else:
		return "enormement"

if __name__ == "__main__":
	for loop in range(15):
		print(str(loop) + " : " + quantifie(loop, True) + "-" + quantifie(loop, False))