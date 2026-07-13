from pathlib import Path
from datetime import datetime
#import pickle

taille_seuil = 5 * 1024 * 1024 # 5 Mo

class Filtreur:
     """ Objet charge de trier les fichiers de plus de taille_seuil et de les expoter 
         dans un fichier '.txt' """
     def __init__(self,dossier):

        self.dossier = Path(dossier)
    
     def _dico_scanneur(self):
         """ Methode parcourant tout le dossier cible et retournant un dictionnaire des
             fichiers trouves avec leur taille et ranges par ordre decroissant"""
         if not self.dossier.is_dir():
             print(f"[Erreur]: Le dossier {self.dossier} n'est pas un dossier.")
             return 
         if not self.dossier.exists(): # Si le dossier entre en parametre n'existe pas
             print(f"[Erreur]: le dossier {self.dossier} n'existe pas.")
             return 
         if not any (file.is_file() for file in self.dossier.rglob("*")): # Si dans le dossier entre en parametre il n'existe aucun fichier
            print("[Erreur]: Il n'y a pas de fichier ici.)")
            return
         fichiers_dico = {
             fichier.name: fichier.stat().st_size/(1024 * 1024) 
            for fichier in self.dossier.rglob("*")
             if fichier.is_file() and fichier.stat().st_size >= taille_seuil
         }# Cree un dictionnaire ou se trouveront les fichier filtres avec leur taille
         fichier_dico_trie = dict(sorted(fichiers_dico.items(), key=lambda element:element[1], reverse=True)) # Range ce dictionnaire par ordre decroissant

         texte = "{\n" 
    
         for cle, valeur in fichier_dico_trie.items():
            texte += f"    {cle}: {valeur:.2f} Mo,\n"
            texte += "   \n"
         texte += "}"

         return texte
     

     def _fichier_vide(self):
         """ Methode creant les fichiers vides sur lesquels seront plutard ecrit les dictionnaire"""
         if not self.dossier.exists(): # Si le dossier entre en parametre n'existe pas
             print(f"[Erreur]: le dossier {self.dossier} n'existe pas.")
             return 
         
         if not self.dossier.is_dir(): # Si le parametre entre n'est pas un dossier
             print(f"[Erreur]: Le dossier {self.dossier} n'est pas un dossier.")
             return 
         dt = datetime.now().strftime("%y-%m-%d_%H-%M-%S-%f")
         (self.dossier/f"autoTaille_{dt}.txt").touch() # Cree un fichier avec un prefixe 'autoTaille' et la date du jour
         fichier_path = Path(f"{self.dossier}/autoTaille_{dt}.txt")
         return fichier_path

     def gf(self):
         
        """ Methode ecrivant le dictionnaire trie dans le fichier vide"""
        fichier = self._fichier_vide()
        #self._dico_scanneur()
        dico = self._dico_scanneur() 
        #fichier_path = Path(fichier)
        # Recuperer le dictionnere le le fichier pour verifier s'il on ete retourne avec succes
        ok_dico = bool(dico) # True si le retour a ete effectue
        #ok_fichier = bool(self._fichier_vide()) # Pareil

        if bool(fichier) and ok_dico: # S'il y a un retour
            
            try: 
                
                (fichier).write_text(f"{dico}", encoding="utf-8")
                
            except FileNotFoundError:
                print(f"[Erreur]: {fichier} est introuvable.")
            except PermissionError:
                print(f"[Erreur]: permission refusee dur {fichier}")
            except OSError:
                print(f"[Errreur]: impossible d'ecrire le dictionnaire de fichiers sur {fichier}.") 
            
        
         
        else: # Si aucun retour
            print("[Erreur]: le dictionnaire de fichier ou le fichier '.txt' n'a pas ete cree")
            
        
        return fichier
        
     

#fil = Filtreur(".")
#fil.gf()

         
