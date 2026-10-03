# prova_gui.py
# Un piccolo esperimento per capire come funzionano le finestre. Non fa parte di FocusFlow.
import customtkinter as ctk

contatore = 0


def al_click():
    """Questa funzione viene chiamata ogni volta che premi il bottone."""
    global contatore                  # "global" = voglio modificare la variabile qui sopra
    contatore += 1
    etichetta.configure(text=f"Hai cliccato {contatore} volte")


finestra = ctk.CTk()                  # crea la finestra
finestra.title("Prova GUI")
finestra.geometry("320x180")          # larghezza x altezza in pixel

etichetta = ctk.CTkLabel(finestra, text="Non hai ancora cliccato", font=("Roboto", 16))
etichetta.pack(pady=(30, 10))         # pack = "metti il widget nella finestra"

bottone = ctk.CTkButton(finestra, text="Cliccami!", command=al_click)
bottone.pack(pady=10)

finestra.mainloop()                   # tiene la finestra aperta e ascolta i click
