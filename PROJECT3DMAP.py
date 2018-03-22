import numpy as np
from PIL import Image


def getImArray(nom) :
	im = Image.open(nom)
	imArray = np.array(im)
	print("Image convertie en tableau")
	return imArray

def listPoints(tabAlt):
	longueur = len(tabAlt)
	largeur = len(tabAlt[0])
	print(longueur,' ', largeur)
	cpt=0
	fichier = open("test.obj", "w")
	fichier.write('o carte\n\n')
	print("ecriture des points")
	for i in range(longueur):
		for j in range(largeur):
			cpt+=1
			fichier.write('v '+str(i)+' '+str(j)+' '+str(tabAlt[i][j])+'\n')
	fichier.write('\n\n\n')
	fichier.close()
	print ('fin de l\'écriture des points, nombre de points : ', cpt)


def listeFace(longueur,largeur):
	fichier = open('test.obj','a')
	print('ecriture des faces')
	cpt=0
	for i in range(1,(largeur)*(longueur)):
		cpt+=1
		fichier.write('f '+str(i)+' '+str(i+1)+' '+str(i+1081)+' '+str(i+1080)+' \n')
	print('fin de l\'ecriture des faces\nConversion terminé')
	print (cpt)
	fichier.close()

def texture(longueur,largeur):
	im = getImArray("quey.jpg")
	longueurIm = len(im)
	largeurIm = len(im[0])
	fichier = open("test.obj", "a")
	print("ecriture de la texture")
	for i in range(longueurIm):
		for j in range(largeurIm):
			fichier.write('vt '+str(i/(largeurIm/largeur))+' '+str(j/(longueurIm/longueur)))
	fichier.close()

def main():
	matrice = getImArray("quey.tiff")
	listPoints(matrice)
	longueur = len(matrice)
	largeur = len(matrice[0])
	print(longueur,largeur)
	listeFace(longueur,largeur)
	print("DEDICACE A TOUT LES FRERES ENFERMES")
	#texture()
main()
