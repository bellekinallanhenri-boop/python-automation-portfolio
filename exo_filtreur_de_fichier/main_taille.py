import argparse
from pathlib import Path 
from gros_fichiers import Filtreur

def filtrer(dossier):
    """ Fonction ou va s'executer le filtre et le trie"""
    if not dossier.exists(): # Si le dossier entre en parametre n'existe pas
        print(f"[Erreur]: le dossier {dossier} n'existe pas.")
        return 
         
    if not dossier.is_dir(): # Si le parametre entre n'est pas un dossier
        print(f"[Erreur]: Le dossier {dossier} n'est pas un dossier.")
        return 
    
    fil = Filtreur(dossier)
    #fil.gf()
    file = f"{str(fil.gf())}"
    print(f"Trie des fichiers effectue avec succes. Veuillez consulter le fichier {file} cree.") 
    

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="Objet ecrivant le dictionnaire de fichier trie l'exportant dans un fichier '.txt'")
    parser.add_argument(
        "--dossier",
        type = Path,
        default = Path("."),
        help = "Dossier cible (defaut: .)",
    )

    
    args = parser.parse_args()

    filtrer(args.dossier)