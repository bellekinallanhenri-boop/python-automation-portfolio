# Large File Finder

Recursively scans a folder and exports a text report listing all files larger
than 5 MB, sorted from heaviest to lightest.

## Requirements

- Python 3.10+

## Usage

Open a terminal and move into the script's folder:

```
cd "C:\path\to\exo_filtreur_de_fichier"
```

Then run the script, pointing it at the folder you want to scan:

```
python main_taille.py --dossier "C:\path\to\target\folder"
```

`--dossier` takes the absolute path of the folder to analyze.

## Example output

Running the script generates a timestamped file, e.g. `autoTaille_26-07-13_10-42-01.txt`,
containing something like:

```
{
    video_project_final.mp4: 842.13 Mo,
    backup_database.sql: 156.40 Mo,
}
```

## Implementation notes

- Recursive traversal via `pathlib.Path.rglob()`
- Timestamped report generation
- Error handling for missing folders, permission errors, and file encoding (UTF-8)
