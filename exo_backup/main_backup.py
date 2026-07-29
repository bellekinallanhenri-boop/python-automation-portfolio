import argparse
from pathlib import Path
from backup import Sauvegarde



def Save(dossier, destination):
    save = Sauvegarde(dossier)
    save.sv(destination)





if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Cree la sauvegarde d'un dossier")

    parser.add_argument(
        "--dossier",
        type=Path,
        default=Path("."),
        help="Dossier cible (defaut : /.)",
    )

    parser.add_argument(
        "--destination",
        type=Path,
        required=True,
        help="Destination du dossier sauvegarde",
    )

    args = parser.parse_args()

    Save(args.dossier,args.destination)
