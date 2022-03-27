# Créé par tristan.pipi, le 18/01/2022 en Python 3.7
import os
import shutil


class Folder:

    def __init__(self):
        pass

    def folder_constructor(self,path,name):
        '''
        teste si un dossier s'appellant 'name' existe déjà et si non le créé
        param -> path (str) : lien du chemin où le dossier sera créé
                 name (str) : nom du dossier
        exemple : U:\\devoirs\\NSI\\2nde\\exos\\

        !!! Ne pas oublier les doubles back-slash à la fin !!!
        '''
        if not os.path.exists(str(name)) : return os.mkdir(path+str(name))

    def folder_destructor(self,name):
        '''
        teste si un dossier s'appellant 'name' existe déjà et si oui le supprime
        param -> name (str) : nom du dossier
        
        !!! Supprime le contenu du dossier également !!!
        '''
        if not os.path.exists(str(name)) : return shutil.rmtree(str(name))

