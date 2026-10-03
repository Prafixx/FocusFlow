# pomodoro.py
# La LOGICA del timer Pomodoro. Nessuna finestra qui dentro: solo numeri e regole.
# (Tenere la logica separata dalla grafica rende tutto più semplice da capire e da testare.)


class PomodoroTimer:
    FOCUS = "focus"      # fase di concentrazione
    PAUSA = "pausa"      # pausa breve
    LUNGA = "lunga"      # pausa lunga (ogni 4 pomodori)

    NOMI = {FOCUS: "FOCUS", PAUSA: "PAUSA BREVE", LUNGA: "PAUSA LUNGA"}

    def __init__(self, focus=25, pausa=5, lunga=15):
        # Un dizionario: per ogni fase, quanti MINUTI dura
        self.minuti = {self.FOCUS: focus, self.PAUSA: pausa, self.LUNGA: lunga}
        self.fase = self.FOCUS
        self.in_corso = False          # il timer sta contando?
        self.completati = 0            # pomodori completati in questa sessione
        self.secondi_rimasti = self.durata_fase()

    def durata_fase(self):
        """Durata della fase attuale, in secondi."""
        return self.minuti[self.fase] * 60

    def imposta_minuti(self, focus, pausa, lunga):
        """Cambia le durate. Se il timer è fermo, aggiorna anche il tempo mostrato."""
        self.minuti = {self.FOCUS: focus, self.PAUSA: pausa, self.LUNGA: lunga}
        if not self.in_corso:
            self.secondi_rimasti = self.durata_fase()

    def avvia(self):
        self.in_corso = True

    def ferma(self):
        self.in_corso = False

    def reset(self):
        """Torna all'inizio della fase attuale."""
        self.in_corso = False
        self.secondi_rimasti = self.durata_fase()

    def salta(self):
        """Passa alla fase successiva senza contare il pomodoro."""
        self._prossima_fase(conta_pomodoro=False)

    def tick(self):
        """Va chiamata ogni secondo. Restituisce la fase appena finita, oppure None."""
        if not self.in_corso:
            return None
        self.secondi_rimasti -= 1
        if self.secondi_rimasti > 0:
            return None
        fase_finita = self.fase
        self._prossima_fase(conta_pomodoro=True)
        return fase_finita

    def _prossima_fase(self, conta_pomodoro):
        # Il "_" iniziale dice: questo metodo è per uso interno della classe
        if self.fase == self.FOCUS:
            lunga = False
            if conta_pomodoro:
                self.completati += 1
                lunga = (self.completati % 4 == 0)     # ogni 4 pomodori: pausa lunga
            self.fase = self.LUNGA if lunga else self.PAUSA
        else:
            self.fase = self.FOCUS
        self.in_corso = False                          # a fine fase si ferma: premi Avvia
        self.secondi_rimasti = self.durata_fase()

    def progresso(self):
        """Numero da 0.0 a 1.0: quanto della fase è già passato."""
        totale = self.durata_fase()
        if totale == 0:
            return 0.0
        return 1 - self.secondi_rimasti / totale

    def testo_tempo(self):
        """Il tempo rimasto come testo, per esempio '24:59'."""
        minuti, secondi = divmod(self.secondi_rimasti, 60)
        return f"{minuti:02d}:{secondi:02d}"
