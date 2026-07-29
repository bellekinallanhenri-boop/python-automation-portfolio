from pathlib import Path
import argparse
from datetime import datetime


def arbor(folder, entreprise):
    dossier = Path(folder) # Conversion en objet Path
    annee = datetime.now().year # -> 2026 (int) au moment de l'ecriture de ce script

    (dossier/f"{entreprise}"/"Comptabilité"/f"{str(annee)}").mkdir(parents=True, exist_ok=True)
    (dossier/f"{entreprise}"/"RH"/f"{str(annee)}").mkdir(parents=True, exist_ok=True)
    (dossier/f"{entreprise}"/"Client"/f"{str(annee)}").mkdir(parents=True, exist_ok=True)
    (dossier/f"{entreprise}"/"Facture"/f"{str(annee)}").mkdir(parents=True, exist_ok=True)
    


if __name__== "__main__":
    parse = argparse.ArgumentParser("Creation de l'arborescence de l'entreprise")
    parse.add_argument(
        "--dossier",
        type=Path,
        default=Path("."),
        help = "Dossier ou sera cree l'arborescence",
    )
    parse.add_argument(
        "--entreprise",
        type=str,
        help="Le nom de l'entreprise",
        required=True,
    )

    arg = parse.parse_args()

    arbor(arg.dossier,arg.entreprise)