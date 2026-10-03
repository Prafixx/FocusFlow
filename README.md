# FocusFlow

App desktop **gratuita** per organizzare la giornata: lista di attività (To-Do)
con categorie, timer Pomodoro, statistiche degli ultimi 7 giorni e tema chiaro/scuro.
Tutto in un'unica finestra, senza account e senza connessione internet.

Creata in **Python 3.13** con [CustomTkinter](https://github.com/tomschimansky/customtkinter)
come progetto per imparare Python da zero.

## Scarica e usa (Windows)

1. Vai nella sezione **Releases** di questo repository e scarica `FocusFlow-windows.zip`.
2. Estrai lo zip dove vuoi (tutta la cartella, non solo il file .exe).
3. Apri `FocusFlow\FocusFlow.exe`.

> Se Windows mostra "Windows ha protetto il PC": clicca **Ulteriori informazioni**
> e poi **Esegui comunque**. Succede perché l'app non ha una firma digitale a pagamento.

I tuoi dati restano nella cartella `C:\Users\<tuo nome>\FocusFlow`
(`tasks.json`, `settings.json`, `stats.json`). Per disinstallare basta cancellare
la cartella dell'app e, se vuoi, quella dei dati.

## Funzioni

- Aggiungi, completa, filtra ed elimina attività
- Timer Pomodoro (focus, pausa breve, pausa lunga ogni 4 pomodori) collegato ai task
- Durate personalizzabili e tema chiaro / scuro / di sistema
- Statistiche: pomodori di oggi, totale e grafico degli ultimi 7 giorni

## Avviarla dal codice

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Creare l'eseguibile

```
pip install -r requirements-dev.txt
build.bat
```

L'app finita si trova in `dist\FocusFlow\`.

## Struttura del progetto

| File | A cosa serve |
| --- | --- |
| `main.py` | punto di partenza dell'app grafica |
| `app.py` | finestra principale |
| `ui_tasks.py`, `ui_timer.py`, `ui_stats.py`, `ui_settings.py` | i quattro pannelli |
| `tasks.py` | classi `Task` e `TaskManager` |
| `pomodoro.py` | logica del timer (senza grafica) |
| `stats.py`, `settings.py`, `storage.py` | dati e file JSON |
| `cli.py` | la prima versione, a terminale |
