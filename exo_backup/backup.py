from pathlib import Path
from shutil import copytree
from datetime import datetime


class Sauvegarde:
    def __init__(self, dossier):
        #pass
        self.dossier = Path(dossier)

    def _nom_disponible(self, nom_propose, destination):
        return not (destination/nom_propose).exists()
    
    def _sauvegarder_vers(self, nom_candidat, destination):
        chemin_dest = destination/nom_candidat
        return copytree(self.dossier,chemin_dest)
    
    def _log_backup(self, copie_dossier, nb_elt, feed_back):
        date = datetime.now().strftime("%Y-%m-%d")
        heure = datetime.now().strftime("%H:%M")
        nom_log = f"rapport_backup_{date}.txt"

        text_log = f"""Sauvegarde effectuee le {date} a {heure}
Source : {self.dossier}
Destination : {copie_dossier}
 
Fichier(s) copie(s) : {nb_elt}
-> {feed_back}"""
        
        Path(copie_dossier/nom_log).write_text(text_log)


    def sv(self, destination):
        
        date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        nom_propose = f"backup_{date}"
        suffixe = 1
        base = f"{suffixe:03d}"
        feed_back = "Aucune erreur rencontree"
        while not self._nom_disponible(nom_propose,destination):
            nom_propose = f"{nom_propose}-{base}"
            suffixe += 1
            base = f"{suffixe:03d}"
            
        
        backup = self._sauvegarder_vers(nom_propose, destination)

        nb_elt = sum(1 for e in backup.rglob("*") if e.is_file())
        nb_elt_origine = sum(1 for e in self.dossier.rglob("*") if e.is_file())

        if nb_elt < nb_elt_origine:
            feed_back = f"{nb_elt_origine - nb_elt} fichier(s) non copie(s)"
        
        self._log_backup(backup, nb_elt, feed_back)
