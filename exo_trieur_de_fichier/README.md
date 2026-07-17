# File Sorter

Moves each file from a folder into a subfolder named after its extension
(e.g. "Mes fichiers (.pdf)"), creating that subfolder if needed. Existing
files are never overwritten — a colliding file gets a timestamp appended
to its name instead.

## Requirements

- Python 3.10+

## Usage

Open a terminal and move into the script's folder:

```
cd "C:\path\to\exo_filtreur_de_fichier"
```

Then run the script, pointing it at the folder you want to sort:

```
python main_trie.py --dossier "C:\path\to\target\folder"
```

`--dossier` takes the absolute path of the folder to sort.

For a recursive sort (subfolders included), add `--mode r`:

```
python main_trie.py --dossier "C:\path\to\target\folder" --mode r
```

## Implementation notes

- Files are grouped into subfolders named after their extension
- Name collisions are resolved with a timestamp, never by overwriting
- Error handling for missing/invalid target folders
