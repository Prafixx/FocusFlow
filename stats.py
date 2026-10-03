# stats.py
# Statistiche: quanti pomodori hai completato ogni giorno (in stats.json).
from datetime import date, timedelta

import storage

STATS_FILE = "stats.json"


def carica_stats():
    """Restituisce un dizionario come {"2026-10-02": 3, "2026-10-01": 5}."""
    dati = storage.carica_json(STATS_FILE, {})
    return dati if isinstance(dati, dict) else {}


def registra_pomodoro():
    """Aggiunge 1 ai pomodori di oggi."""
    dati = carica_stats()
    oggi = date.today().isoformat()
    dati[oggi] = dati.get(oggi, 0) + 1
    storage.salva_json(STATS_FILE, dati)


def pomodori_oggi():
    return carica_stats().get(date.today().isoformat(), 0)


def pomodori_totali():
    return sum(carica_stats().values())


def ultimi_giorni(quanti=7):
    """Lista di tuple (data, pomodori) degli ultimi giorni, dal più vecchio a oggi."""
    dati = carica_stats()
    oggi = date.today()
    risultato = []
    for indietro in range(quanti - 1, -1, -1):
        giorno = oggi - timedelta(days=indietro)
        risultato.append((giorno, dati.get(giorno.isoformat(), 0)))
    return risultato
