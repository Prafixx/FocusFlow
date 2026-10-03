# main.py  (Step 14: classi) - l'interfaccia "a testo" di FocusFlow
import time

from tasks import TaskManager

APP_NAME = "FocusFlow"
VERSION = "0.14"

MENU = (
    "Aggiungere un task",
    "Mostrare i task",
    "Completare / riaprire un task",
    "Rimuovere un task",
    "Mini-pomodoro su un task (5 secondi di prova)",
    "Mostrare le categorie usate",
    "Eliminare tutti i task completati",
)


def mostra_banner():
    print("=" * 40)
    print(f"   {APP_NAME} v{VERSION}")
    print("=" * 40)


def chiedi_testo(domanda, predefinito=""):
    risposta = input(domanda).strip()
    if risposta == "":
        return predefinito
    return risposta


def chiedi_numero(domanda, minimo, massimo):
    try:
        numero = int(input(domanda))
    except ValueError:
        print("Devi scrivere un numero intero (per esempio 3).")
        return None
    if numero < minimo or numero > massimo:
        print(f"Il numero deve essere tra {minimo} e {massimo}.")
        return None
    return numero


def mostra_menu(nome):
    print(f"\n--- Menu di {nome} ---")
    for numero, voce in enumerate(MENU, start=1):
        print(f"{numero}) {voce}")
    print("0) Uscire")


def mostra_task(manager):
    if not manager.tasks:
        print("La lista è vuota. Aggiungi il tuo primo task!")
        return
    print("\nI tuoi task:")
    for numero, task in enumerate(manager.tasks, start=1):
        print(f"  {numero}. {task}")          # print(task) usa il metodo __str__


def scegli_task(manager, domanda):
    if not manager.tasks:
        print("Non hai ancora nessun task.")
        return None
    mostra_task(manager)
    numero = chiedi_numero(domanda, 1, len(manager.tasks))
    if numero is None:
        return None
    return manager.tasks[numero - 1]


def aggiungi_task(manager):
    titolo = chiedi_testo("Nome del task: ")
    if titolo == "":
        print("Non hai scritto niente: task non aggiunto.")
        return
    categoria = chiedi_testo("Categoria (Invio = Generale): ", "Generale")
    manager.aggiungi(titolo, categoria)
    print(f"Task aggiunto! Ora ne hai {len(manager.tasks)}.")


def cambia_stato_task(manager):
    task = scegli_task(manager, "Numero del task: ")
    if task is not None:
        manager.cambia_stato(task)
        print("Fatto! Bel lavoro." if task.fatto else "Task riaperto.")


def rimuovi_task(manager):
    task = scegli_task(manager, "Numero del task da rimuovere: ")
    if task is not None:
        manager.rimuovi(task)
        print(f"Rimosso: {task.titolo}")


def mini_pomodoro(manager):
    task = scegli_task(manager, "Su quale task ti concentri? ")
    if task is None:
        return
    print("Concentrazione! (premi Ctrl+C per interrompere)")
    try:
        for secondi in range(5, 0, -1):
            print(f"  {secondi}...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPomodoro interrotto: non viene conteggiato.")
        return
    manager.aggiungi_pomodoro(task)
    print("Pomodoro completato!")


def mostra_categorie(manager):
    categorie = manager.categorie()
    if not categorie:
        print("Nessuna categoria: non hai ancora task.")
    else:
        print("Categorie usate:", ", ".join(sorted(categorie)))


def main():
    mostra_banner()
    nome = chiedi_testo("Come ti chiami? ", "amico")
    manager = TaskManager()                      # crea il gestore: carica da solo i task salvati
    print(f"Ho caricato {len(manager.tasks)} task salvati.")

    try:
        while True:
            mostra_menu(nome)
            scelta = input("La tua scelta: ").strip()

            if scelta == "1":
                aggiungi_task(manager)
            elif scelta == "2":
                mostra_task(manager)
            elif scelta == "3":
                cambia_stato_task(manager)
            elif scelta == "4":
                rimuovi_task(manager)
            elif scelta == "5":
                mini_pomodoro(manager)
            elif scelta == "6":
                mostra_categorie(manager)
            elif scelta == "7":
                manager.pulisci_completati()
                print("Task completati eliminati.")
            elif scelta == "0":
                break
            else:
                print("Scelta non valida, riprova.")
    except (KeyboardInterrupt, EOFError):
        print("\nInterrotto dall'utente.")
    finally:
        print(f"A presto {nome}! Da fare: {manager.quanti_da_fare()} | fatti: {manager.quanti_fatti()}.")


if __name__ == "__main__":
    main()
