"""Module de tri de fichier par extension.

Deplace chaque fichier d'un dossier vers un sous-dossier nomme d'apres son extension (ex : "Mes
fichiers (.pdf)"), en creant ce sous-dossier si besoin et sans ecraser un fichier existant."""


from pathlib import Path
from shutil import move
from datetime import datetime


class Trieur:
    """La classe permettant de creer les objets utilisant la methode de tri ("tri()")"""
    def __init__(self,dossier):
        """C'est la methode constructeur. Elle est appelee a chaque fois qu'un objet est 
        cree."""
        self.dossier = Path(dossier) # Le parametre "dossier" est converti en objet Path


    def _sous_dossier(self,fichier):
        """Retourne le sous dossier correspondant a l'extension du fichier en le creant s'il 
         n'existe pas."""
        nouveau_dossier = f"Mes fichiers ({fichier.suffix})" # Le nom du sous dossier
        dossier_cible = self.dossier/ nouveau_dossier # Chemin cree avec le nom du nouveau sous dossier
        dossier_cible.mkdir(exist_ok=True) # Creation du sous dossier dans le chemin "dossier_cibe"
        return dossier_cible # Retour du chemin Path 
    
    def _nom_disponible(self, fichier, dossier_cible):
        """Verifie si le nom de CE FICHIER PRECIS est lible dans CE DOSSIER CIBLE PRECIS"""
        return not (dossier_cible/fichier.name).exists() 
    
    def tri(self, mode=None):
        """Deplace chaque fichier du dossier vers un sous-dossier par extension.
        
        Arguments:
          mode (str): 'r' pour un parcours recursif (rglob), sinon parcours simple du dossier (glob)
          
        Retourne:
          int: le nombre de fichiers effectivement deplaces.
          """
        parcours = self.dossier.rglob("*") if mode == "r" else self.dossier.glob("*")# Tout les element contenu dans le dossier
        element = list(parcours) # On transforme un iterateur en liste pour pouvoir parcourir ses elements avec un boucle for
        deplaces = 0
        for elt in element:
            if not elt.is_file(): # On ignore les elements qui ne sont pas des fichiers
                continue
            if elt.parent.name.startswith("Mes fichiers ("): # On ignore les elements dont less dossiers parent commencent
                # avec "Mes fichiers (" (On ne touche pas a un fichier deja range lors d'un tri precedent)
                continue
            if elt.suffix == ".py": # On ne deplace jamais le script (ou un autre fichier .py)
                continue

            dossier_cible = self._sous_dossier(elt)

            if self._nom_disponible(elt,dossier_cible):
                nouveau_chemin = dossier_cible/elt.name
            else: # Si le nom n'est pas disponible, on renomme le fichier
                dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
                nouveau_nom = elt.with_name(f"{elt.stem}_{dt}{elt.suffix}")
                elt.rename(nouveau_nom)
                nouveau_chemin = dossier_cible/nouveau_nom.name

            try:
                move(str(elt),str(nouveau_chemin))
                deplaces += 1
            except OSError as e:
                print(f"[ERREUR]: Impossible de deplacer le fichier {elt.name}:{e}")

        return deplaces
