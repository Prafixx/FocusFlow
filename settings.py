# settings.py
# Le impostazioni dell'app (durate del timer, tema), salvate in settings.json.
import storage

SETTINGS_FILE = "settings.json"

DEFAULTS = {
    "focus": 25,        # minuti di concentrazione
    "pausa": 5,         # minuti di pausa breve
    "lunga": 15,        # minuti di pausa lunga
    "tema": "system",   # "system", "light" oppure "dark"
}


def carica_settings():
    """Parte dai valori predefiniti e sovrascrive quelli trovati nel file."""
    settings = dict(DEFAULTS)                      # copia del dizionario
    salvate = storage.carica_json(SETTINGS_FILE, {})
    if isinstance(salvate, dict):                  # sicurezza: deve essere un dizionario
        settings.update(salvate)
    if settings["tema"] not in ("system", "light", "dark"):
        settings["tema"] = DEFAULTS["tema"]        # valore strano nel file? torna al predefinito
    return settings


def salva_settings(settings):
    storage.salva_json(SETTINGS_FILE, settings)
