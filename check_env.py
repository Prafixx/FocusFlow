# check_env.py
# Controlla se stai usando l'ambiente virtuale giusto e se le librerie sono installate.
import sys

print("Python:", sys.version.split()[0])
print("Eseguibile:", sys.executable)

# Dentro un ambiente virtuale, sys.prefix è diverso da sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print("Ambiente virtuale attivo?", "SÌ" if in_venv else "NO")

try:
    import customtkinter
    print("customtkinter:", customtkinter.__version__)
except ImportError:
    print("customtkinter: NON installato (esegui: pip install -r requirements.txt)")
