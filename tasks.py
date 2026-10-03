from datetime import date     

import storage                

TASKS_FILE = "tasks.json"
CATEGORIE_BASE = ("Generale", "Studio", "Lavoro", "Casa")


def nuovo_task(titolo, categoria="Generale"):
    """Crea un nuovo task (un dizionario)."""
    return {
        "titolo": titolo,
        "categoria": categoria,
        "fatto": False,
        "pomodori": 0,
        "creato": date.today().isoformat(),    
    }


def carica_task():
    """Legge i task dal file. Se mancano delle chiavi, mette valori predefiniti."""
    dati = storage.carica_json(TASKS_FILE, [])
    tasks = []
    for d in dati:
        
        tasks.append({
            "titolo": d.get("titolo", "(senza titolo)"),
            "categoria": d.get("categoria", "Generale"),
            "fatto": d.get("fatto", False),
            "pomodori": d.get("pomodori", 0),
            "creato": d.get("creato", ""),
        })
    return tasks


def salva_task(tasks):
    storage.salva_json(TASKS_FILE, tasks)


def conta_fatti(tasks):
    fatti = 0
    for task in tasks:
        if task["fatto"]:
            fatti += 1
    return fatti


def statistiche(tasks):
    """Restituisce una TUPLA: (totale, fatti, da_fare)."""
    totale = len(tasks)
    fatti = conta_fatti(tasks)
    return totale, fatti, totale - fatti


def categorie_usate(tasks):
    """Restituisce un SET con le categorie usate (senza doppioni)."""
    categorie = set()
    for task in tasks:
        categorie.add(task["categoria"])
    return categorie