# Company Folder Structure Generator

Creates a standard folder structure for a company: 4 main folders
(Comptabilité, RH, Client, Facture), each containing a subfolder named
after the current year. Existing folders are never duplicated or
overwritten.

## Requirements

- Python 3.10+

## Usage

Open a terminal and move into the script's folder:

```
cd "C:\path\to\exo_arborescence"
```

Then run the script, giving it a company name and (optionally) a target folder:

```
python arborescence.py --entreprise "Agri-Cameroun" --dossier "C:\path\to\target\folder"
```

`--entreprise` is required. `--dossier` is optional (defaults to the current folder).

## Example output

```
Agri-Cameroun/
├── Comptabilité/
│   └── 2026/
├── RH/
│   └── 2026/
├── Client/
│   └── 2026/
└── Facture/
    └── 2026/
```

## Implementation notes

- The year subfolder is computed dynamically (`datetime.now().year`), never hardcoded
- Safe to run multiple times on the same target: `exist_ok=True` prevents crashes or duplicates
