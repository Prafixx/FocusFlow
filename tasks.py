# tasks.py  (Step 14: programmazione a oggetti)
# Due classi: Task (un singolo task) e TaskManager (la lista di tutti i task).
from datetime import date

import storage

TASKS_FILE = "tasks.json"
CATEGORIE_BASE = ("Generale", "Studio", "Lavoro", "Casa")


class Task:
    """Un singolo task (una cosa da fare)."""

    def __init__(self, titolo, categoria="Generale", fatto=False, pomodori=0, creato=None):
        # __init__ viene eseguito quando crei un Task: prepara i suoi "attributi"
        self.titolo = titolo
        self.categoria = categoria
        self.fatto = fatto
        self.pomodori = pomodori
        self.creato = creato or date.today().isoformat()   # se creato è vuoto, usa oggi

    def cambia_stato(self):
        """Da fare -> fatto, e viceversa."""
        self.fatto = not self.fatto

    def aggiungi_pomodoro(self):
        self.pomodori += 1

    def to_dict(self):
        """Trasforma il task in un dizionario (serve per salvarlo in JSON)."""
        return {
            "titolo": self.titolo,
            "categoria": self.categoria,
            "fatto": self.fatto,
            "pomodori": self.pomodori,
            "creato": self.creato,
        }

    def __str__(self):
        # __str__ decide come appare il task quando lo stampi con print()
        simbolo = "[x]" if self.fatto else "[ ]"
        return f"{simbolo} {self.titolo} ({self.categoria}) - pomodori: {self.pomodori} - creato: {self.creato}"


class TaskManager:
    """Gestisce l'elenco dei task e li salva su file ad ogni modifica."""

    def __init__(self):
        self.tasks = []
        self.carica()

    # --- salvataggio ---
    def carica(self):
        dati = storage.carica_json(TASKS_FILE, [])
        self.tasks = []
        for d in dati:
            self.tasks.append(Task(
                titolo=d.get("titolo", "(senza titolo)"),
                categoria=d.get("categoria", "Generale"),
                fatto=d.get("fatto", False),
                pomodori=d.get("pomodori", 0),
                creato=d.get("creato"),
            ))

    def salva(self):
        storage.salva_json(TASKS_FILE, [task.to_dict() for task in self.tasks])

    # --- azioni ---
    def aggiungi(self, titolo, categoria="Generale"):
        task = Task(titolo, categoria)
        self.tasks.append(task)
        self.salva()
        return task

    def rimuovi(self, task):
        self.tasks.remove(task)
        self.salva()

    def cambia_stato(self, task):
        task.cambia_stato()
        self.salva()

    def aggiungi_pomodoro(self, task):
        task.aggiungi_pomodoro()
        self.salva()

    def pulisci_completati(self):
        # lista nuova che contiene SOLO i task non ancora fatti
        self.tasks = [task for task in self.tasks if not task.fatto]
        self.salva()

    # --- domande sui dati ---
    def quanti_fatti(self):
        return len([task for task in self.tasks if task.fatto])

    def quanti_da_fare(self):
        return len(self.tasks) - self.quanti_fatti()

    def categorie(self):
        return {task.categoria for task in self.tasks}     # un set, senza doppioni
