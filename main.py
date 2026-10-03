import time


from tasks import (
    nuovo_task, carica_task, salva_task,
    categorie_usate, statistiche,
)

APP_NAME = "FocusFlow"
VERSION = "0.11"

MENU = (
    "Aggiungere un task",
    "Mostrare i task",
    "Completare un task",
    "Rimuovere un task",
    "Mini-pomodoro su un task (5 secondi di prova)",
    "Mostrare le categorie usate",
)


# ---------- Funzioni di aiuto ----------

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


# ---------- Azioni sui task ----------

def mostra_task(tasks):
    if not tasks:
        print("La lista è vuota. Aggiungi il tuo primo task!")
        return
    print("\nI tuoi task:")
    for numero, task in enumerate(tasks, start=1):
        simbolo = "[x]" if task["fatto"] else "[ ]"
        print(f"  {numero}. {simbolo} {task['titolo']} ({task['categoria']}) "
              f"- pomodori: {task['pomodori']} - creato: {task['creato']}")


def scegli_task(tasks, domanda):
    if not tasks:
        print("Non hai ancora nessun task.")
        return None
    mostra_task(tasks)
    numero = chiedi_numero(domanda, 1, len(tasks))
    if numero is None:
        return None
    return tasks[numero - 1]


def aggiungi_task(tasks):
    titolo = chiedi_testo("Nome del task: ")
    if titolo == "":
        print("Non hai scritto niente: task non aggiunto.")
        return
    categoria = chiedi_testo("Categoria (Invio = Generale): ", "Generale")
    tasks.append(nuovo_task(titolo, categoria))
    print(f"Task aggiunto! Ora ne hai {len(tasks)}.")


def completa_task(tasks):
    task = scegli_task(tasks, "Numero del task completato: ")
    if task is not None:
        task["fatto"] = True
        print("Fatto! Bel lavoro.")


def rimuovi_task(tasks):
    task = scegli_task(tasks, "Numero del task da rimuovere: ")
    if task is not None:
        tasks.remove(task)
        print(f"Rimosso: {task['titolo']}")


def mini_pomodoro(tasks):
    task = scegli_task(tasks, "Su quale task ti concentri? ")
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
    task["pomodori"] += 1
    print("Pomodoro completato!")


def mostra_categorie(tasks):
    categorie = categorie_usate(tasks)
    if not categorie:
        print("Nessuna categoria: non hai ancora task.")
    else:
        print("Categorie usate:", ", ".join(sorted(categorie)))


# ---------- Programma principale ----------

def main():
    mostra_banner()
    nome = chiedi_testo("Come ti chiami? ", "amico")
    tasks = carica_task()
    print(f"Ho caricato {len(tasks)} task salvati.")

    try:
        while True:
            mostra_menu(nome)
            scelta = input("La tua scelta: ").strip()

            if scelta == "1":
                aggiungi_task(tasks)
                salva_task(tasks)
            elif scelta == "2":
                mostra_task(tasks)
            elif scelta == "3":
                completa_task(tasks)
                salva_task(tasks)
            elif scelta == "4":
                rimuovi_task(tasks)
                salva_task(tasks)
            elif scelta == "5":
                mini_pomodoro(tasks)
                salva_task(tasks)
            elif scelta == "6":
                mostra_categorie(tasks)
            elif scelta == "0":
                break
            else:
                print("Scelta non valida, riprova.")
    except (KeyboardInterrupt, EOFError):
        print("\nInterrotto dall'utente.")
    finally:
        totale, fatti, da_fare = statistiche(tasks)     
        print(f"A presto {nome}! Totale: {totale} | fatti: {fatti} | da fare: {da_fare}.")


if __name__ == "__main__":
    main()
