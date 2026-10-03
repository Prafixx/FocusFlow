# ui_stats.py  (Step 18)
# Il pannello delle statistiche: numeri di oggi e grafico degli ultimi 7 giorni.
import customtkinter as ctk

import stats
import style

GIORNI = ("Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom")


class StatsPanel(ctk.CTkFrame):
    def __init__(self, master, manager):
        super().__init__(master, fg_color="transparent")
        self.manager = manager
        self.grid_columnconfigure(0, weight=1)

        titolo = ctk.CTkLabel(self, text="Statistiche", font=style.FONT_TITLE)
        titolo.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.oggi_numero = ctk.CTkLabel(self, text="0", font=("Roboto", 56, "bold"), text_color=style.ACCENT)
        self.oggi_numero.grid(row=1, column=0, pady=(10, 0))
        oggi_testo = ctk.CTkLabel(self, text="pomodori completati oggi", font=style.FONT_TEXT, text_color=style.MUTED)
        oggi_testo.grid(row=2, column=0)

        self.dettagli = ctk.CTkLabel(self, text="", font=style.FONT_TEXT, justify="center")
        self.dettagli.grid(row=3, column=0, pady=(15, 5))

        grafico_titolo = ctk.CTkLabel(self, text="Ultimi 7 giorni", font=style.FONT_SMALL, text_color=style.MUTED)
        grafico_titolo.grid(row=4, column=0, pady=(10, 0))

        # Il "grafico": 7 colonne, ognuna con numero, barra verticale e nome del giorno
        grafico = ctk.CTkFrame(self, fg_color="transparent")
        grafico.grid(row=5, column=0, pady=(5, 10))
        self.numeri, self.barre, self.nomi = [], [], []
        for colonna in range(7):
            numero = ctk.CTkLabel(grafico, text="0", font=style.FONT_SMALL)
            numero.grid(row=0, column=colonna, padx=7)
            barra = ctk.CTkProgressBar(
                grafico, orientation="vertical", width=16, height=110, progress_color=style.ACCENT,
            )
            barra.set(0)
            barra.grid(row=1, column=colonna, padx=7)
            nome = ctk.CTkLabel(grafico, text="", font=style.FONT_SMALL, text_color=style.MUTED)
            nome.grid(row=2, column=colonna, padx=7)
            self.numeri.append(numero)
            self.barre.append(barra)
            self.nomi.append(nome)

        self.aggiorna()

    def aggiorna(self):
        self.oggi_numero.configure(text=str(stats.pomodori_oggi()))
        self.dettagli.configure(
            text=f"Totale pomodori: {stats.pomodori_totali()}\n"
                 f"Task completati: {self.manager.quanti_fatti()} su {len(self.manager.tasks)}"
        )
        giorni = stats.ultimi_giorni(7)                      # lista di tuple (data, pomodori)
        massimo = max(1, max(n for _, n in giorni))          # il giorno "record" riempie la barra
        for i, (giorno, pomodori) in enumerate(giorni):
            self.numeri[i].configure(text=str(pomodori))
            self.barre[i].set(pomodori / massimo)
            self.nomi[i].configure(text=GIORNI[giorno.weekday()])
