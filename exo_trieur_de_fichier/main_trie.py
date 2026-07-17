import argparse
from pathlib import Path
from trieur import Trieur








def triage(dossier, mode = None):
    trier = Trieur(dossier)
    
    nb_f = Path(dossier).rglob("*") if mode == "r" else Path(dossier).glob("*")
    liste_fichier = list(nb_f)
    nombre_fichier = 0
    for elt in liste_fichier:
        if elt.is_file():
            nombre_fichier += 1
    deplaces = trier.tri(mode)
    print(f"Tri effectue avec succes : {deplaces}/{nombre_fichier}")



if __name__ == "__main__":
    parse = argparse.ArgumentParser("Trie les fichiers par dossiers")
    parse.add_argument(
        "--dossier",
        type = Path,
        default= Path("."),
        help="Dossier cible. Defaut = Dossier courant",
    )

    parse.add_argument(
         "--mode",
         default=None,
         help=" 'r' pour scan recursif",
    )

    arg = parse.parse_args()

    triage(arg.dossier, arg.mode)


    