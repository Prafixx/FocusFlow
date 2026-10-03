import json
from pathlib import Path

DATA_DIR = Path.home() / "FocusFlow"


def carica_json(nome_file, predefinito):
    """Legge un file JSON. Se non esiste o è rovinato, restituisce 'predefinito'."""
    percorso = DATA_DIR / nome_file
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return predefinito
    except json.JSONDecodeError:
        print(f"Il file {nome_file} è rovinato: uso i valori predefiniti.")
        return predefinito


def salva_json(nome_file, dati):
    """Scrive 'dati' in un file JSON (crea la cartella se manca)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    percorso = DATA_DIR / nome_file
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)
