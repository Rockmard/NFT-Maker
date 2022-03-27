from PIL.Image import *
from random import randint
from organisateur import Folder
from chances import Chance


def colors(img_name,background,skin,numéro_de_série):
    '''
    param : img_name -> nom de l'image à modifier [format : 'name.ext'] (str)
            background -> liste d'entiers correspondant à la valeur RGB du fond à modifiée de l'image [format : [64,64,64] ] (list)
            skin -> liste d'entiers correspondant à la valeur RGB du contenu à modifiée de l'image [format : [64,64,64] ] (list)
            numéro_de_série -> entier servant à nommer la nouvelle image (int)

    Sauvergarde dans le dossier où est situé le programme une image modifiée
    '''
    img=open(img_name).convert('RGB')
    (largeur,hauteur)=img.size

    for ligne in range(hauteur) :
        for colonne in range(largeur) :
            if img.getpixel((ligne,colonne)) == (64,64,64) :
                img.putpixel((ligne,colonne),skin)
            elif img.getpixel((ligne,colonne)) == (128,128,128):
                img.putpixel((ligne,colonne),background)

    img.save(str(numéro_de_série)+"/"+img_name[4:-4]+".png")


def fusion(img_name,mask_name):
    '''
    param : img_name -> nom de l'image à modifier [format : 'name.ext'] (str)
            mask_name -> nom de l'image servant de masque [format : 'name.ext'] (str)

    Sauvergarde dans le dossier où est situé le programme une nouvelle image étant le résultat de la fusion de deux images
    '''
    img=open(img_name).convert('RGB')
    mask=open(mask_name).convert('RGB')
    (largeur,hauteur)=img.size

    for ligne in range(hauteur) :
        for colonne in range(largeur) :
            if mask.getpixel((ligne,colonne)) != (255,255,255) :
                img.putpixel((ligne,colonne),mask.getpixel((ligne,colonne)))           

    img.save(img_name)


def nftMaker(n):
    
    ###############   INITIALISE LES CLASSES  #################
    folder = Folder()
    asset = Chance()
    
    for i in range(n):

        #################   CRÉER DOSSIER  ####################
        folder.folder_constructor('',i)
        #################   RANDOMIZER  #######################
        background = (randint(40,200),randint(40,200),randint(40,200))
        skin = (randint(40,200),randint(40,200),randint(40,200))
        chance = randint(1,100)
        #################   MAIN GAUCHE #######################
        colors("src/l.png",background,skin,i)
        fusion(str(i)+"/l.png","src/"+str(asset.get_assets(chance,'l')))
        #################   MAIN DROITE #######################
        colors("src/r.png",background,skin,i)
        fusion(str(i)+"/r.png","src/"+str(asset.get_assets(chance,'r')))



