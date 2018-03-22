import numpy as np
from PIL import Image
import sys


def getImArray(nom) :
	im = Image.open(nom)
	imArray = np.array(im)
	return imArray

def listPoints(tabAlt, nom):
	longueur = len(tabAlt)
	largeur = len(tabAlt[0])
	print('\n>>> longueur :',longueur, ', largeur :',largeur,'\n')
	fichier = open(nom, "w")
	fichier.write('o carte\n\n')
	print(">>> Etape 1/2 : écriture des points\n")
	for i in range(longueur):
		for j in range(largeur):
			fichier.write('v '+str(i)+' '+str(j)+' '+str(tabAlt[i][j])+'\n')
	fichier.write('\n\n\n')
	fichier.close()
	print ('>>> fin de l\'écriture des points\n')


def listeFace(longueur,largeur, nom):
	fichier = open(nom,'a')
	print('>>> Etape 2/2 : écriture des faces\n')
	for i in range(1,(largeur)*(longueur-1)):
		fichier.write('f '+str(i)+'/'+str(i)+' '+str(i+1)+'/'+str(i+1)+' '+str(i+largeur)+'/'+str(i+largeur)+' '+str(i+largeur-1)+'/'+str(i+largeur-1)+' \n')
	print('>>> fin de l\'écriture des faces\n\n>>> Conversion terminé\n')
	fichier.close()

def texture(longueur,largeur, nomTexture, nom):
	im = getImArray(nomTexture)
	longueurIm = len(im)
	largeurIm = len(im[0])
	fichier = open(nom, "a")
	print(">>> Etape 3/3 : écriture de la texture\n")
	for i in range(longueurIm):
		for j in range(largeurIm):
			fichier.write('vt '+str(i/(largeurIm/largeur))+' '+str(j/(longueurIm/longueur)))
	print(">>> Fin de l\'écriture de la texture")
	fichier.close()


def main():

	try :
		nomTiff = sys.argv[1]
		nom = sys.argv[2]
	except (IOError, IndexError) :
		print("vous n'avez entré(e) aucun argument veuillez reesayer !")
		exit()
	matrice = getImArray(nomTiff)
	listPoints(matrice, nom)
	longueur = len(matrice)
	largeur = len(matrice[0])
	listeFace(longueur,largeur, nom)
	#texture(longueur, largeur, nomTexture)
main()
