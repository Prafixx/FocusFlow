# resources.py
# Trova i file inclusi nell'app (come l'icona), sia quando lanci "python main.py"
# sia quando l'app è diventata un .exe creato con PyInstaller.
import sys
from pathlib import Path


def resource_path(relativo):
    """Restituisce il percorso completo di un file, per esempio resource_path("assets/icon.ico")."""
    # Dentro l'.exe, PyInstaller scompatta i file in una cartella indicata da sys._MEIPASS
    base = getattr(sys, "_MEIPASS", None)
    if base is None:
        base = Path(__file__).parent       # esecuzione normale: la cartella di questo file
    return Path(base) / relativo
