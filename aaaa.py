import numpy as np
from PIL import Image

print(test)
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
			fichier.write('v '+str(i)+' '+str(j)+' '+str(tabAlt[i][j]*2)+'\n')
	fichier.write('\n\n\n')
	fichier.close()
	print ('fin de l\'écriture des points, nombre de points : ', cpt)

"""
def listeFace(tabPoints):
	tabFace = []
	longueur = 1200
	largeur = 1200
	print ('largeur : '+str(largeur)+'longueur : '+str(longueur))
	for i in range(longueur) :
		for j in range(largeur) :
			tabSommets=[]
			tabSommets.append(tabPoints[i][j])
			tabFace.append(tabSommets)
	return tabFace
"""

def listeFace():
	fichier = open('test.obj','a')
	print('ecriture des faces')
	for i in range(1,726*1081):
		fichier.write('f '+str(i)+'/'+' '+str(i+1)+' '+str(i+1081)+' '+str(i+1080)+' \n')
	print('fin de l\'ecriture des faces\nConversion terminé')
	fichier.close()
"""
def texture():
	im = getImArray("quey.jpg")
	longueur = len(im)
	largeur = len(im[0])
	fichier = open("test.obj", "a")
	print("ecriture de la texture")
	for i in range():
		fichier.write('vt '+str(i/))

	fichier.close()"""

def main():
	listPoints(getImArray("quey.tiff"))
	listeFace()
	#texture()
main()
