# ui_settings.py  (Step 18)
# Il pannello delle impostazioni: durate del timer e tema chiaro/scuro.
import customtkinter as ctk

import style
from settings import salva_settings

# Testo mostrato nel pulsante -> valore salvato nel file
TEMI = {"Sistema": "system", "Chiaro": "light", "Scuro": "dark"}


class SettingsPanel(ctk.CTkFrame):
    def __init__(self, master, settings, on_change=None):
        super().__init__(master, fg_color="transparent")
        self.settings = settings
        self.on_change = on_change
        self.etichette = {}                 # chiave -> la label col valore (es. "focus" -> label)
        self.grid_columnconfigure(0, weight=1)

        titolo = ctk.CTkLabel(self, text="Impostazioni", font=style.FONT_TITLE)
        titolo.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        # Tre slider: (testo, chiave nel dizionario, minimo, massimo)
        righe = [
            ("Focus", "focus", 1, 60),
            ("Pausa breve", "pausa", 1, 30),
            ("Pausa lunga", "lunga", 5, 45),
        ]
        riga = 1
        for testo, chiave, minimo, massimo in righe:
            self.crea_slider(testo, chiave, minimo, massimo, riga)
            riga += 2

        tema_label = ctk.CTkLabel(self, text="Tema", font=style.FONT_TEXT)
        tema_label.grid(row=riga, column=0, padx=20, pady=(20, 5), sticky="w")

        self.tema_button = ctk.CTkSegmentedButton(
            self, values=list(TEMI.keys()), command=self.on_tema,
            selected_color=style.ACCENT, selected_hover_color=style.ACCENT_HOVER,
        )
        # Trova il testo giusto partendo dal valore salvato ("dark" -> "Scuro")
        for testo, valore in TEMI.items():
            if valore == self.settings["tema"]:
                self.tema_button.set(testo)
        self.tema_button.grid(row=riga + 1, column=0, padx=20, sticky="ew")

        aiuto = ctk.CTkLabel(
            self, text="Suggerimento: metti il focus a 1 minuto\nper provare il timer in fretta.",
            font=style.FONT_SMALL, text_color=style.MUTED, justify="left",
        )
        aiuto.grid(row=riga + 2, column=0, padx=20, pady=(25, 0), sticky="w")

    def crea_slider(self, testo, chiave, minimo, massimo, riga):
        label = ctk.CTkLabel(self, text="", font=style.FONT_TEXT)
        label.grid(row=riga, column=0, padx=20, pady=(15, 0), sticky="w")
        self.etichette[chiave] = label
        self.mostra_valore(testo, chiave, self.settings[chiave])

        slider = ctk.CTkSlider(
            self, from_=minimo, to=massimo, number_of_steps=massimo - minimo,
            progress_color=style.ACCENT, button_color=style.ACCENT, button_hover_color=style.ACCENT_HOVER,
            command=lambda valore, t=testo, k=chiave: self.on_slider(t, k, valore),
        )
        slider.set(self.settings[chiave])
        slider.grid(row=riga + 1, column=0, padx=20, pady=(5, 0), sticky="ew")

    def mostra_valore(self, testo, chiave, valore):
        self.etichette[chiave].configure(text=f"{testo}: {valore} min")

    def on_slider(self, testo, chiave, valore):
        minuti = int(round(valore))
        self.settings[chiave] = minuti
        self.mostra_valore(testo, chiave, minuti)
        salva_settings(self.settings)
        if self.on_change is not None:
            self.on_change()

    def on_tema(self, scelta):
        valore = TEMI[scelta]
        ctk.set_appearance_mode(valore)        # cambia subito l'aspetto di tutta l'app
        self.settings["tema"] = valore
        salva_settings(self.settings)
