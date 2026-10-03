# app.py  (Step 19)
# La finestra principale: intestazione, task a sinistra, schede (timer/statistiche/impostazioni) a destra.
import sys

import customtkinter as ctk

import style
from resources import resource_path
from settings import carica_settings
from tasks import TaskManager
from ui_settings import SettingsPanel
from ui_stats import StatsPanel
from ui_tasks import TaskPanel
from ui_timer import TimerPanel


class FocusFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=style.BG)

        self.manager = TaskManager()
        self.settings = carica_settings()
        ctk.set_appearance_mode(self.settings["tema"])     # il tema scelto l'ultima volta

        self.title("FocusFlow")
        self.geometry("1020x700")
        self.minsize(920, 620)
        self.imposta_icona()

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)

        # --- intestazione ---
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.grid(row=0, column=0, columnspan=2, padx=30, pady=(18, 0), sticky="ew")
        nome = ctk.CTkLabel(header, text="FocusFlow", font=("Roboto", 28, "bold"), text_color=style.ACCENT)
        nome.pack(side="left")
        sottotitolo = ctk.CTkLabel(header, text="to-do + pomodoro", font=style.FONT_TEXT, text_color=style.MUTED)
        sottotitolo.pack(side="left", padx=12, pady=(8, 0))

        # --- sinistra: i task ---
        self.tasks_panel = TaskPanel(self, self.manager, on_change=self.on_tasks_changed)
        self.tasks_panel.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")

        # --- destra: le schede ---
        self.tabs = ctk.CTkTabview(
            self, corner_radius=16, fg_color=style.CARD,
            segmented_button_selected_color=style.ACCENT,
            segmented_button_selected_hover_color=style.ACCENT_HOVER,
        )
        self.tabs.grid(row=1, column=1, padx=(10, 20), pady=(10, 20), sticky="nsew")
        for nome_scheda in ("Timer", "Statistiche", "Impostazioni"):
            self.tabs.add(nome_scheda)

        self.timer_panel = TimerPanel(
            self.tabs.tab("Timer"), self.manager, self.settings, on_pomodoro=self.on_pomodoro_done,
        )
        self.timer_panel.pack(fill="both", expand=True)

        self.stats_panel = StatsPanel(self.tabs.tab("Statistiche"), self.manager)
        self.stats_panel.pack(fill="both", expand=True)

        self.settings_panel = SettingsPanel(
            self.tabs.tab("Impostazioni"), self.settings, on_change=self.on_settings_changed,
        )
        self.settings_panel.pack(fill="both", expand=True)

    def imposta_icona(self):
        """Mette la nostra icona nella barra del titolo e nella barra delle applicazioni (Windows)."""
        if not sys.platform.startswith("win"):
            return
        percorso = resource_path("assets/icon.ico")
        if percorso.exists():
            # CustomTkinter mette la sua icona dopo ~200 ms: noi mettiamo la nostra subito dopo
            self.after(300, lambda: self.iconbitmap(str(percorso)))

    # ---------- Callback: i pannelli si "parlano" tramite la finestra ----------

    def on_tasks_changed(self):
        self.timer_panel.aggiorna_lista_task()
        self.stats_panel.aggiorna()

    def on_pomodoro_done(self):
        self.tasks_panel.refresh()
        self.stats_panel.aggiorna()

    def on_settings_changed(self):
        self.timer_panel.applica_durate(self.settings)
