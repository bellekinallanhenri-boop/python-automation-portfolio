# Folder Backup Tool

Creates a timestamped backup copy of a folder. If a backup with the exact
same name already exists (two backups run within the same second), a
numeric suffix is appended instead of overwriting anything. Every backup
includes a text log listing what was copied.

## Requirements

- Python 3.10+

## Usage

Open a terminal and move into the script's folder:

```
cd "C:\path\to\exo_backup"
```

Then run the script, pointing it at the folder to back up and where to store the backup:

```
python main_backup.py --dossier "C:\path\to\source\folder" --destination "C:\path\to\backups"
```

`--destination` is required. `--dossier` is optional (defaults to the current folder).

## Example output

```
backups/
└── backup_2026-07-19-20-35-15/
    ├── rapport_backup_2026-07-19.txt
    ├── document1.pdf
    └── document2.pdf
```

Log file content:

```
Sauvegarde effectuee le 2026-07-19 a 20:35
Source : C:\path\to\source\folder
Destination : C:\path\to\backups\backup_2026-07-19-20-35-15

Fichier(s) copie(s) : 2
-> Aucune erreur rencontree
```

## Implementation notes

- Name collisions are resolved with an incremental suffix (`-1`, `-2`...), never by overwriting
- The log file is written inside the backup folder itself, so it always travels with the backup it describes
