import numpy as np
from PIL import Image

#1. lie une image et le converti en tableau d'altitudes
def getImArray() :
       im = Image.open("27-38.tif") #Ouvre l'image tif et le met dans la variable im
       imArray = np.array(im)       #Convertie le tif en matrice contenant les altitudes de chaque points de l'image
       print("Conversion de l'image en tableau terminé. \n")
       return imArray

def listPoints(tabAlt,L):
    Ny = len(tabAlt[0])
    Nx = len(tabAlt)
    a=L/(Nx-1)
    tab=[]
    cpt=0
    f = open('carte.obj','w')
    f.write('o carte \n\n')
    for j in range(Ny):
           tab2=[]
           for i in range(Nx):
              tab3=[]
              cpt+=1
              f.write('v'+' '+str(i*a)+' '+str(j*a)+' '+str(tabAlt[i][j])+'\n')
              x=i*a
              y=j*a
              z=tabAlt[i][j]
              tab3.append(x)
              tab3.append(y)
              tab3.append(z)
              tab2.append(tab3)
           tab.append(tab2)
    f.write('\n\n\n')
    f.close()
    print("Listage des points terminé, points = ", cpt, "\n")
    return tab


def listFace(tabPoints):
       tabFace = [] #tableau qui va contenir les faces et que l'on retournera à la fin
       longueur = len(tabPoints)
       largeur = len(tabPoints)
       for i in range(longueur-1):        
              for j in range(largeur-1):
                     tabSommets=[]
                     s1=tabPoints[i][j]     #Sommet en haut à gauche de la face
                     s2=tabPoints[i][j+1]   #Sommet en haut à droite de la face
                     s3=tabPoints[i+1][j+1] #Sommet en bas à droite de la face
                     s4=tabPoints[i+1][j]   #Sommet en bas à gauche de la face
                     tabSommets.append(s1)  #On ajoute les sommets dans tabSommets pour regrouper les sommets d'une face
                     tabSommets.append(s2)  #
                     tabSommets.append(s3)  #
                     tabSommets.append(s4)  #
                     tabFace.append(tabSommets)#Puis on ajoute tabSommets dans tabFace
       print("Listage des faces consituées de 4 sommets de l'image terminé. \n")            
       return tabFace



def ecrireFace():
       f = open('carte.obj','a')

       for b in range(1,1199*1199,4):
              f.write('f '+str(b)+' '+str(b+1)+' '+str(b+2)+' '+str(b+3)+'\n')
       f.close()
       
       print("le fichier obj a bien été généré.")






def main():
    L=410 #taille réelle de la carte en mm
    tabAlt=getImArray()
    tabPoints=listPoints(tabAlt,L)
    
    tabFace=listFace(tabPoints)
    n2=len(tabFace)
    
    print("Le nombre de faces est de ", n2, ". \n")
    ecrireFace()

main()
