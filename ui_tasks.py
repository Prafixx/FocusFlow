# ui_tasks.py  (Step 16)
# Il pannello dei task: aggiungi, spunta, elimina, filtra, pulisci.
import customtkinter as ctk

import style
from tasks import CATEGORIE_BASE

FILTRI = ("Tutte", "Da fare", "Fatte")


class TaskPanel(ctk.CTkFrame):
    def __init__(self, master, manager, on_change=None):
        super().__init__(master, corner_radius=16, fg_color=style.CARD)
        self.manager = manager
        self.on_change = on_change      # una funzione "da chiamare" quando i task cambiano (callback)
        self.filtro = "Tutte"

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # --- riga 0: titolo ---
        titolo = ctk.CTkLabel(self, text="Le tue attività", font=style.FONT_TITLE)
        titolo.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="w")

        # --- riga 1: casella di testo + categoria + bottone ---
        self.entry = ctk.CTkEntry(self, placeholder_text="Cosa devi fare?", height=40)
        self.entry.grid(row=1, column=0, padx=(20, 8), pady=(0, 10), sticky="ew")
        self.entry.bind("<Return>", self.on_add)

        self.categoria_menu = ctk.CTkOptionMenu(
            self, values=list(CATEGORIE_BASE), width=110, height=40,
            fg_color=style.ROW, button_color=style.ROW, button_hover_color=style.MUTED,
            text_color=("gray10", "gray90"),
        )
        self.categoria_menu.grid(row=1, column=1, padx=(0, 8), pady=(0, 10))

        self.add_button = ctk.CTkButton(
            self, text="Aggiungi", width=100, height=40,
            fg_color=style.ACCENT, hover_color=style.ACCENT_HOVER,
            command=self.on_add,
        )
        self.add_button.grid(row=1, column=2, padx=(0, 20), pady=(0, 10))

        # --- riga 2: filtri ---
        self.filtri = ctk.CTkSegmentedButton(
            self, values=list(FILTRI), command=self.on_filter,
            selected_color=style.ACCENT, selected_hover_color=style.ACCENT_HOVER,
        )
        self.filtri.set("Tutte")
        self.filtri.grid(row=2, column=0, columnspan=3, padx=20, pady=(0, 10), sticky="ew")

        # --- riga 3: la lista (con barra di scorrimento) ---
        self.lista = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.lista.grid(row=3, column=0, columnspan=3, padx=10, sticky="nsew")

        # --- riga 4: contatori e "pulisci" ---
        piede = ctk.CTkFrame(self, fg_color="transparent")
        piede.grid(row=4, column=0, columnspan=3, padx=20, pady=(5, 15), sticky="ew")
        piede.grid_columnconfigure(0, weight=1)

        self.contatore = ctk.CTkLabel(piede, text="", font=style.FONT_SMALL, text_color=style.MUTED)
        self.contatore.grid(row=0, column=0, sticky="w")

        self.pulisci_button = ctk.CTkButton(
            piede, text="Pulisci completate", width=140, height=30,
            fg_color="transparent", border_width=1, border_color=style.MUTED,
            text_color=style.MUTED, hover_color=style.ROW,
            command=self.on_pulisci,
        )
        self.pulisci_button.grid(row=0, column=1, sticky="e")

        self.refresh()

    # ---------- Eventi (cosa succede quando l'utente fa qualcosa) ----------

    def on_add(self, event=None):
        titolo = self.entry.get().strip()
        if titolo == "":
            return
        self.manager.aggiungi(titolo, self.categoria_menu.get())
        self.entry.delete(0, "end")
        self.aggiorna_tutto()

    def on_toggle(self, task):
        self.manager.cambia_stato(task)
        self.aggiorna_tutto()

    def on_delete(self, task):
        self.manager.rimuovi(task)
        self.aggiorna_tutto()

    def on_pulisci(self):
        self.manager.pulisci_completati()
        self.aggiorna_tutto()

    def on_filter(self, valore):
        self.filtro = valore
        self.refresh()

    def aggiorna_tutto(self):
        """Ridisegna la lista e avvisa chi ci ha chiesto di essere avvisato."""
        self.refresh()
        if self.on_change is not None:
            self.on_change()

    # ---------- Disegno ----------

    def task_visibili(self):
        if self.filtro == "Da fare":
            return [task for task in self.manager.tasks if not task.fatto]
        if self.filtro == "Fatte":
            return [task for task in self.manager.tasks if task.fatto]
        return list(self.manager.tasks)

    def refresh(self):
        for widget in self.lista.winfo_children():
            widget.destroy()

        visibili = self.task_visibili()
        if not visibili:
            testo = "Nessuna attività qui.\nAggiungine una nella casella in alto!"
            vuoto = ctk.CTkLabel(self.lista, text=testo, font=style.FONT_TEXT, text_color=style.MUTED)
            vuoto.pack(pady=50)
        for task in visibili:
            self.crea_riga(task)

        da_fare = self.manager.quanti_da_fare()
        fatti = self.manager.quanti_fatti()
        self.contatore.configure(text=f"{da_fare} da fare  ·  {fatti} completate")

    def crea_riga(self, task):
        riga = ctk.CTkFrame(self.lista, fg_color=style.ROW, corner_radius=10)
        riga.pack(fill="x", padx=6, pady=4)
        riga.grid_columnconfigure(0, weight=1)

        # Task fatto = testo barrato e grigio
        font = ctk.CTkFont(family="Roboto", size=15, overstrike=task.fatto)
        colore = style.MUTED if task.fatto else ("gray10", "gray90")
        casella = ctk.CTkCheckBox(
            riga, text=self.accorcia(task.titolo), font=font, text_color=colore,
            fg_color=style.SUCCESS, hover_color=style.SUCCESS_HOVER,
            command=lambda t=task: self.on_toggle(t),   # "t=task" ricorda QUALE task è
        )
        if task.fatto:
            casella.select()
        casella.grid(row=0, column=0, padx=(12, 6), pady=10, sticky="w")

        categoria = ctk.CTkLabel(riga, text=task.categoria, font=style.FONT_SMALL, text_color=style.MUTED)
        categoria.grid(row=0, column=1, padx=6)

        if task.pomodori > 0:
            parola = "pomodoro" if task.pomodori == 1 else "pomodori"
            conta = ctk.CTkLabel(
                riga, text=f"{task.pomodori} {parola}", font=style.FONT_SMALL, text_color=style.ACCENT,
            )
            conta.grid(row=0, column=2, padx=6)

        elimina = ctk.CTkButton(
            riga, text="×", width=30, height=30, font=("Roboto", 18),
            fg_color="transparent", text_color=style.MUTED, hover_color=("gray80", "gray30"),
            command=lambda t=task: self.on_delete(t),
        )
        elimina.grid(row=0, column=3, padx=(0, 8))

    @staticmethod
    def accorcia(testo, massimo=34):
        """Se il titolo è troppo lungo lo taglia e aggiunge '...'."""
        if len(testo) <= massimo:
            return testo
        return testo[:massimo - 3] + "..."
