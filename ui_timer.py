# ui_timer.py  (Step 17)
# Il pannello del timer Pomodoro.
import customtkinter as ctk

import stats
import style
from pomodoro import PomodoroTimer

try:
    import winsound          # esiste solo su Windows
except ImportError:
    winsound = None

NESSUN_TASK = "Nessun task (focus libero)"


class TimerPanel(ctk.CTkFrame):
    def __init__(self, master, manager, settings, on_pomodoro=None):
        super().__init__(master, corner_radius=16, fg_color=style.CARD)
        self.manager = manager
        self.on_pomodoro = on_pomodoro        # callback: chiamata quando finisce un pomodoro
        self.timer = PomodoroTimer(settings["focus"], settings["pausa"], settings["lunga"])
        self._after_id = None                 # ricorda il "prossimo tick" programmato
        self.mappa_task = {}                  # testo del menu -> oggetto Task

        self.grid_columnconfigure(0, weight=1)

        titolo = ctk.CTkLabel(self, text="Timer Pomodoro", font=style.FONT_TITLE)
        titolo.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.task_menu = ctk.CTkOptionMenu(
            self, values=[NESSUN_TASK], height=36,
            fg_color=style.ROW, button_color=style.ROW, button_hover_color=style.MUTED,
            text_color=("gray10", "gray90"),
        )
        self.task_menu.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.fase_label = ctk.CTkLabel(self, text="FOCUS", font=("Roboto", 14, "bold"))
        self.fase_label.grid(row=2, column=0, pady=(10, 0))

        self.tempo_label = ctk.CTkLabel(self, text="25:00", font=("Roboto", 72, "bold"))
        self.tempo_label.grid(row=3, column=0, pady=(0, 5))

        self.barra = ctk.CTkProgressBar(self, height=10, progress_color=style.ACCENT)
        self.barra.set(0)
        self.barra.grid(row=4, column=0, padx=30, pady=(0, 15), sticky="ew")

        self.messaggio = ctk.CTkLabel(self, text="", font=style.FONT_SMALL, text_color=style.MUTED)
        self.messaggio.grid(row=5, column=0, pady=(0, 10))

        # --- bottoni ---
        bottoni = ctk.CTkFrame(self, fg_color="transparent")
        bottoni.grid(row=6, column=0, pady=(0, 10))

        self.avvia_button = ctk.CTkButton(
            bottoni, text="Avvia", width=110, height=40,
            fg_color=style.ACCENT, hover_color=style.ACCENT_HOVER,
            command=self.avvia_o_pausa,
        )
        self.avvia_button.grid(row=0, column=0, padx=5)

        ctk.CTkButton(
            bottoni, text="Reset", width=80, height=40,
            fg_color=style.ROW, hover_color=style.MUTED, text_color=("gray10", "gray90"),
            command=self.reset,
        ).grid(row=0, column=1, padx=5)

        ctk.CTkButton(
            bottoni, text="Salta", width=80, height=40,
            fg_color=style.ROW, hover_color=style.MUTED, text_color=("gray10", "gray90"),
            command=self.salta,
        ).grid(row=0, column=2, padx=5)

        self.oggi_label = ctk.CTkLabel(self, text="", font=style.FONT_TEXT)
        self.oggi_label.grid(row=7, column=0, pady=(10, 20))

        self.aggiorna_lista_task()
        self.aggiorna()

    # ---------- Bottoni ----------

    def avvia_o_pausa(self):
        if self.timer.in_corso:
            self.timer.ferma()
            self._ferma_tick()
        else:
            self.timer.avvia()
            self.messaggio.configure(text="")
            self._pianifica_tick()
        self.aggiorna()

    def reset(self):
        self._ferma_tick()
        self.timer.reset()
        self.messaggio.configure(text="")
        self.aggiorna()

    def salta(self):
        self._ferma_tick()
        self.timer.salta()
        self.messaggio.configure(text="")
        self.aggiorna()

    # ---------- Il "cuore": un tick ogni secondo ----------

    def _pianifica_tick(self):
        self._ferma_tick()
        # after(1000, funzione) = "tra 1000 millisecondi chiama questa funzione"
        self._after_id = self.after(1000, self._tick)

    def _ferma_tick(self):
        if self._after_id is not None:
            self.after_cancel(self._after_id)
            self._after_id = None

    def _tick(self):
        self._after_id = None
        fase_finita = self.timer.tick()
        if fase_finita is not None:
            self._fase_completata(fase_finita)
        if self.timer.in_corso:
            self._pianifica_tick()
        self.aggiorna()

    def _fase_completata(self, fase_finita):
        self._suona()
        if fase_finita == PomodoroTimer.FOCUS:
            stats.registra_pomodoro()
            task = self.mappa_task.get(self.task_menu.get())
            if task is not None and task in self.manager.tasks:
                self.manager.aggiungi_pomodoro(task)
            self.messaggio.configure(text="Pomodoro completato! Fai una pausa.")
        else:
            self.messaggio.configure(text="Pausa finita: pronto a ripartire?")
        if self.on_pomodoro is not None:
            self.on_pomodoro()

    def _suona(self):
        if winsound is not None:
            winsound.MessageBeep()      # il suono di sistema di Windows
        else:
            self.bell()                 # su altri sistemi: il "beep" di Tk

    # ---------- Aggiornamento della grafica ----------

    def aggiorna(self):
        """Allinea tutto quello che si vede con lo stato del timer."""
        fase = self.timer.fase
        colore = style.ACCENT if fase == PomodoroTimer.FOCUS else style.SUCCESS
        self.fase_label.configure(text=PomodoroTimer.NOMI[fase], text_color=colore)
        self.tempo_label.configure(text=self.timer.testo_tempo())
        self.barra.configure(progress_color=colore)
        self.barra.set(self.timer.progresso())
        self.avvia_button.configure(text="Pausa" if self.timer.in_corso else "Avvia")
        self.oggi_label.configure(text=f"Pomodori di oggi: {stats.pomodori_oggi()}")

    def aggiorna_lista_task(self):
        """Riempie il menu con i task ancora da fare."""
        scelta_precedente = self.task_menu.get()
        self.mappa_task = {}
        for numero, task in enumerate(self.manager.tasks, start=1):
            if not task.fatto:
                etichetta = f"{numero}. {task.titolo}"
                if len(etichetta) > 38:
                    etichetta = etichetta[:35] + "..."
                self.mappa_task[etichetta] = task
        valori = [NESSUN_TASK] + list(self.mappa_task.keys())
        self.task_menu.configure(values=valori)
        self.task_menu.set(scelta_precedente if scelta_precedente in valori else NESSUN_TASK)

    def applica_durate(self, settings):
        """Chiamata quando cambi le impostazioni."""
        self.timer.imposta_minuti(settings["focus"], settings["pausa"], settings["lunga"])
        self.aggiorna()
