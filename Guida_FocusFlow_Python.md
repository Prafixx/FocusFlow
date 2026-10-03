# FocusFlow — Impara Python costruendo un'app vera

*Guida completa per principianti assoluti · Windows · da zero all'eseguibile (.exe)*

> **Come aprire questo file:** apri il file `.md` con VS Code (dopo averlo installato allo Step 1) e premi **Ctrl+Shift+V**: vedrai la guida ben formattata, con indice cliccabile. Puoi leggerla e seguirla **offline**: tutto il codice è già dentro, pronto da copiare.

## Cosa costruirai

**FocusFlow**: un'app per Windows con interfaccia grafica moderna che ti aiuta nella giornata di tutti i giorni:

- una **lista di attività (To-Do)** con categorie, filtri e spunte;
- un **timer Pomodoro** (25 minuti di concentrazione, 5 di pausa, pausa lunga ogni 4 pomodori) collegato alle tue attività;
- **statistiche** dei pomodori di oggi e degli ultimi 7 giorni;
- **tema chiaro / scuro**, impostazioni salvate, dati salvati su file;
- un **eseguibile `.exe`** che puoi copiare su un altro PC **senza installare Python**.

Tutto con strumenti e librerie **gratuiti**. Impari Python *costruendo* l'app: ogni step aggiunge un pezzo, e parte dal codice dello step precedente.

## Versioni usate

| Strumento | Versione | Note |
| --- | --- | --- |
| Python | **3.13.x** (a ottobre 2026: 3.13.16) | installer classico da python.org |
| CustomTkinter | **6.0.x** | interfaccia grafica moderna (gratuita) |
| PyInstaller | **6.22.x** | crea l'eseguibile |
| Pillow | **12.x** | disegna l'icona dell'app |
| VS Code, Git per Windows | ultima versione | gratuiti |

**Cosa è stato verificato.** Tutto il codice Python di questa guida è stato eseguito e controllato con Python 3.13: i programmi a terminale, la logica del timer, l'interfaccia grafica (anche con prove automatiche e schermate di controllo) e la creazione dell'eseguibile con PyInstaller. Il collaudo è avvenuto in un ambiente di prova **Linux**, non su un PC Windows: le parti proprie di Windows (installer, PowerShell, suono di sistema, icona `.ico`, `build.bat`) seguono la documentazione ufficiale ma non ho potuto provarle di persona. Se qualcosa non torna, vai alla sezione **Se mi blocco**.

## Come funziona ogni step

Ogni step ha sempre le stesse parti, nello stesso ordine:

1. **Obiettivo** dello step, in una frase.
2. **Concetti in 2 minuti**: la teoria minima, spiegata *prima* di usarla.
3. **Dove lavori**: il nome esatto del file e dove incollare il codice.
4. **Il codice** completo, con commenti, pronto da copiare.
5. **Cosa fa questo codice**: spiegazione a blocchi.
6. **Come eseguirlo**: il comando esatto e cosa devi vedere.
7. **Errori comuni** di quello step e come risolverli.
8. **Esercizio**: un piccolo esercizio da fare da solo (le soluzioni sono in fondo alla guida).
9. **Il progetto finora**: cosa si è aggiunto a FocusFlow.

**Convenzioni.** I blocchi `python` sono codice da incollare nei file. I blocchi `powershell` sono comandi da scrivere nel **terminale** di VS Code (la finestra dei comandi, che vedrai allo Step 1): non scrivere il `PS C:\...>` iniziale, solo il comando.

## Come studiare (7–10 ore a settimana)

1. **Copia, esegui, poi cambia qualcosa.** Dopo che il codice funziona, modifica un testo o un numero e rilancia: è così che si impara davvero.
2. **Salva sempre prima di avviare** (Ctrl+S). Un pallino bianco nel titolo della scheda significa "non salvato".
3. **Gli errori sono normali.** Python ti dice cosa non va: leggi l'ultima riga del messaggio (lo spiego bene allo Step 9).
4. **Non saltare gli esercizi**: sono corti e fissano le idee.
5. **Dallo Step 13 in poi, fai un commit Git a fine step**: è la tua rete di sicurezza.

## Piano settimanale

| Settimana | Step | Cosa ottieni |
| --- | --- | --- |
| 1 | 1 – 5 | Python installato, programma a menu con cicli e condizioni |
| 2 | 6 – 10 | Task in liste e dizionari, funzioni, errori, **salvataggio su file** |
| 3 | 11 – 14 | Progetto in moduli, ambiente virtuale, Git/GitHub, classi (OOP) |
| 4 | 15 – 16 | **Prima finestra grafica**, lista task completa |
| 5 | 17 – 18 | Timer Pomodoro, statistiche, impostazioni, tema scuro |
| 6 | 19 – 20 | Icona, **eseguibile**, distribuzione su GitHub |

Gli step durano circa 1–2 ore ciascuno. Se una settimana salti, nessun problema: la guida si riprende da dove sei.

## Mappa degli argomenti

| Argomento | Dove lo trovi |
| --- | --- |
| Installare Python e VS Code | Step 1 |
| Variabili e tipi di dato | Step 2 |
| Input e output | Step 3 |
| Condizioni (`if`) | Step 4 |
| Cicli (`while`, `for`) | Step 5 |
| Liste e tuple | Step 6 |
| Dizionari e set | Step 7 |
| Funzioni | Step 8 |
| Gestione degli errori | Step 9 |
| File (testo e JSON) | Step 10 |
| Moduli | Step 11 |
| Ambienti virtuali e pip | Step 12 |
| Git e GitHub | Step 13 |
| Programmazione a oggetti (OOP) | Step 14 |
| Interfaccia grafica | Step 15 – 18 |
| Creare l'eseguibile | Step 19 – 20 |

## Struttura finale del progetto

Alla fine la tua cartella `FocusFlow` conterrà questi file (non devi crearli ora: nascono step dopo step):

```text
FocusFlow/
├── main.py              # avvia l'app grafica
├── app.py               # finestra principale
├── ui_tasks.py          # pannello dei task
├── ui_timer.py          # pannello del timer
├── ui_stats.py          # pannello delle statistiche
├── ui_settings.py       # pannello delle impostazioni
├── style.py             # colori e font
├── tasks.py             # classi Task e TaskManager
├── pomodoro.py          # logica del timer (senza grafica)
├── stats.py             # statistiche giornaliere
├── settings.py          # impostazioni salvate
├── storage.py           # lettura/scrittura file JSON
├── resources.py         # trova icona e file dentro l'.exe
├── make_icon.py         # disegna l'icona
├── cli.py               # la versione a terminale (archivio)
├── build.bat            # crea l'eseguibile
├── check_env.py         # controlla ambiente virtuale e librerie
├── requirements.txt     # librerie necessarie
├── requirements-dev.txt # librerie per costruire l'.exe
├── README.md            # presentazione del progetto
├── .gitignore           # cosa Git deve ignorare
├── assets/              # icon.ico e icon.png
└── esercizi/            # i tuoi esercizi
```

Intanto i **dati dell'app** (task, impostazioni, statistiche) vivranno fuori dal progetto, in `C:\Users\TuoNome\FocusFlow\`.

## Indice


**[PARTE A — Le fondamenta: Python da terminale (step 1–10)](#parte-a--le-fondamenta-python-da-terminale-step-110)**

- [Step 1 — Installare Python e VS Code, e il primo programma](#step-1--installare-python-e-vs-code-e-il-primo-programma)
- [Step 2 — Variabili e tipi di dato](#step-2--variabili-e-tipi-di-dato)
- [Step 3 — Input e output](#step-3--input-e-output)
- [Step 4 — Condizioni (`if`, `elif`, `else`)](#step-4--condizioni-if-elif-else)
- [Step 5 — Cicli (`while`, `for`)](#step-5--cicli-while-for)
- [Step 6 — Liste e tuple](#step-6--liste-e-tuple)
- [Step 7 — Dizionari e set](#step-7--dizionari-e-set)
- [Step 8 — Funzioni](#step-8--funzioni)
- [Step 9 — Gestione degli errori](#step-9--gestione-degli-errori)
- [Step 10 — File: salvare e caricare i dati (JSON)](#step-10--file-salvare-e-caricare-i-dati-json)

**[PARTE B — Organizzare il progetto (step 11–14)](#parte-b--organizzare-il-progetto-step-1114)**

- [Step 11 — Moduli: dividere il programma in più file](#step-11--moduli-dividere-il-programma-in-più-file)
- [Step 12 — Ambienti virtuali e pip](#step-12--ambienti-virtuali-e-pip)
- [Step 13 — Git e GitHub](#step-13--git-e-github)
- [Step 14 — Programmazione a oggetti (OOP): le classi `Task` e `TaskManager`](#step-14--programmazione-a-oggetti-oop-le-classi-task-e-taskmanager)

**[PARTE C — L'app grafica (step 15–18)](#parte-c--lapp-grafica-step-1518)**

- [Step 15 — La prima finestra: aggiungere e mostrare i task](#step-15--la-prima-finestra-aggiungere-e-mostrare-i-task)
- [Step 16 — Task completabili, eliminabili e filtrabili](#step-16--task-completabili-eliminabili-e-filtrabili)
- [Step 17 — Il timer Pomodoro](#step-17--il-timer-pomodoro)
- [Step 18 — Impostazioni, statistiche e tema scuro](#step-18--impostazioni-statistiche-e-tema-scuro)

**[PARTE D — Dall'app all'eseguibile (step 19–20)](#parte-d--dallapp-alleseguibile-step-1920)**

- [Step 19 — Icona ed eseguibile (`.exe`) con PyInstaller](#step-19--icona-ed-eseguibile-exe-con-pyinstaller)
- [Step 20 — Distribuire FocusFlow: zip, prova su un altro PC e GitHub Releases](#step-20--distribuire-focusflow-zip-prova-su-un-altro-pc-e-github-releases)
- [Soluzioni degli esercizi](#soluzioni-degli-esercizi)
- [Se mi blocco](#se-mi-blocco)
- [Checklist finale: cosa hai imparato](#checklist-finale-cosa-hai-imparato)


---

# PARTE A — Le fondamenta: Python da terminale (step 1–10)

In questa parte costruisci la versione "a testo" di FocusFlow: niente finestre, solo il terminale. Qui impari le basi vere di Python. Tutto ciò che scrivi servirà anche per l'app grafica.

## Step 1 — Installare Python e VS Code, e il primo programma

**Obiettivo:** preparare il PC e far girare il tuo primo programma Python.

### Concetti in 2 minuti

- **Python** è il linguaggio di programmazione; il **programma `python`** è l'interprete: legge il tuo file e lo esegue riga per riga.
- **VS Code** (Visual Studio Code) è l'editor gratuito in cui scrivi il codice.
- Il **terminale** è la finestra in cui scrivi comandi. In VS Code è già incorporato.
- **PATH** è l'elenco di cartelle in cui Windows cerca i programmi quando scrivi un comando. Se Python è nel PATH, il comando `python` funziona da qualsiasi cartella.

### A. Installa Python

1. Apri <https://www.python.org/downloads/windows/>.
2. Cerca **Python 3.13.x** (la più recente della serie 3.13; a ottobre 2026 è la 3.13.16) e clicca **Windows installer (64-bit)**.
   *Nota:* la pagina propone anche Python 3.14 tramite il "Python install manager". Funziona, ma per imparare è più semplice l'installer classico, e le librerie di questa guida sono state verificate con la 3.13.
3. Avvia il file scaricato. Nella prima schermata **spunta "Add python.exe to PATH"** (in basso: è la cosa più importante di tutta l'installazione). Poi clicca **Install Now**.
4. A fine installazione, se compare **"Disable path length limit"**, cliccalo (evita problemi coi percorsi lunghi) e poi **Close**.

### B. Installa VS Code

1. Vai su <https://code.visualstudio.com>, scarica la versione per Windows e installala. Nella schermata "Select Additional Tasks" lascia spuntato **Add to PATH** e le due voci **"Apri con Code"**.
2. Apri VS Code. Premi **Ctrl+Shift+X** (Estensioni), cerca **Python** (autore *Microsoft*) e clicca **Installa**.
3. *Facoltativo:* installa anche **Italian Language Pack for Visual Studio Code** per avere i menu in italiano (in questa guida uso i nomi italiani).

### C. Crea la cartella del progetto

1. In Esplora file vai in `C:\Users\TuoNome`, crea la cartella **Progetti** e dentro di essa la cartella **FocusFlow**. Evita Desktop e Documenti: spesso sono sincronizzati con OneDrive e danno problemi coi file temporanei.
2. In VS Code: **File → Apri cartella…** → scegli `FocusFlow` → conferma **"Sì, mi fido degli autori"**.
3. Nel pannello **Esplora risorse** a sinistra, passa il mouse sul nome della cartella e clicca l'icona **Nuovo file**: chiamalo `focusflow.py`.
4. Apri il terminale: menu **Terminale → Nuovo terminale**. Appare in basso; il prompt mostra la cartella (per esempio `PS C:\Users\Marco\Progetti\FocusFlow>`). Scrivi:

```powershell
python --version
```

Devi vedere qualcosa come `Python 3.13.16`.

### Dove lavori

Il file **`focusflow.py`**, nella cartella `FocusFlow`. Incolla tutto il codice qui sotto e salva con **Ctrl+S**.

### Il codice

```python
# focusflow.py
# Il mio primo programma Python: il "biglietto da visita" di FocusFlow.

print("=" * 40)
print("   FOCUSFLOW")
print("   To-Do + Pomodoro")
print("=" * 40)
print("Ciao! Il tuo primo programma Python funziona.")
```

### Cosa fa questo codice

- Le righe che iniziano con `#` sono **commenti**: Python le ignora, servono a te.
- `print("...")` scrive un testo sullo schermo. Il testo tra virgolette si chiama **stringa**.
- `"=" * 40` ripete il carattere `=` per 40 volte: così disegniamo una riga.

### Come eseguirlo

Nel terminale, nella cartella del progetto:

```powershell
python focusflow.py
```

Se funziona vedrai:

```text
========================================
   FOCUSFLOW
   To-Do + Pomodoro
========================================
Ciao! Il tuo primo programma Python funziona.
```

(In alternativa puoi cliccare il triangolo **▷ Run Python File** in alto a destra nell'editor.)

### Errori comuni

- **`python` non è riconosciuto**, oppure si apre il Microsoft Store: durante l'installazione non avevi spuntato "Add python.exe to PATH". Reinstalla Python (rilancia l'installer e scegli *Modify*/ripara) spuntandolo. Se si apre lo Store, vai in *Impostazioni → App → Impostazioni app avanzate → Alias di esecuzione app* e disattiva `python.exe` e `python3.exe`. Poi **chiudi e riapri VS Code**. Come ripiego prova `py focusflow.py`.
- **`can't open file ... No such file or directory`**: sei in una cartella diversa o il nome del file è sbagliato. Controlla il prompt e scrivi `dir` per vedere i file presenti.
- **Vedi ancora il vecchio risultato**: non hai salvato (pallino nella scheda). Premi Ctrl+S.
- **`SyntaxError: unterminated string literal`**: hai dimenticato una virgoletta. Python ti indica anche la riga.
- **Lettere strane (`Ã¨` al posto di `è`)**: il file deve essere salvato in UTF-8, che è l'impostazione normale di VS Code.

### Esercizio

Crea la cartella `esercizi` dentro il progetto e dentro un file `esercizi\step01.py`. Fagli stampare un riquadro di asterischi con dentro **il tuo nome** e la frase *"Sto imparando Python!"*. Eseguilo con `python esercizi\step01.py`. *(Soluzione in fondo.)*

### Il progetto finora

Hai `focusflow.py` con il biglietto da visita di FocusFlow. Da qui fino allo Step 10 **lavori sempre su questo file**, che cresce a ogni step.

---

## Step 2 — Variabili e tipi di dato

**Obiettivo:** memorizzare informazioni (il nome dell'app, la durata del pomodoro…) e capire che tipo di informazione sono.

### Concetti in 2 minuti

- Una **variabile** è una scatola con un'etichetta: dentro c'è un valore. Si crea con `=`: `pomodoro_minuti = 25` significa "metti 25 nella scatola `pomodoro_minuti`". Attenzione: `=` **assegna**, non confronta.
- I **nomi** si scrivono in minuscolo con il trattino basso (`ore_di_studio`), senza spazi né accenti. Python distingue maiuscole e minuscole: `Nome` e `nome` sono variabili diverse. Per i valori che non cambiano mai si usa il MAIUSCOLO (`APP_NAME`): è solo una convenzione, ma aiuta a leggere.
- I **tipi di dato** principali:
  - `str` (stringa): testo, tra virgolette → `"Ciao"`
  - `int`: numero intero → `25`
  - `float`: numero con la virgola (si scrive col **punto**) → `1.5`
  - `bool`: vero o falso → `True` / `False` (la prima lettera è maiuscola)
- Una **f-string** è un testo che inizia con `f` e può contenere variabili tra graffe: `f"Ciao {nome}"`.

### Dove lavori

Sempre **`focusflow.py`**: **cancella tutto il contenuto** e incolla questo.

### Il codice

```python
# focusflow.py  (Step 2: variabili e tipi di dato)

# --- Dati dell'app (le variabili) ---
APP_NAME = "FocusFlow"            # str: testo
VERSION = "0.2"                   # str: anche i numeri di versione sono testo
pomodoro_minuti = 25              # int: numero intero
pausa_minuti = 5                  # int
primo_task = "Installare Python"  # str
task_completato = False           # bool: vero/falso (True o False)
ore_di_studio = 1.5               # float: numero con la virgola

# --- Calcoli ---
ciclo_totale = pomodoro_minuti + pausa_minuti

# --- Output ---
print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)
print(f"Il tuo primo task: {primo_task}")
print(f"Completato? {task_completato}")
print(f"Un pomodoro dura {pomodoro_minuti} minuti, poi {pausa_minuti} di pausa.")
print(f"Un ciclo completo dura {ciclo_totale} minuti.")
print(f"Oggi vuoi studiare {ore_di_studio} ore.")

# type() ci dice di che tipo è una variabile
print()
print("--- I tipi delle variabili ---")
print("primo_task      ->", type(primo_task))
print("pomodoro_minuti ->", type(pomodoro_minuti))
print("ore_di_studio   ->", type(ore_di_studio))
print("task_completato ->", type(task_completato))
```

### Cosa fa questo codice

- **Variabili**: le prime righe creano le scatole con i loro valori; i commenti a destra indicano il tipo.
- **Calcolo**: `pomodoro_minuti + pausa_minuti` somma due numeri (operatori: `+ - * /`).
- **f-string**: dentro `print(f"...")` le parti tra `{}` vengono sostituite dal valore delle variabili.
- **`type(...)`** restituisce il tipo di una variabile: ti serve quando non sei sicuro di cosa contenga.

### Come eseguirlo

```powershell
python focusflow.py
```

Devi vedere:

```text
========================================
   FocusFlow v0.2
========================================
Il tuo primo task: Installare Python
Completato? False
Un pomodoro dura 25 minuti, poi 5 di pausa.
Un ciclo completo dura 30 minuti.
Oggi vuoi studiare 1.5 ore.

--- I tipi delle variabili ---
primo_task      -> <class 'str'>
pomodoro_minuti -> <class 'int'>
ore_di_studio   -> <class 'float'>
task_completato -> <class 'bool'>
```

### Errori comuni

- **`NameError: name 'primo_task' is not defined`**: hai usato una variabile prima di crearla, oppure l'hai scritta in modo diverso (maiuscole, trattino basso). Controlla il nome riga per riga.
- **`SyntaxError`** con una f-string: dimentichi la `f` davanti alle virgolette, e allora vedi `{primo_task}` stampato così com'è.
- **`TypeError: can only concatenate str (not "int") to str`**: stai sommando un testo e un numero con `+`. Usa una f-string.
- **Il decimale con la virgola** (`1,5`) non funziona: in Python si scrive `1.5`.

### Esercizio

In `esercizi\step02.py`: crea le variabili `pomodori = 4`, `minuti_focus = 25`, `minuti_pausa = 5`. Calcola i **minuti totali** di 4 pomodori con **3 pause** in mezzo (dopo l'ultimo non serve) e le **ore** con due decimali (suggerimento: `{ore:.2f}` dentro la f-string). Stampa anche il tipo dei due risultati. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow ora "conosce" i suoi dati di base: nome, versione, durate di pomodoro e pausa, un primo task (come variabili).

---

## Step 3 — Input e output

**Obiettivo:** far dialogare il programma con te: fare domande, leggere le risposte e calcolare.

### Concetti in 2 minuti

- **`input("domanda")`** mostra la domanda, aspetta che tu scriva e prema Invio, e restituisce **ciò che hai scritto, sempre come testo** (`str`), anche se hai scritto `25`.
- Per fare calcoli devi **convertire** il testo in numero: `int("25")` → `25`; `float("1.5")` → `1.5`.
- Altri operatori matematici: `/` divisione normale (`90 / 60 = 1.5`), `//` **divisione intera** (`90 // 60 = 1`), `%` **resto** (`90 % 60 = 30`).
- Nelle f-string puoi formattare: `{ore:.2f}` = numero con 2 decimali.

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 3: input e output)

APP_NAME = "FocusFlow"
VERSION = "0.3"

print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)

# --- input(): il programma fa una domanda e aspetta la risposta ---
nome = input("Come ti chiami? ")
primo_task = input("Qual è il tuo primo task di oggi? ")

# input() restituisce SEMPRE testo: per fare calcoli lo convertiamo in numero con int()
minuti_testo = input("Quanti minuti vuoi concentrarti? (per esempio 25) ")
minuti = int(minuti_testo)

# --- Calcoli ---
ore = minuti / 60                 # divisione normale (risultato con la virgola)
ore_intere = minuti // 60         # divisione intera (butta via i decimali)
minuti_avanzati = minuti % 60     # resto della divisione

# --- Output ---
print()
print(f"Perfetto, {nome}!")
print(f"Task: {primo_task}")
print(f"Ti concentrerai per {minuti} minuti, cioè {ore:.2f} ore.")
print(f"In altre parole: {ore_intere} ore e {minuti_avanzati} minuti.")
```

### Cosa fa questo codice

- Le prime due `input()` leggono il tuo nome e il task: restano testo, vanno bene così.
- La terza legge i minuti **come testo** in `minuti_testo`, e `int(...)` li trasforma in numero in `minuti`.
- `//` e `%` ti danno ore intere e minuti avanzati (90 minuti → 1 ora e 30 minuti).
- Le `print` finali mostrano il riepilogo.

### Come eseguirlo

```powershell
python focusflow.py
```

Rispondi alle domande (esempio con Marco, "Studiare", 90):

```text
Come ti chiami? Marco
Qual è il tuo primo task di oggi? Studiare
Quanti minuti vuoi concentrarti? (per esempio 25) 90

Perfetto, Marco!
Task: Studiare
Ti concentrerai per 90 minuti, cioè 1.50 ore.
In altre parole: 1 ore e 30 minuti.
```

### Errori comuni

- **`ValueError: invalid literal for int() with base 10: 'venticinque'`**: hai scritto lettere (o un numero con la virgola) dove serviva un numero intero. Per ora riscrivi il numero; allo **Step 9** insegneremo al programma a non andare in crash.
- **`TypeError: unsupported operand type(s) for /: 'str' and 'int'`**: hai dimenticato `int(...)`, quindi stai dividendo un testo.
- **Il programma "sembra bloccato"**: sta aspettando che tu risponda. Scrivi e premi Invio.

### Esercizio

In `esercizi\step03.py`: chiedi **quanti pomodori** hai completato oggi e **quanti minuti** dura ciascuno. Stampa il tempo totale in ore e minuti (usa `//` e `%`). *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow ora **parla con l'utente**: chiede nome, primo task e durata della sessione.


---

## Step 4 — Condizioni (`if`, `elif`, `else`)

**Obiettivo:** far prendere decisioni al programma: fare cose diverse a seconda di cosa scrive l'utente.

### Concetti in 2 minuti

- Una **condizione** è una domanda a cui si risponde Vero o Falso. Si costruisce con i **confronti**: `==` (uguale), `!=` (diverso), `<` `>` `<=` `>=`.
  Attenzione: `=` assegna, `==` confronta.
- Struttura:

  ```python
  if condizione:
      # cosa fare se è vera
  elif altra_condizione:
      # altrimenti, se questa è vera
  else:
      # in tutti gli altri casi
  ```

- **L'indentazione conta!** Le righe "dentro" l'`if` sono spostate a destra di **4 spazi** (VS Code lo fa premendo Tab). Python usa gli spazi per capire quali righe appartengono a quale blocco.
- Puoi combinare condizioni con **`and`** (entrambe vere), **`or`** (almeno una vera), **`not`** (contrario).

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 4: condizioni)

APP_NAME = "FocusFlow"
VERSION = "0.4"

print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)

nome = input("Come ti chiami? ")
if nome == "":
    nome = "amico"          # se premi solo Invio, usiamo un nome di riserva

print(f"\nCiao {nome}! Cosa vuoi fare?")
print("1) Aggiungere un task")
print("2) Scegliere la durata del pomodoro")
print("0) Uscire")

scelta = input("La tua scelta: ")

if scelta == "1":
    task = input("Nome del task: ")
    if task == "":
        print("Non hai scritto niente: task non aggiunto.")
    else:
        print(f"Task aggiunto: {task}")

elif scelta == "2":
    minuti = int(input("Quanti minuti? "))
    if minuti < 5:
        print("Troppo breve: sotto i 5 minuti non è un vero pomodoro.")
    elif minuti > 60:
        print("Troppo lungo: oltre 60 minuti la concentrazione cala.")
    else:
        print(f"Ok! Pomodoro da {minuti} minuti impostato.")
        if minuti == 25:
            print("(È la durata classica del metodo Pomodoro.)")

elif scelta == "0":
    print("A presto!")

else:
    print("Scelta non valida. Riavvia il programma e riprova.")
```

### Cosa fa questo codice

- Se non scrivi il nome (`nome == ""`), usa `"amico"`.
- Mostra un menu e legge la tua scelta in `scelta`.
- La catena `if / elif / else` esegue **un solo** blocco: quello della scelta fatta.
- Nella scelta 2 c'è un `if` *dentro* un altro `if` (condizioni annidate): controlla se la durata è troppo corta, troppo lunga o giusta.
- L'ultimo `else` gestisce tutte le scelte non previste.

### Come eseguirlo

```powershell
python focusflow.py
```

Prova più volte, scegliendo opzioni diverse (anche `2` con `3`, `25`, `90`, e una scelta sbagliata come `7`). Esempio:

```text
La tua scelta: 2
Quanti minuti? 25
Ok! Pomodoro da 25 minuti impostato.
(È la durata classica del metodo Pomodoro.)
```

### Errori comuni

- **`IndentationError: expected an indented block`**: dopo i due punti `:` manca il blocco indentato (o hai usato spazi diversi). Premi Tab, non la barra spaziatrice a caso.
- **`SyntaxError: invalid syntax`** su un `if`: hai scritto `if scelta = "1":` con **un** `=`. Serve `==`.
- **`scelta == 1` non scatta mai**: `input()` restituisce testo, quindi va confrontato con `"1"` (con le virgolette), non con `1`.
- **Dimenticato i due punti `:`** a fine riga di `if`, `elif`, `else`.

### Esercizio

In `esercizi\step04.py`: chiedi quanti pomodori hai completato oggi (come numero) e stampa un messaggio diverso: 0 → "Inizia!", da 1 a 3 → "Buon inizio", da 4 a 7 → "Ottimo lavoro", 8 o più → "Fenomenale, ricordati di riposare". *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow ha un **menu** e **valida** la durata del pomodoro. Ma esegue una sola azione e poi finisce: al prossimo step lo facciamo ripartire da solo.

---

## Step 5 — Cicli (`while`, `for`)

**Obiettivo:** ripetere azioni: il menu deve tornare finché non scegli di uscire, e il programma deve saper contare alla rovescia.

### Concetti in 2 minuti

- **`while condizione:`** ripete il blocco finché la condizione è vera. `while True:` = ripeti per sempre, finché non incontri un **`break`** (esce dal ciclo).
- **`for variabile in ...:`** ripete il blocco per ogni elemento. Con **`range(5, 0, -1)`** ottieni 5, 4, 3, 2, 1 (parte da 5, si ferma *prima* di 0, passo -1).
- **`+=`**: `contatore += 1` equivale a `contatore = contatore + 1`.
- **`import`**: Python ha tanti "attrezzi" già pronti, chiamati **moduli**. `import time` ti presta il modulo `time`, che contiene `time.sleep(1)` = "aspetta 1 secondo". (I moduli li studieremo meglio allo Step 11.)

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 5: cicli)
import time   # "time" è un modulo di Python: ci serve per fare pause (time.sleep)

APP_NAME = "FocusFlow"
VERSION = "0.5"

print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)

nome = input("Come ti chiami? ")
if nome == "":
    nome = "amico"

task_aggiunti = 0     # contatore: parte da zero e cresce ogni volta che aggiungi un task
ultimo_task = ""      # qui ricordiamo l'ultimo task inserito

# --- Il ciclo principale: si ripete finché non scegli "0" ---
while True:
    print(f"\n--- Menu di {nome} ---")
    print("1) Aggiungere un task")
    print("2) Mostrare l'ultimo task")
    print("3) Provare un countdown di 5 secondi")
    print("0) Uscire")

    scelta = input("La tua scelta: ")

    if scelta == "1":
        task = input("Nome del task: ")
        if task == "":
            print("Non hai scritto niente: task non aggiunto.")
        else:
            ultimo_task = task
            task_aggiunti += 1          # equivale a: task_aggiunti = task_aggiunti + 1
            print(f"Task aggiunto! Ne hai aggiunti {task_aggiunti} in questa sessione.")

    elif scelta == "2":
        if ultimo_task == "":
            print("Non hai ancora aggiunto nessun task.")
        else:
            print(f"Ultimo task: {ultimo_task}")

    elif scelta == "3":
        print("Countdown!")
        for secondi in range(5, 0, -1):     # 5, 4, 3, 2, 1
            print(f"  {secondi}...")
            time.sleep(1)                   # aspetta 1 secondo
        print("Tempo scaduto! Bel lavoro.")

    elif scelta == "0":
        print(f"A presto {nome}! Hai aggiunto {task_aggiunti} task.")
        break                               # esce dal ciclo while

    else:
        print("Scelta non valida, riprova.")
```

### Cosa fa questo codice

- `while True:` fa ripartire il menu all'infinito. Si esce solo con la scelta `0`, che esegue `break`.
- `task_aggiunti += 1` conta i task aggiunti; `ultimo_task` ricorda l'ultimo.
- L'opzione 3 usa `for secondi in range(5, 0, -1)` per stampare 5…1, con `time.sleep(1)` che attende un secondo a ogni giro: è un **mini-timer**, il seme del Pomodoro!

### Come eseguirlo

```powershell
python focusflow.py
```

Aggiungi un paio di task, mostra l'ultimo, prova il countdown, poi esci con `0`:

```text
Countdown!
  5...
  4...
  3...
  2...
  1...
Tempo scaduto! Bel lavoro.
```

### Errori comuni

- **Il programma non finisce mai / sembra bloccato**: in un `while True` manca il `break`, oppure stai aspettando un input. Per fermarlo a forza premi **Ctrl+C** nel terminale.
- **Il countdown stampa subito tutto**: hai dimenticato `time.sleep(1)` o `import time` (in quel caso vedi `NameError: name 'time' is not defined`).
- **`range(5, 0)` non conta**: senza il passo `-1` non scende. Serve `range(5, 0, -1)`.
- **Il `break` dà `SyntaxError: 'break' outside loop`**: l'hai scritto fuori da un ciclo (indentazione sbagliata).

### Esercizio

In `esercizi\step05.py`: chiedi in ripetizione i **minuti di ogni sessione di studio** finché scrivi `0`; alla fine stampa quante sessioni hai fatto e il totale dei minuti. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow è un **programma a menu che si ripete**, con un contatore e un countdown di prova. Ancora però ricorda un solo task: servono le liste.

---

## Step 6 — Liste e tuple

**Obiettivo:** memorizzare *tanti* task, mostrarli numerati e rimuoverli.

### Concetti in 2 minuti

- Una **lista** è una sequenza ordinata di elementi: `spesa = ["pane", "latte"]`. Si può modificare.
  - `lista.append(x)` aggiunge in fondo · `lista.pop(i)` toglie l'elemento in posizione `i` e lo restituisce · `len(lista)` dice quanti sono · `lista.sort()` li mette in ordine.
  - **Gli indici partono da 0**: `spesa[0]` è il primo, `spesa[1]` il secondo, `spesa[-1]` l'ultimo.
- Una **tupla** è come una lista ma **non si può modificare**: `GIORNI = ("lun", "mar")`. Perfetta per cose fisse, come le voci del menu.
- **`enumerate(lista, start=1)`** ti dà, per ogni elemento, anche il suo numero: perfetto per elenchi numerati.
- Una lista vuota vale "falso": `if not tasks:` significa "se la lista è vuota".
- **`.strip()`** toglie gli spazi all'inizio e alla fine di un testo.

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 6: liste e tuple)
import time

APP_NAME = "FocusFlow"
VERSION = "0.6"

# Una TUPLA è come una lista, ma non si può modificare.
# Perfetta per valori che non devono cambiare mai, come le voci del menu.
MENU = (
    "Aggiungere un task",
    "Mostrare i task",
    "Rimuovere un task",
    "Countdown di prova (5 secondi)",
)

print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)

nome = input("Come ti chiami? ")
if nome == "":
    nome = "amico"

tasks = []   # una LISTA vuota: qui metteremo tutti i task

while True:
    print(f"\n--- Menu di {nome} ---")
    for numero, voce in enumerate(MENU, start=1):   # enumerate numera le voci: 1, 2, 3...
        print(f"{numero}) {voce}")
    print("0) Uscire")

    scelta = input("La tua scelta: ")

    if scelta == "1":
        titolo = input("Nome del task: ").strip()   # .strip() toglie gli spazi inutili
        if titolo == "":
            print("Non hai scritto niente: task non aggiunto.")
        else:
            tasks.append(titolo)                    # append = aggiungi in fondo alla lista
            print(f"Task aggiunto! Ora ne hai {len(tasks)}.")

    elif scelta == "2":
        if not tasks:                               # una lista vuota vale "falso"
            print("La lista è vuota. Aggiungi il tuo primo task!")
        else:
            print("\nI tuoi task:")
            for numero, titolo in enumerate(tasks, start=1):
                print(f"  {numero}. {titolo}")

    elif scelta == "3":
        if not tasks:
            print("Non c'è nulla da rimuovere.")
        else:
            for numero, titolo in enumerate(tasks, start=1):
                print(f"  {numero}. {titolo}")
            numero = int(input("Numero del task da rimuovere: "))
            if 1 <= numero <= len(tasks):
                rimosso = tasks.pop(numero - 1)     # pop = togli l'elemento in quella posizione
                print(f"Rimosso: {rimosso}")
            else:
                print("Numero non valido.")

    elif scelta == "4":
        print("Countdown!")
        for secondi in range(5, 0, -1):
            print(f"  {secondi}...")
            time.sleep(1)
        print("Tempo scaduto! Bel lavoro.")

    elif scelta == "0":
        print(f"A presto {nome}! Task nella lista: {len(tasks)}.")
        break

    else:
        print("Scelta non valida, riprova.")
```

### Cosa fa questo codice

- `MENU` è una **tupla**: il ciclo `for ... in enumerate(MENU, start=1)` stampa le voci già numerate.
- `tasks = []` è la lista dei task, all'inizio vuota.
- Opzione 1: `tasks.append(titolo)` aggiunge un task.
- Opzione 2: scorre `tasks` con `enumerate` e li stampa numerati (1, 2, 3…).
- Opzione 3: chiede un numero e rimuove con `tasks.pop(numero - 1)`. Il `- 1` serve perché tu conti da 1 ma Python da 0.
- `1 <= numero <= len(tasks)` controlla che il numero esista davvero.

### Come eseguirlo

```powershell
python focusflow.py
```

Aggiungi 3 task, mostrali, rimuovine uno (per esempio il 2) e mostra di nuovo la lista: devi vedere i numeri aggiornarsi.

### Errori comuni

- **`IndexError: list index out of range`**: hai chiesto una posizione che non esiste (per esempio il 5° elemento di una lista da 3). Controlla l'indice, ricordando che parte da 0.
- **`ValueError`** quando scrivi lettere al posto del numero: capita ancora, lo risolviamo allo Step 9.
- **`TypeError: 'tuple' object does not support item assignment`**: stai provando a modificare una tupla. Per quello servono le liste.
- **Al riavvio i task spariscono**: è normale! Per ora vivono solo in memoria. Il salvataggio arriva allo Step 10.

### Esercizio

In `esercizi\step06.py`: chiedi prodotti in ripetizione finché scrivi `fine`, salvandoli in una lista. Poi togli l'**ultimo** inserito, metti gli altri in **ordine alfabetico** e stampali numerati, con il totale. Inoltre crea una tupla con i giorni della settimana e stampa il terzo. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow gestisce **una lista di task**: aggiungi, mostra, rimuovi. Il menu è costruito da una tupla.

---

## Step 7 — Dizionari e set

**Obiettivo:** dare a ogni task più informazioni (titolo, categoria, fatto/da fare, pomodori) e imparare a elencare le categorie senza doppioni.

### Concetti in 2 minuti

- Un **dizionario** (`dict`) è un insieme di coppie **chiave → valore**, come una scheda:

  ```python
  task = {"titolo": "Studiare", "fatto": False, "pomodori": 0}
  print(task["titolo"])     # legge: Studiare
  task["fatto"] = True      # modifica
  ```

- Una lista di dizionari è una "tabella": ogni dizionario è una riga.
- Un **set** è una "scatola senza doppioni": `{"Casa", "Studio"}`. Si crea con `set()` e si riempie con `.add(x)`: aggiungere due volte lo stesso valore non cambia nulla.
- `sorted(...)` restituisce gli elementi in ordine; `", ".join(lista)` li unisce in un unico testo separati da virgole.
- **`valore_a if condizione else valore_b`**: una scelta in una riga. Esempio: `"[x]" if task["fatto"] else "[ ]"`.
- Dentro una f-string tra virgolette doppie, usa le virgolette **singole** per le chiavi: `f"{task['titolo']}"`.

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 7: dizionari e set)
import time

APP_NAME = "FocusFlow"
VERSION = "0.7"

MENU = (
    "Aggiungere un task",
    "Mostrare i task",
    "Completare un task",
    "Rimuovere un task",
    "Mini-pomodoro su un task (5 secondi di prova)",
    "Mostrare le categorie usate",
)

print("=" * 40)
print(f"   {APP_NAME} v{VERSION}")
print("=" * 40)

nome = input("Come ti chiami? ")
if nome == "":
    nome = "amico"

tasks = []   # ora è una lista di DIZIONARI: ogni task è un dizionario

while True:
    print(f"\n--- Menu di {nome} ---")
    for numero, voce in enumerate(MENU, start=1):
        print(f"{numero}) {voce}")
    print("0) Uscire")

    scelta = input("La tua scelta: ")

    if scelta == "1":
        titolo = input("Nome del task: ").strip()
        if titolo == "":
            print("Non hai scritto niente: task non aggiunto.")
        else:
            categoria = input("Categoria (Invio = Generale): ").strip()
            if categoria == "":
                categoria = "Generale"
            # Un dizionario: coppie chiave -> valore
            task = {
                "titolo": titolo,
                "categoria": categoria,
                "fatto": False,
                "pomodori": 0,
            }
            tasks.append(task)
            print(f"Task aggiunto! Ora ne hai {len(tasks)}.")

    elif scelta == "2":
        if not tasks:
            print("La lista è vuota. Aggiungi il tuo primo task!")
        else:
            print("\nI tuoi task:")
            for numero, task in enumerate(tasks, start=1):
                # "valore if condizione else altro valore": una scelta in una riga
                simbolo = "[x]" if task["fatto"] else "[ ]"
                print(f"  {numero}. {simbolo} {task['titolo']} ({task['categoria']}) - pomodori: {task['pomodori']}")

    elif scelta == "3":
        if not tasks:
            print("Non c'è nessun task da completare.")
        else:
            for numero, task in enumerate(tasks, start=1):
                print(f"  {numero}. {task['titolo']}")
            numero = int(input("Numero del task completato: "))
            if 1 <= numero <= len(tasks):
                tasks[numero - 1]["fatto"] = True      # cambio il valore della chiave "fatto"
                print("Fatto! Bel lavoro.")
            else:
                print("Numero non valido.")

    elif scelta == "4":
        if not tasks:
            print("Non c'è nulla da rimuovere.")
        else:
            for numero, task in enumerate(tasks, start=1):
                print(f"  {numero}. {task['titolo']}")
            numero = int(input("Numero del task da rimuovere: "))
            if 1 <= numero <= len(tasks):
                rimosso = tasks.pop(numero - 1)
                print(f"Rimosso: {rimosso['titolo']}")
            else:
                print("Numero non valido.")

    elif scelta == "5":
        if not tasks:
            print("Aggiungi prima un task.")
        else:
            for numero, task in enumerate(tasks, start=1):
                print(f"  {numero}. {task['titolo']}")
            numero = int(input("Su quale task ti concentri? "))
            if 1 <= numero <= len(tasks):
                print("Concentrazione!")
                for secondi in range(5, 0, -1):
                    print(f"  {secondi}...")
                    time.sleep(1)
                tasks[numero - 1]["pomodori"] += 1
                print("Pomodoro completato!")
            else:
                print("Numero non valido.")

    elif scelta == "6":
        categorie = set()                  # un SET: una "scatola" senza doppioni
        for task in tasks:
            categorie.add(task["categoria"])
        if not categorie:
            print("Nessuna categoria: non hai ancora task.")
        else:
            print("Categorie usate:", ", ".join(sorted(categorie)))

    elif scelta == "0":
        fatti = 0
        for task in tasks:
            if task["fatto"]:
                fatti += 1
        print(f"A presto {nome}! Task completati: {fatti} su {len(tasks)}.")
        break

    else:
        print("Scelta non valida, riprova.")
```

### Cosa fa questo codice

- Ogni task è ora un **dizionario** con `titolo`, `categoria`, `fatto`, `pomodori`.
- Opzione 2 stampa `[ ]` o `[x]` a seconda di `task["fatto"]`.
- Opzione 3 (completa) fa `tasks[numero - 1]["fatto"] = True`: prende il task e cambia la chiave `fatto`.
- Opzione 5 è un **mini-pomodoro di prova** da 5 secondi: al termine aggiunge `+= 1` ai `pomodori` di quel task.
- Opzione 6 riempie un **set** con le categorie usate, senza ripetizioni.
- Il codice dell'uscita (opzione `0`) conta i task fatti con un ciclo.

### Come eseguirlo

```powershell
python focusflow.py
```

Aggiungi 3 task con categorie (due uguali, per esempio "Studio" e "Studio"), completane uno, poi scegli l'opzione 6:

```text
Categorie usate: Casa, Studio
```

### Errori comuni

- **`KeyError: 'titolo'`**: la chiave non esiste (errore di battitura, per esempio `"Titolo"` con la maiuscola).
- **`SyntaxError` dentro una f-string** con `task["titolo"]`: usa le virgolette singole `task['titolo']` quando la f-string è già tra virgolette doppie.
- **`TypeError: list indices must be integers`**: hai usato un dizionario come indice di lista, o viceversa. Controlla se la cosa tra `[]` è un numero (lista) o una chiave (dizionario).
- **`{}` crea un dizionario, non un set vuoto**: per un set vuoto usa `set()`.

### Esercizio

In `esercizi\step07.py`: crea un dizionario `pomodori_per_giorno` con tre giorni; aggiungine un quarto; trova (con un ciclo) il giorno col numero più alto. Poi prendi la frase `"studiare python è bello e studiare ogni giorno è meglio"`, spezzala in parole con `frase.split()` e crea un **set** per contare le parole diverse. *(Soluzione in fondo.)*

### Il progetto finora

I task sono **dizionari completi** e FocusFlow conta i pomodori per ogni task. Il codice però sta diventando lungo e ripetitivo: allo Step 8 lo mettiamo in ordine.


---

## Step 8 — Funzioni

**Obiettivo:** riorganizzare il programma in "pezzi" con un nome, per non ripetere codice e leggerlo meglio.

### Concetti in 2 minuti

- Una **funzione** è un blocco di codice con un nome, che puoi richiamare quando vuoi:

  ```python
  def saluta(nome):          # def = "definisco una funzione"; nome = parametro
      return f"Ciao {nome}"  # return = il risultato che restituisce

  messaggio = saluta("Marco")  # chiamata
  ```

- I **parametri** sono i dati che la funzione riceve; il **`return`** è il dato che restituisce. Se non c'è `return` la funzione restituisce `None` ("niente").
- Un **valore predefinito** si scrive nei parametri: `def chiedi_testo(domanda, predefinito="")`.
- Il testo tra `"""triple virgolette"""` all'inizio della funzione è la **docstring**: la descrizione, utile a te e a VS Code.
- Le variabili create **dentro** una funzione vivono solo lì (sono *locali*).
- Se passi una **lista** o un dizionario a una funzione e lo modifichi, la modifica vale anche fuori: non serve restituirlo.
- Convenzione `main()` + `if __name__ == "__main__":` (la riga in fondo): significa "esegui `main()` solo se questo file è stato avviato direttamente". Ci servirà tra poco.

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 8: funzioni)
import time

APP_NAME = "FocusFlow"
VERSION = "0.8"

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
    """Stampa il titolo dell'app."""
    print("=" * 40)
    print(f"   {APP_NAME} v{VERSION}")
    print("=" * 40)


def chiedi_testo(domanda, predefinito=""):
    """Fa una domanda. Se premi solo Invio, restituisce il valore predefinito."""
    risposta = input(domanda).strip()
    if risposta == "":
        return predefinito
    return risposta


def chiedi_numero(domanda, minimo, massimo):
    """Chiede un numero tra minimo e massimo. Restituisce None se la risposta non va bene."""
    testo = input(domanda).strip()
    if not testo.isdigit():                  # isdigit(): il testo è fatto solo di cifre?
        print("Devi scrivere un numero.")
        return None
    numero = int(testo)
    if numero < minimo or numero > massimo:
        print(f"Il numero deve essere tra {minimo} e {massimo}.")
        return None
    return numero


def mostra_menu(nome):
    print(f"\n--- Menu di {nome} ---")
    for numero, voce in enumerate(MENU, start=1):
        print(f"{numero}) {voce}")
    print("0) Uscire")


# ---------- Funzioni dei task ----------

def mostra_task(tasks):
    if not tasks:
        print("La lista è vuota. Aggiungi il tuo primo task!")
        return
    print("\nI tuoi task:")
    for numero, task in enumerate(tasks, start=1):
        simbolo = "[x]" if task["fatto"] else "[ ]"
        print(f"  {numero}. {simbolo} {task['titolo']} ({task['categoria']}) - pomodori: {task['pomodori']}")


def scegli_task(tasks, domanda):
    """Mostra i task, chiede un numero e restituisce il task scelto (o None)."""
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
    tasks.append({"titolo": titolo, "categoria": categoria, "fatto": False, "pomodori": 0})
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
    print("Concentrazione!")
    for secondi in range(5, 0, -1):
        print(f"  {secondi}...")
        time.sleep(1)
    task["pomodori"] += 1
    print("Pomodoro completato!")


def mostra_categorie(tasks):
    categorie = set()
    for task in tasks:
        categorie.add(task["categoria"])
    if not categorie:
        print("Nessuna categoria: non hai ancora task.")
    else:
        print("Categorie usate:", ", ".join(sorted(categorie)))


def conta_fatti(tasks):
    """Restituisce quanti task sono completati."""
    fatti = 0
    for task in tasks:
        if task["fatto"]:
            fatti += 1
    return fatti


# ---------- Programma principale ----------

def main():
    mostra_banner()
    nome = chiedi_testo("Come ti chiami? ", "amico")
    tasks = []

    while True:
        mostra_menu(nome)
        scelta = input("La tua scelta: ").strip()

        if scelta == "1":
            aggiungi_task(tasks)
        elif scelta == "2":
            mostra_task(tasks)
        elif scelta == "3":
            completa_task(tasks)
        elif scelta == "4":
            rimuovi_task(tasks)
        elif scelta == "5":
            mini_pomodoro(tasks)
        elif scelta == "6":
            mostra_categorie(tasks)
        elif scelta == "0":
            print(f"A presto {nome}! Task completati: {conta_fatti(tasks)} su {len(tasks)}.")
            break
        else:
            print("Scelta non valida, riprova.")


# Questa riga fa partire main() solo se avvii QUESTO file direttamente.
if __name__ == "__main__":
    main()
```

### Cosa fa questo codice

- **Aiuti generici**: `mostra_banner`, `chiedi_testo` (restituisce il valore predefinito se premi solo Invio), `chiedi_numero` (chiede un numero in un intervallo e restituisce `None` se non va bene), `mostra_menu`.
- **Azioni sui task**: ogni opzione del menu ora è una funzione (`aggiungi_task`, `completa_task`, `rimuovi_task`…). Tutte ricevono la lista `tasks`.
- **`scegli_task`** è usata da più funzioni: mostra l'elenco, chiede il numero e restituisce il task scelto. Prima lo stesso codice era ripetuto tre volte!
- **`main()`** contiene il programma principale: ora è corto e leggibile come un indice.

### Come eseguirlo

```powershell
python focusflow.py
```

Il comportamento è **identico** allo Step 7: lo scopo di un *refactoring* è proprio cambiare l'organizzazione senza cambiare il risultato. Provali tutti: aggiungi, completa, rimuovi, mini-pomodoro, categorie, uscita.

### Errori comuni

- **`NameError: name 'aggiungi_task' is not defined`**: stai chiamando una funzione prima di averla definita sopra, oppure il nome è scritto diversamente.
- **`TypeError: aggiungi_task() missing 1 required positional argument: 'tasks'`**: hai chiamato la funzione senza darle il parametro. Serve `aggiungi_task(tasks)`.
- **La funzione "non fa niente"**: l'hai definita ma non l'hai mai **chiamata** (`def` non esegue nulla, definisce soltanto).
- **Una funzione restituisce `None`**: ti sei dimenticato il `return`.
- **Il programma non parte**: hai tolto o indentato male le ultime due righe (`if __name__ == "__main__":` e `main()`).

### Esercizio

In `esercizi\step08.py`: scrivi la funzione `ore_e_minuti(minuti)` che **restituisce** due valori (ore, minuti) e la funzione `messaggio_pomodori(n)` che restituisce un testo diverso a seconda di `n`. Provale con `135` minuti e con 0, 2 e 9 pomodori. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow è **ordinato in funzioni**: aggiungere una voce al menu significa scrivere una funzione e una riga in `main()`.

---

## Step 9 — Gestione degli errori

**Obiettivo:** far sì che il programma non vada in crash se scrivi lettere dove servono numeri o premi Ctrl+C.

### Concetti in 2 minuti

- Un **errore** (o *eccezione*) interrompe il programma e mostra un **traceback**. Imparare a leggerlo è la competenza più utile di un programmatore. Esempio:

  ```text
  Traceback (most recent call last):
    File "C:\Users\Marco\Progetti\FocusFlow\focusflow.py", line 12, in <module>
      minuti = int(minuti_testo)
  ValueError: invalid literal for int() with base 10: 'venticinque'
  ```

  **Si legge dal basso**: l'**ultima riga** dice *che errore* è (`ValueError`) e perché; sopra c'è *in quale file e riga* è successo, e la riga di codice colpevole.
- **`try / except`** permette di "provare" del codice e di gestire l'errore:

  ```python
  try:
      numero = int(input("Numero: "))
  except ValueError:
      print("Non è un numero!")
  ```

- Altri errori frequenti: `ZeroDivisionError`, `KeyError`, `IndexError`, `FileNotFoundError`, **`KeyboardInterrupt`** (Ctrl+C).
- Il blocco **`finally`** viene eseguito **sempre**, errore o no: utile per le operazioni di chiusura.
- Cattura errori **specifici** (`except ValueError`), mai un `except:` generico che nasconde i problemi veri.

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 9: gestione degli errori)
import time

APP_NAME = "FocusFlow"
VERSION = "0.9"

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
    """Stampa il titolo dell'app."""
    print("=" * 40)
    print(f"   {APP_NAME} v{VERSION}")
    print("=" * 40)


def chiedi_testo(domanda, predefinito=""):
    """Fa una domanda. Se premi solo Invio, restituisce il valore predefinito."""
    risposta = input(domanda).strip()
    if risposta == "":
        return predefinito
    return risposta


def chiedi_numero(domanda, minimo, massimo):
    """Chiede un numero tra minimo e massimo. Restituisce None se la risposta non va bene."""
    try:
        numero = int(input(domanda))          # se non è un numero, int() solleva un errore...
    except ValueError:                        # ...e noi lo "prendiamo" qui, senza crash
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


# ---------- Funzioni dei task ----------

def mostra_task(tasks):
    if not tasks:
        print("La lista è vuota. Aggiungi il tuo primo task!")
        return
    print("\nI tuoi task:")
    for numero, task in enumerate(tasks, start=1):
        simbolo = "[x]" if task["fatto"] else "[ ]"
        print(f"  {numero}. {simbolo} {task['titolo']} ({task['categoria']}) - pomodori: {task['pomodori']}")


def scegli_task(tasks, domanda):
    """Mostra i task, chiede un numero e restituisce il task scelto (o None)."""
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
    tasks.append({"titolo": titolo, "categoria": categoria, "fatto": False, "pomodori": 0})
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
    except KeyboardInterrupt:                 # Ctrl+C durante il countdown
        print("\nPomodoro interrotto: non viene conteggiato.")
        return
    task["pomodori"] += 1
    print("Pomodoro completato!")


def mostra_categorie(tasks):
    categorie = set()
    for task in tasks:
        categorie.add(task["categoria"])
    if not categorie:
        print("Nessuna categoria: non hai ancora task.")
    else:
        print("Categorie usate:", ", ".join(sorted(categorie)))


def conta_fatti(tasks):
    """Restituisce quanti task sono completati."""
    fatti = 0
    for task in tasks:
        if task["fatto"]:
            fatti += 1
    return fatti


# ---------- Programma principale ----------

def main():
    mostra_banner()
    nome = chiedi_testo("Come ti chiami? ", "amico")
    tasks = []

    try:
        while True:
            mostra_menu(nome)
            scelta = input("La tua scelta: ").strip()

            if scelta == "1":
                aggiungi_task(tasks)
            elif scelta == "2":
                mostra_task(tasks)
            elif scelta == "3":
                completa_task(tasks)
            elif scelta == "4":
                rimuovi_task(tasks)
            elif scelta == "5":
                mini_pomodoro(tasks)
            elif scelta == "6":
                mostra_categorie(tasks)
            elif scelta == "0":
                break
            else:
                print("Scelta non valida, riprova.")
    except (KeyboardInterrupt, EOFError):     # Ctrl+C (o Ctrl+Z su Windows) nel menu
        print("\nInterrotto dall'utente.")
    finally:                                  # il blocco "finally" viene eseguito SEMPRE
        print(f"A presto {nome}! Task completati: {conta_fatti(tasks)} su {len(tasks)}.")


# Questa riga fa partire main() solo se avvii QUESTO file direttamente.
if __name__ == "__main__":
    main()
```

### Cosa fa questo codice

- È il codice dello Step 8 con tre migliorie:
  1. `chiedi_numero` ora usa `try / except ValueError`: se scrivi lettere stampa un messaggio e restituisce `None`.
  2. `mini_pomodoro` intercetta **`KeyboardInterrupt`**: se premi Ctrl+C durante il countdown, il pomodoro viene annullato senza crash.
  3. `main()` avvolge tutto in `try / except / finally`: anche se chiudi con Ctrl+C, il programma saluta e mostra il riepilogo.

### Come eseguirlo

```powershell
python focusflow.py
```

Prova a **rompere** il programma: aggiungi un task, scegli "Completa" e scrivi `abc`, poi `9`, poi `1`. Devi vedere messaggi gentili invece di un crash:

```text
Numero del task completato: Devi scrivere un numero intero (per esempio 3).
Numero del task completato: Il numero deve essere tra 1 e 1.
Numero del task completato: Fatto! Bel lavoro.
```

Poi avvia un mini-pomodoro e premi **Ctrl+C** durante il countdown.

### Errori comuni

- **`except ValueError:` ma l'errore è un altro** (per esempio `KeyError`): il tuo `except` non lo cattura. Leggi l'ultima riga del traceback per sapere il nome esatto.
- **Il messaggio d'errore è scomparso e non capisci cosa è successo**: non usare mai `except:` vuoto. Se serve vedere l'errore: `except ValueError as errore: print(errore)`.
- **Come uscire dal menu in modo "pulito"**: scrivi `0`. Ctrl+C (o Ctrl+Z e Invio su Windows) funziona comunque: il programma saluta e mostra il riepilogo grazie al `finally`.

### Esercizio

In `esercizi\step09.py`: chiedi un numero e stampa `100 / numero`. Ripeti la domanda finché l'utente scrive un numero valido, gestendo **sia** le lettere (`ValueError`) **sia** lo zero (`ZeroDivisionError`). *(Suggerimento: un blocco `try` può avere più `except`; la parte `else:` parte solo se non ci sono stati errori. Soluzione in fondo.)*

### Il progetto finora

FocusFlow è **robusto**: non va più in crash per input sbagliati. Manca una cosa fondamentale: ogni volta che lo chiudi, i task spariscono.

---

## Step 10 — File: salvare e caricare i dati (JSON)

**Obiettivo:** salvare i task su disco e ritrovarli alla prossima apertura del programma.

### Concetti in 2 minuti

- Per leggere/scrivere un file si usa **`with open(percorso, modo, encoding="utf-8") as f:`**. I **modi**: `"r"` leggi, `"w"` scrivi (cancella il contenuto precedente!), `"a"` aggiungi in fondo. Il `with` chiude il file da solo. `encoding="utf-8"` serve per le lettere accentate.
- **JSON** è un formato di testo per salvare liste e dizionari: è quasi identico a come li scrivi in Python. Il modulo `json` li converte:
  - `json.dump(dati, f, ensure_ascii=False, indent=2)` → scrive i dati nel file (`indent=2` li rende leggibili, `ensure_ascii=False` mantiene le accentate);
  - `json.load(f)` → legge il file e restituisce i dati.
- **`pathlib.Path`** gestisce percorsi di file e cartelle: `Path.home()` è la tua cartella utente (`C:\Users\Marco`), e l'operatore **`/`** unisce i pezzi: `Path.home() / "FocusFlow"`. `cartella.mkdir(parents=True, exist_ok=True)` crea la cartella se manca.
- Salveremo in `C:\Users\TuoNome\FocusFlow\tasks.json`: una cartella fissa e sicura, indipendente da dove si trova il programma (fondamentale quando diventerà un `.exe`).

### Dove lavori

**`focusflow.py`** (cancella tutto e incolla).

### Il codice

```python
# focusflow.py  (Step 10: file e JSON)
import json                  # per salvare/leggere dati in formato JSON
import time
from pathlib import Path     # per lavorare con le cartelle in modo semplice

APP_NAME = "FocusFlow"
VERSION = "0.10"

# Dove salviamo i dati: nella tua cartella personale, dentro "FocusFlow".
# Esempio su Windows: C:\Users\Marco\FocusFlow\tasks.json
DATA_DIR = Path.home() / "FocusFlow"
TASKS_FILE = DATA_DIR / "tasks.json"

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
    """Stampa il titolo dell'app."""
    print("=" * 40)
    print(f"   {APP_NAME} v{VERSION}")
    print("=" * 40)


def chiedi_testo(domanda, predefinito=""):
    """Fa una domanda. Se premi solo Invio, restituisce il valore predefinito."""
    risposta = input(domanda).strip()
    if risposta == "":
        return predefinito
    return risposta


def chiedi_numero(domanda, minimo, massimo):
    """Chiede un numero tra minimo e massimo. Restituisce None se la risposta non va bene."""
    try:
        numero = int(input(domanda))          # se non è un numero, int() solleva un errore...
    except ValueError:                        # ...e noi lo "prendiamo" qui, senza crash
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


# ---------- Funzioni dei task ----------

def mostra_task(tasks):
    if not tasks:
        print("La lista è vuota. Aggiungi il tuo primo task!")
        return
    print("\nI tuoi task:")
    for numero, task in enumerate(tasks, start=1):
        simbolo = "[x]" if task["fatto"] else "[ ]"
        print(f"  {numero}. {simbolo} {task['titolo']} ({task['categoria']}) - pomodori: {task['pomodori']}")


def scegli_task(tasks, domanda):
    """Mostra i task, chiede un numero e restituisce il task scelto (o None)."""
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
    tasks.append({"titolo": titolo, "categoria": categoria, "fatto": False, "pomodori": 0})
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
    except KeyboardInterrupt:                 # Ctrl+C durante il countdown
        print("\nPomodoro interrotto: non viene conteggiato.")
        return
    task["pomodori"] += 1
    print("Pomodoro completato!")


def mostra_categorie(tasks):
    categorie = set()
    for task in tasks:
        categorie.add(task["categoria"])
    if not categorie:
        print("Nessuna categoria: non hai ancora task.")
    else:
        print("Categorie usate:", ", ".join(sorted(categorie)))


def conta_fatti(tasks):
    """Restituisce quanti task sono completati."""
    fatti = 0
    for task in tasks:
        if task["fatto"]:
            fatti += 1
    return fatti


# ---------- Salvataggio su file ----------

def carica_task():
    """Legge i task dal file. Se il file non esiste ancora, restituisce una lista vuota."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []                              # prima volta che avvii l'app: nessun problema
    except json.JSONDecodeError:
        print("Il file dei task è rovinato: riparto da una lista vuota.")
        return []


def salva_task(tasks):
    """Scrive tutti i task nel file (lo crea se non esiste)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)   # crea la cartella se manca
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


# ---------- Programma principale ----------

def main():
    mostra_banner()
    nome = chiedi_testo("Come ti chiami? ", "amico")
    tasks = carica_task()                     # all'avvio leggiamo i task salvati
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
    except (KeyboardInterrupt, EOFError):     # Ctrl+C (o Ctrl+Z su Windows) nel menu
        print("\nInterrotto dall'utente.")
    finally:                                  # il blocco "finally" viene eseguito SEMPRE
        print(f"A presto {nome}! Task completati: {conta_fatti(tasks)} su {len(tasks)}.")


# Questa riga fa partire main() solo se avvii QUESTO file direttamente.
if __name__ == "__main__":
    main()
```

### Cosa fa questo codice

- In cima: `import json`, `from pathlib import Path`, e le costanti `DATA_DIR` (la cartella dati) e `TASKS_FILE` (il file).
- **`carica_task()`**: legge il file. Se non esiste ancora (`FileNotFoundError`, la prima volta) restituisce una lista vuota; se il file è rovinato (`json.JSONDecodeError`) avvisa e riparte da zero.
- **`salva_task(tasks)`**: crea la cartella se serve e scrive tutta la lista nel file.
- **`main()`**: all'avvio fa `tasks = carica_task()`; dopo ogni modifica (aggiungi, completa, rimuovi, pomodoro) chiama `salva_task(tasks)`.

### Come eseguirlo

```powershell
python focusflow.py
```

1. Aggiungi due task, completane uno, esci con `0`.
2. **Riavvia** il programma: scegli "Mostra i task". I task ci sono ancora! All'avvio leggi *"Ho caricato 2 task salvati."*
3. Guarda il file: in VS Code usa **File → Apri file…** e apri `C:\Users\TuoNome\FocusFlow\tasks.json`. Vedrai i tuoi dati in forma leggibile:

```text
[
  {
    "titolo": "Studiare Python",
    "categoria": "Studio",
    "fatto": true,
    "pomodori": 0
  }
]
```

### Errori comuni

- **`PermissionError`**: stai scrivendo in una cartella protetta. Usiamo la tua cartella utente proprio per evitarlo.
- **Caratteri accentati rovinati nel file**: manca `encoding="utf-8"` oppure `ensure_ascii=False`.
- **I task non si salvano**: hai dimenticato `salva_task(tasks)` dopo la modifica (il salvataggio non è automatico).
- **`json.decoder.JSONDecodeError`**: il file è stato modificato a mano e ora non è JSON valido (una virgola in più, per esempio). Il programma lo gestisce e riparte da vuoto; se vuoi azzerare tutto, cancella il file `tasks.json`.
- **Vuoi ricominciare da zero**: cancella la cartella `C:\Users\TuoNome\FocusFlow`.

### Esercizio

In `esercizi\step10.py`: crea un mini **diario**. Chiedi una frase e **aggiungila in fondo** a un file `diario.txt` (modo `"a"`) insieme alla data di oggi (`from datetime import date` e `date.today().isoformat()`). Poi rileggi il file e stampa tutte le righe. Eseguilo due volte per vedere che le frasi si accumulano. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow ora **ricorda i task** tra una sessione e l'altra. La versione a terminale è completa: nella prossima parte la ripuliamo per prepararla all'interfaccia grafica.


---

# PARTE B — Organizzare il progetto (step 11–14)

Ora FocusFlow funziona. Prima di costruire l'interfaccia grafica lo mettiamo in ordine come fanno i professionisti: file separati, ambiente virtuale, Git/GitHub e classi.

## Step 11 — Moduli: dividere il programma in più file

**Obiettivo:** separare il programma in file con compiti diversi (dati, logica dei task, interfaccia a testo), per poter riusare la logica anche nell'app grafica.

### Concetti in 2 minuti

- Ogni file `.py` è un **modulo**. Con `import` puoi usare ciò che c'è dentro un altro file della stessa cartella:
  - `import storage` → poi scrivi `storage.carica_json(...)`;
  - `from tasks import nuovo_task, carica_task` → prendi solo alcune funzioni e le usi direttamente.
- Python ha già migliaia di moduli pronti, la **libreria standard** (`json`, `time`, `pathlib`, `datetime`, `random`…). Fuori dalla libreria standard ci sono le **librerie di terze parti**, che si installano con `pip` (Step 12).
- **Separazione dei compiti**: `storage.py` sa solo leggere/scrivere file; `tasks.py` sa come è fatto un task (senza `input` né `print`); `main.py` parla con l'utente. Così, quando faremo la finestra grafica, **riuseremo `tasks.py` e `storage.py` senza toccarli**.
- **`dict.get("chiave", valore)`** legge una chiave e, se non c'è, usa il valore di riserva: serve per i vecchi file che non hanno i campi nuovi.
- Una funzione può restituire **più valori** (una tupla) e puoi "spacchettarli": `totale, fatti, da_fare = statistiche(tasks)`.
- **Non chiamare mai un tuo file come un modulo che usi** (`json.py`, `time.py`…): Python importerebbe il tuo al posto di quello vero.

### Dove lavori

Crea **due file nuovi**, `storage.py` e `tasks.py`, nella cartella `FocusFlow`. Poi **rinomina `focusflow.py` in `main.py`** e sostituisci tutto il suo contenuto con il codice di `main.py` qui sotto.

### Il codice

**`storage.py`**

```python
# storage.py
# Si occupa SOLO di leggere e scrivere file JSON nella cartella dati di FocusFlow.
import json
from pathlib import Path

# Esempio su Windows: C:\Users\Marco\FocusFlow
DATA_DIR = Path.home() / "FocusFlow"


def carica_json(nome_file, predefinito):
    """Legge un file JSON. Se non esiste o è rovinato, restituisce 'predefinito'."""
    percorso = DATA_DIR / nome_file
    try:
        with open(percorso, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return predefinito
    except json.JSONDecodeError:
        print(f"Il file {nome_file} è rovinato: uso i valori predefiniti.")
        return predefinito


def salva_json(nome_file, dati):
    """Scrive 'dati' in un file JSON (crea la cartella se manca)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    percorso = DATA_DIR / nome_file
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)
```

**`tasks.py`**

```python
# tasks.py
# La "logica" dei task: come si crea un task, come si carica, come si contano.
# Qui dentro NON ci sono input() né print(): così lo riuseremo anche nell'app grafica.
from datetime import date     # date.today() ci dà la data di oggi

import storage                # il nostro modulo storage.py

TASKS_FILE = "tasks.json"
CATEGORIE_BASE = ("Generale", "Studio", "Lavoro", "Casa")


def nuovo_task(titolo, categoria="Generale"):
    """Crea un nuovo task (un dizionario)."""
    return {
        "titolo": titolo,
        "categoria": categoria,
        "fatto": False,
        "pomodori": 0,
        "creato": date.today().isoformat(),    # per esempio "2026-10-02"
    }


def carica_task():
    """Legge i task dal file. Se mancano delle chiavi, mette valori predefiniti."""
    dati = storage.carica_json(TASKS_FILE, [])
    tasks = []
    for d in dati:
        # d.get("chiave", valore) = prendi la chiave, e se non c'è usa il valore
        tasks.append({
            "titolo": d.get("titolo", "(senza titolo)"),
            "categoria": d.get("categoria", "Generale"),
            "fatto": d.get("fatto", False),
            "pomodori": d.get("pomodori", 0),
            "creato": d.get("creato", ""),
        })
    return tasks


def salva_task(tasks):
    storage.salva_json(TASKS_FILE, tasks)


def conta_fatti(tasks):
    fatti = 0
    for task in tasks:
        if task["fatto"]:
            fatti += 1
    return fatti


def statistiche(tasks):
    """Restituisce una TUPLA: (totale, fatti, da_fare)."""
    totale = len(tasks)
    fatti = conta_fatti(tasks)
    return totale, fatti, totale - fatti


def categorie_usate(tasks):
    """Restituisce un SET con le categorie usate (senza doppioni)."""
    categorie = set()
    for task in tasks:
        categorie.add(task["categoria"])
    return categorie
```

**`main.py`** *(il vecchio `focusflow.py`, rinominato)*

```python
# main.py  (Step 11: moduli) - l'interfaccia "a testo" (terminale) di FocusFlow
import time

# from ... import ...: prendo dal file tasks.py solo le funzioni che mi servono
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
        totale, fatti, da_fare = statistiche(tasks)     # "spacchetto" la tupla in 3 variabili
        print(f"A presto {nome}! Totale: {totale} | fatti: {fatti} | da fare: {da_fare}.")


if __name__ == "__main__":
    main()
```

### Cosa fa questo codice

- **`storage.py`**: due funzioni generiche, `carica_json(nome_file, predefinito)` e `salva_json(nome_file, dati)`. Usate per qualunque file JSON, non solo per i task.
- **`tasks.py`**: `nuovo_task` crea il dizionario di un task (con la data di creazione, nuovo campo `creato`), `carica_task` e `salva_task` usano `storage`, e poi ci sono funzioni "di calcolo": `conta_fatti`, `statistiche` (restituisce una tupla), `categorie_usate` (restituisce un set).
- **`main.py`**: contiene solo la parte "a testo": menu, domande, stampe. Importa da `tasks` le funzioni che servono.
- I **vecchi task** salvati allo Step 10 si caricano lo stesso: `carica_task` usa `.get()` per i campi mancanti (la data di creazione sarà vuota).

### Come eseguirlo

```powershell
python main.py
```

Il programma si comporta come prima (i tuoi task salvati ci sono ancora), con in più la data di creazione e il riepilogo finale `Totale | fatti | da fare`:

```text
A presto Marco! Totale: 2 | fatti: 1 | da fare: 1.
```

Noterai anche una nuova cartella **`__pycache__`**: la crea Python da solo per velocizzare gli import. Ignorala (la escluderemo da Git).

### Errori comuni

- **`ModuleNotFoundError: No module named 'storage'`**: `storage.py` non è nella stessa cartella di `main.py`, oppure stai lanciando il comando da un'altra cartella, oppure il nome è sbagliato (controlla che non sia `storage.py.txt`).
- **`ImportError: cannot import name 'nuovo_task' from 'tasks'`**: il nome nell'`import` non corrisponde a quello nel file (errore di battitura) o `tasks.py` non è salvato.
- **`AttributeError: module 'storage' has no attribute 'carica_json'`**: stesso problema, vicino a un `storage.xxx`.
- **Modifichi un modulo ma non cambia nulla**: ricordati di **salvare tutti i file** (Ctrl+K poi S, oppure File → Salva tutto).

### Esercizio

In `esercizi\utils.py` scrivi la funzione `formatta_durata(minuti)` che trasforma `135` in `"2h 15min"` e `45` in `"45min"`. In un altro file `esercizi\step11_prova.py` importala con `from utils import formatta_durata`, provala, e usa anche il modulo `random` della libreria standard (`random.choice(...)`) per stampare una frase motivazionale a caso da una tupla. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow è diviso in **3 moduli**: `storage.py` (file), `tasks.py` (logica), `main.py` (terminale). Il modulo `tasks.py` è pronto per essere riusato dall'interfaccia grafica.

---

## Step 12 — Ambienti virtuali e pip

**Obiettivo:** creare un ambiente isolato per il progetto e installare la prima libreria esterna (CustomTkinter).

### Concetti in 2 minuti

- **`pip`** è il programma che scarica e installa librerie da **PyPI**, il grande archivio pubblico e gratuito di Python. Funziona come un "negozio di app" per Python.
- Un **ambiente virtuale** (*virtual environment*, `venv`) è una cartella (`.venv`) con una **copia isolata di Python** e delle librerie del *solo* progetto. Vantaggi: progetti diversi non litigano tra loro, e puoi ricreare tutto su un altro PC.
- Quando l'ambiente è **attivo**, il prompt inizia con **`(.venv)`** e `python` / `pip` lavorano dentro l'ambiente.
- **`requirements.txt`** elenca le librerie del progetto: con `pip install -r requirements.txt` le reinstalli tutte in un colpo. `customtkinter>=6.0,<7` significa "versione 6.x, mai la 7".
- Un secondo file, **`requirements-dev.txt`**, elenca gli strumenti che servono solo a *costruire* l'app (PyInstaller, Pillow): li useremo allo Step 19.
- Il **terminale** di VS Code a volte si chiama anche "shell"; su Windows è **PowerShell**.

### Dove lavori

Crea nella cartella `FocusFlow` **tre file nuovi**: `requirements.txt`, `requirements-dev.txt` e `check_env.py`. Poi usi il terminale.

### Il codice

**`requirements.txt`**

```text
customtkinter>=6.0,<7
```

**`requirements-dev.txt`**

```text
-r requirements.txt
pyinstaller>=6.20
pillow>=11.0
```

**`check_env.py`**

```python
# check_env.py
# Controlla se stai usando l'ambiente virtuale giusto e se le librerie sono installate.
import sys

print("Python:", sys.version.split()[0])
print("Eseguibile:", sys.executable)

# Dentro un ambiente virtuale, sys.prefix è diverso da sys.base_prefix
in_venv = sys.prefix != sys.base_prefix
print("Ambiente virtuale attivo?", "SÌ" if in_venv else "NO")

try:
    import customtkinter
    print("customtkinter:", customtkinter.__version__)
except ImportError:
    print("customtkinter: NON installato (esegui: pip install -r requirements.txt)")
```

### Cosa fa questo codice

- `requirements.txt`: dice che il progetto ha bisogno di CustomTkinter 6.x.
- `requirements-dev.txt`: include quello sopra (`-r requirements.txt`) e aggiunge PyInstaller e Pillow.
- `check_env.py`: stampa la versione di Python, dove si trova, se sei dentro un ambiente virtuale (`sys.prefix != sys.base_prefix`) e se `customtkinter` è installato. Il `try / except ImportError` gestisce il caso "non installato".

### Come eseguirlo

Nel terminale di VS Code, nella cartella del progetto, un comando alla volta:

```powershell
python -m venv .venv
```

*(Aspetta qualche secondo: crea la cartella `.venv`.)* Poi attivalo:

```powershell
.venv\Scripts\Activate.ps1
```

Il prompt ora inizia con `(.venv)`. Se VS Code mostra un avviso *"È stato rilevato un nuovo ambiente… vuoi usarlo?"* rispondi **Sì**. Altrimenti premi **Ctrl+Shift+P**, scrivi **"Python: Seleziona interprete"** e scegli quello con `.venv`.

Poi aggiorna pip e installa le librerie:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
python check_env.py
```

Devi vedere (i percorsi saranno i tuoi):

```text
Python: 3.13.16
Eseguibile: C:\Users\Marco\Progetti\FocusFlow\.venv\Scripts\python.exe
Ambiente virtuale attivo? SÌ
customtkinter: 6.0.0
```

Comandi utili da ricordare: `pip list` (librerie installate), `pip show customtkinter` (dettagli), `deactivate` (esci dall'ambiente).

### Errori comuni

- **`Activate.ps1 non può essere caricato… l'esecuzione di script è disabilitata`**: è una protezione di PowerShell. Scrivi una volta sola:

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

  rispondi **S** (o **Y**) e riprova l'attivazione. In alternativa apri un terminale "Command Prompt" e usa `.venv\Scripts\activate.bat`.
- **`pip` non è riconosciuto**: usa sempre `python -m pip install ...` (equivale a `pip`).
- **Hai installato senza `(.venv)` nel prompt**: le librerie sono finite nel Python "globale". Attiva l'ambiente e reinstalla.
- **`ERROR: Could not find a version that satisfies the requirement`**: nome scritto male nel file, oppure manca internet.
- **Non usare `pip freeze > requirements.txt` in PowerShell**: crea un file con codifica UTF-16 che pip non legge. Scrivi i file a mano come qui sopra, oppure usa `pip freeze | Out-File -Encoding utf8 requirements.txt`.
- **Hai spostato o rinominato la cartella del progetto e l'ambiente non va più**: cancella `.venv` e ricrealo (`python -m venv .venv` + `pip install -r requirements.txt`). È proprio il motivo per cui esiste `requirements.txt`.
- **`python check_env.py` dice "NO" o "NON installato"**: l'ambiente non è attivo o l'installazione non è andata a buon fine. Guarda il prompt per `(.venv)`.

### Esercizio

Con l'ambiente attivo, installa una libreria di prova: `pip install rich`. Poi crea `esercizi\step12_rich.py` che stampa una frase colorata e una piccola tabella con i pomodori di due giorni, usando `from rich import print` e `from rich.table import Table`. *(Non aggiungerla a `requirements.txt`: è solo una prova. Soluzione in fondo.)*

### Il progetto finora

FocusFlow ha un **ambiente virtuale** (`.venv`), un file di requisiti e CustomTkinter installato: tutto pronto per la grafica. Prima però mettiamo il codice in sicurezza con Git.

---

## Step 13 — Git e GitHub

**Obiettivo:** salvare la cronologia del progetto con Git e pubblicarlo su GitHub (backup gratuito e portfolio).

### Concetti in 2 minuti

- **Git** è un programma che registra la cronologia del tuo codice, come un "salva partita" con tanti punti di ripristino. Funziona in locale, sul tuo PC.
- **Repository** (o *repo*) = la cartella del progetto controllata da Git.
- **Commit** = un punto di salvataggio con un messaggio ("ho aggiunto X"). Si fa in due tempi: `git add` mette i file nella "scatola da spedire" (*staging*), `git commit` chiude la scatola e la etichetta.
- **GitHub** è un sito gratuito dove puoi mettere online una copia del repository: backup, condivisione e, alla fine, anche il posto da cui distribuire l'app.
- **`.gitignore`** elenca ciò che Git deve **ignorare**: ambiente virtuale, file temporanei, cartelle di build.
- I tuoi dati personali (`tasks.json` ecc.) vivono in `C:\Users\TuoNome\FocusFlow`, fuori dal progetto: non finiranno mai su GitHub.

### A. Installa Git

1. Vai su <https://git-scm.com/download/win> e scarica **Git for Windows (64-bit)**.
2. Installa lasciando **tutte le opzioni predefinite** (clicca sempre *Next*).
3. **Chiudi e riapri VS Code** (così vede il nuovo programma) e verifica nel terminale:

```powershell
git --version
```

### B. Presentati a Git (una volta sola)

Sostituisci nome ed email con i tuoi (saranno visibili nei commit):

```powershell
git config --global user.name "Il Tuo Nome"
git config --global user.email "tua@email.it"
git config --global init.defaultBranch main
```

### Dove lavori

Crea nella cartella `FocusFlow` due file nuovi: **`.gitignore`** (il nome inizia con un punto!) e **`README.md`** (la presentazione del progetto, che GitHub mostra in prima pagina).

### Il codice

**`.gitignore`**

```text
# Ambiente virtuale: si ricrea sempre con "pip install", non va su Git
.venv/

# File temporanei di Python
__pycache__/
*.pyc

# Cartelle create da PyInstaller (le useremo alla fine)
build/
dist/
*.spec

# File dell'editor
.vscode/
```

**`README.md`**

````markdown
# FocusFlow

App desktop gratuita per organizzare la giornata: lista di attività (To-Do)
e timer Pomodoro, tutto in un'unica finestra. Creata in Python come progetto
per imparare passo dopo passo.

## Stato del progetto

- [x] Versione a terminale (menu a testo)
- [ ] Interfaccia grafica con CustomTkinter
- [ ] Timer Pomodoro
- [ ] Eseguibile per Windows (.exe)

## Come avviarla

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
````

### Cosa fa questo codice

- `.gitignore`: ogni riga è un nome o schema da ignorare. `.venv/` (ambiente virtuale), `__pycache__/` e `*.pyc` (file temporanei di Python), `build/`, `dist/`, `*.spec` (prodotti da PyInstaller allo Step 19), `.vscode/` (impostazioni dell'editor). Le righe con `#` sono commenti.
- `README.md`: scritto in **Markdown** (lo stesso formato di questa guida). Descrive il progetto e come avviarlo.

### Come eseguirlo

**1. Il primo commit** (nel terminale, nella cartella del progetto):

```powershell
git init
git add .
git commit -m "Versione a terminale di FocusFlow (step 1-12)"
git log --oneline
```

`git init` crea il repository; `git add .` prepara tutti i file (tranne quelli ignorati); `git commit` salva; `git log --oneline` mostra la cronologia (devi vedere una riga con il tuo messaggio). Con `git status` puoi sempre vedere cosa è cambiato.

**2. Crea il repository su GitHub.** Vai su <https://github.com>, crea un account gratuito, poi **New repository**: nome `focusflow`, scegli *Public* o *Private*, e **NON** spuntare "Add a README", ".gitignore" o "license" (li abbiamo già). Clicca **Create repository** e copia l'indirizzo HTTPS (finisce con `.git`).

**3. Collega e pubblica:**

```powershell
git remote add origin https://github.com/TUO-USERNAME/focusflow.git
git branch -M main
git push -u origin main
```

Si apre una finestra del browser per accedere a GitHub e autorizzare Git: conferma. Poi aggiorna la pagina del repository: vedrai i tuoi file e il README formattato.

**4. La routine da qui in poi**, a fine di ogni step:

```powershell
git add .
git commit -m "Step 14 completato"
git push
```

In VS Code puoi fare lo stesso con il pannello **Controllo del codice sorgente** (Ctrl+Shift+G): scrivi il messaggio, clicca **Commit**, poi **Sincronizza/Push**.

### Errori comuni

- **`git` non è riconosciuto**: dopo l'installazione devi chiudere e riaprire VS Code.
- **`Please tell me who you are` / `Author identity unknown`**: manca la configurazione del punto B.
- **`fatal: not a git repository`**: non sei nella cartella del progetto, oppure non hai fatto `git init`.
- **`! [rejected] ... fetch first`** al push: il repository su GitHub non era vuoto (hai spuntato "Add a README"). Soluzione semplice: elimina il repository su GitHub (Settings → Danger zone) e ricrealo **vuoto**; oppure `git pull origin main --allow-unrelated-histories` e poi di nuovo `git push`.
- **`Authentication failed`**: rifai l'accesso dalla finestra del browser; se non compare, in GitHub genera un *Personal access token* (Settings → Developer settings) e usalo al posto della password.
- **Hai committato `.venv` per sbaglio** (il commit è lentissimo e GitHub si lamenta): il `.gitignore` deve esistere **prima** del `git add .`. Rimedio: `git rm -r --cached .venv`, poi `git commit -m "Tolgo .venv"`.
- **Vuoi annullare le modifiche a un file** dall'ultimo commit: `git restore nome_file.py` (attenzione: le modifiche non salvate in Git vanno perse).

### Esercizio

Modifica `README.md` aggiungendo in fondo una sezione **"Diario di bordo"** con una riga su cosa hai imparato finora. Salva, poi fai `git add .`, `git commit -m "Aggiorno il README"` e `git push`. Controlla su GitHub che la modifica sia comparsa e guarda la cronologia con `git log --oneline`. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow è **sotto controllo di versione** e **pubblicato su GitHub**. D'ora in poi, a fine di ogni step, un commit.

---

## Step 14 — Programmazione a oggetti (OOP): le classi `Task` e `TaskManager`

**Obiettivo:** trasformare i dizionari dei task in **oggetti** con comportamenti propri, il modo più ordinato di preparare il codice per la grafica.

### Concetti in 2 minuti

- Una **classe** è uno **stampo**; un **oggetto** (o *istanza*) è un pezzo prodotto con quello stampo. La classe `Task` descrive come è fatto *ogni* task; `Task("Studiare")` crea un task concreto.
- Dentro una classe ci sono:
  - **attributi**: i dati dell'oggetto (`self.titolo`, `self.fatto`…);
  - **metodi**: funzioni dell'oggetto (`task.cambia_stato()`).
- **`__init__`** è il metodo speciale che si esegue quando crei l'oggetto: prepara gli attributi. **`self`** significa "questo oggetto" e va messo come primo parametro di ogni metodo.
- **`__str__`** decide come appare l'oggetto quando fai `print(oggetto)`.
- Un oggetto può **contenerne altri**: `TaskManager` ha una lista `self.tasks` di oggetti `Task` e sa salvarli, caricarli e contarli.
- **List comprehension**: modo compatto di creare una lista da un'altra. `[t for t in tasks if not t.fatto]` = "la lista dei `t` presi da `tasks`, solo quelli non fatti". Con le graffe `{...}` ottieni un set.
- `a or b` restituisce `a` se non è vuoto, altrimenti `b`: usato per "se non c'è la data, usa quella di oggi".

### Dove lavori

Sostituisci **tutto il contenuto** di `tasks.py` e di `main.py`. `storage.py` **non cambia**.

### Il codice

**`tasks.py`**

```python
# tasks.py  (Step 14: programmazione a oggetti)
# Due classi: Task (un singolo task) e TaskManager (la lista di tutti i task).
from datetime import date

import storage

TASKS_FILE = "tasks.json"
CATEGORIE_BASE = ("Generale", "Studio", "Lavoro", "Casa")


class Task:
    """Un singolo task (una cosa da fare)."""

    def __init__(self, titolo, categoria="Generale", fatto=False, pomodori=0, creato=None):
        # __init__ viene eseguito quando crei un Task: prepara i suoi "attributi"
        self.titolo = titolo
        self.categoria = categoria
        self.fatto = fatto
        self.pomodori = pomodori
        self.creato = creato or date.today().isoformat()   # se creato è vuoto, usa oggi

    def cambia_stato(self):
        """Da fare -> fatto, e viceversa."""
        self.fatto = not self.fatto

    def aggiungi_pomodoro(self):
        self.pomodori += 1

    def to_dict(self):
        """Trasforma il task in un dizionario (serve per salvarlo in JSON)."""
        return {
            "titolo": self.titolo,
            "categoria": self.categoria,
            "fatto": self.fatto,
            "pomodori": self.pomodori,
            "creato": self.creato,
        }

    def __str__(self):
        # __str__ decide come appare il task quando lo stampi con print()
        simbolo = "[x]" if self.fatto else "[ ]"
        return f"{simbolo} {self.titolo} ({self.categoria}) - pomodori: {self.pomodori} - creato: {self.creato}"


class TaskManager:
    """Gestisce l'elenco dei task e li salva su file ad ogni modifica."""

    def __init__(self):
        self.tasks = []
        self.carica()

    # --- salvataggio ---
    def carica(self):
        dati = storage.carica_json(TASKS_FILE, [])
        self.tasks = []
        for d in dati:
            self.tasks.append(Task(
                titolo=d.get("titolo", "(senza titolo)"),
                categoria=d.get("categoria", "Generale"),
                fatto=d.get("fatto", False),
                pomodori=d.get("pomodori", 0),
                creato=d.get("creato"),
            ))

    def salva(self):
        storage.salva_json(TASKS_FILE, [task.to_dict() for task in self.tasks])

    # --- azioni ---
    def aggiungi(self, titolo, categoria="Generale"):
        task = Task(titolo, categoria)
        self.tasks.append(task)
        self.salva()
        return task

    def rimuovi(self, task):
        self.tasks.remove(task)
        self.salva()

    def cambia_stato(self, task):
        task.cambia_stato()
        self.salva()

    def aggiungi_pomodoro(self, task):
        task.aggiungi_pomodoro()
        self.salva()

    def pulisci_completati(self):
        # lista nuova che contiene SOLO i task non ancora fatti
        self.tasks = [task for task in self.tasks if not task.fatto]
        self.salva()

    # --- domande sui dati ---
    def quanti_fatti(self):
        return len([task for task in self.tasks if task.fatto])

    def quanti_da_fare(self):
        return len(self.tasks) - self.quanti_fatti()

    def categorie(self):
        return {task.categoria for task in self.tasks}     # un set, senza doppioni
```

**`main.py`**

```python
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
```

### Cosa fa questo codice

- **`Task`**: costruttore con i suoi attributi, `cambia_stato()` (da fare ↔ fatto), `aggiungi_pomodoro()`, `to_dict()` (per salvare in JSON) e `__str__`.
- **`TaskManager`**: all'avvio **carica da solo** i task dal file e li trasforma in oggetti `Task`; ogni azione (`aggiungi`, `rimuovi`, `cambia_stato`, `aggiungi_pomodoro`, `pulisci_completati`) **salva automaticamente**. Così non devi più ricordarti di chiamare `salva_task`.
- Metodi "di domanda": `quanti_fatti()`, `quanti_da_fare()`, `categorie()`.
- **`main.py`** usa un solo oggetto `manager`. Stesso menu di prima, con una voce in più (7: elimina i completati) e la voce 3 che ora **completa o riapre**.
- I file JSON dei task creati negli step precedenti si leggono ancora senza problemi.

### Come eseguirlo

```powershell
python main.py
```

Prova tutte le voci del menu. In particolare: aggiungi un task, completalo (voce 3), poi riaprilo (voce 3 ancora), poi completalo ed eliminalo con la voce 7. Il riepilogo finale diventa:

```text
A presto Marco! Da fare: 1 | fatti: 0.
```

### Errori comuni

- **`AttributeError: 'Task' object has no attribute 'titolo'`**: nel costruttore hai scritto `titolo = titolo` invece di `self.titolo = titolo`, o c'è un errore di battitura nel nome.
- **`TypeError: Task.cambia_stato() takes 0 positional arguments but 1 was given`**: hai dimenticato `self` come primo parametro del metodo.
- **`NameError` dentro un metodo**: per usare un attributo devi scrivere `self.fatto`, non solo `fatto`.
- **`__init__` non viene chiamato**: controlla di aver scritto **due** trattini bassi prima e dopo (`__init__`).
- **I metodi non sono "dentro" la classe**: indentazione sbagliata. Ogni `def` della classe va spostato di 4 spazi a destra.

### Esercizio

In `esercizi\step14.py`: crea una classe `Abitudine` con `nome` e `giorni_di_fila` (parte da 0), i metodi `segna_oggi()` e `azzera()`, e `__str__` che stampa per esempio `Leggere 10 pagine: 2 giorni di fila`. Crea due abitudini, falle evolvere e stampale. *(Soluzione in fondo.)*

### Il progetto finora

Il cuore di FocusFlow (`Task`, `TaskManager`, `storage`) è **pronto e indipendente dall'interfaccia**. Dall'altra parte, `main.py` è solo una "facciata a testo". Nel prossimo step mettiamo una facciata grafica. Fai il commit: `git add .`, `git commit -m "Step 14: classi"`, `git push`.


---

# PARTE C — L'app grafica (step 15–18)

Ora arriva la parte più bella: FocusFlow diventa una vera app con finestre, bottoni e un timer. Useremo **CustomTkinter**, una libreria gratuita costruita su **Tkinter** (già incluso in Python) che offre widget moderni, con tema chiaro/scuro.

## Step 15 — La prima finestra: aggiungere e mostrare i task

**Obiettivo:** aprire la finestra di FocusFlow, con una casella per scrivere un task, un bottone per aggiungerlo e la lista dei task salvati.

### Concetti in 2 minuti

- **Interfaccia grafica (GUI)**: finestre con **widget** (bottoni, etichette, caselle di testo…). Con CustomTkinter i widget si chiamano `CTkButton`, `CTkLabel`, `CTkEntry`…
- **Programmazione a eventi**: il programma non segue più un copione dall'alto in basso. Dopo aver costruito la finestra chiami **`mainloop()`**: un ciclo infinito che *aspetta* che tu faccia qualcosa (un clic, un tasto…).
- **Callback**: la funzione che deve partire quando succede un evento. Si passa con `command=nome_funzione` **senza parentesi**: stai dicendo "chiama questa quando clicchi", non "chiamala adesso".
- **Posizionare i widget**: `pack()` li impila uno dopo l'altro (semplice); `grid(row=..., column=...)` li mette in una griglia di righe e colonne (più preciso). `sticky="ew"` fa allargare un widget da est a ovest; `weight=1` dice a una riga/colonna di prendersi lo spazio libero. **In uno stesso contenitore usa o `pack` o `grid`, mai entrambi.**
- **Ereditarietà**: `class TaskPanel(ctk.CTkFrame):` significa "`TaskPanel` è un `CTkFrame` (un riquadro) con in più le nostre cose". `super().__init__(...)` prepara prima la parte del riquadro standard.
- **`global`** dentro una funzione serve a modificare una variabile creata fuori (lo vedrai in `prova_gui.py`).
- **Colori con due valori** `(chiaro, scuro)`: CustomTkinter sceglie il primo con il tema chiaro e il secondo con il tema scuro.

### Dove lavori

1. **Rinomina `main.py` in `cli.py`** (la versione a terminale resta come archivio; non cambiare nulla dentro).
2. Crea 5 file nuovi: `prova_gui.py` (un esperimento), `style.py`, `ui_tasks.py`, `app.py` e un **nuovo `main.py`**.

### Il codice

**`prova_gui.py`** *(non fa parte di FocusFlow: serve solo a capire come funziona una finestra)*

```python
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
```

**`style.py`**

```python
# style.py
# Colori e font di FocusFlow in un posto solo: se vuoi cambiare lo stile, cambi qui.
# I colori con due valori sono (modo chiaro, modo scuro).

ACCENT = "#E5533D"          # rosso pomodoro
ACCENT_HOVER = "#C94330"    # lo stesso, più scuro (quando passi il mouse sopra)
SUCCESS = "#3BA55D"         # verde (pause e task completati)
SUCCESS_HOVER = "#2F8A4B"

BG = ("#F2F3F5", "#16171A")      # sfondo della finestra
CARD = ("#FFFFFF", "#212328")    # sfondo dei "riquadri"
ROW = ("#F4F5F7", "#2B2D33")     # sfondo di ogni riga della lista
MUTED = ("#6B7280", "#9CA3AF")   # testo secondario (grigio)

FONT_TITLE = ("Roboto", 22, "bold")
FONT_TEXT = ("Roboto", 15)
FONT_SMALL = ("Roboto", 12)
```

**`ui_tasks.py`**

```python
# ui_tasks.py  (Step 15)
# Il pannello con la lista dei task: una "classe" che è un riquadro (CTkFrame).
import customtkinter as ctk

import style


class TaskPanel(ctk.CTkFrame):
    def __init__(self, master, manager):
        super().__init__(master, corner_radius=16, fg_color=style.CARD)
        self.manager = manager

        # Layout a griglia: la colonna 0 si allarga, la riga 2 (la lista) si allunga
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        titolo = ctk.CTkLabel(self, text="Le tue attività", font=style.FONT_TITLE)
        titolo.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="w")

        self.entry = ctk.CTkEntry(self, placeholder_text="Cosa devi fare?", height=40)
        self.entry.grid(row=1, column=0, padx=(20, 10), pady=(0, 10), sticky="ew")
        self.entry.bind("<Return>", self.on_add)           # premere Invio = clic su Aggiungi

        self.add_button = ctk.CTkButton(
            self, text="Aggiungi", width=100, height=40,
            fg_color=style.ACCENT, hover_color=style.ACCENT_HOVER,
            command=self.on_add,
        )
        self.add_button.grid(row=1, column=1, padx=(0, 20), pady=(0, 10))

        # Un contenitore che scorre quando ci sono tanti task
        self.lista = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.lista.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 15), sticky="nsew")

        self.refresh()

    def on_add(self, event=None):
        """Chiamata quando premi il bottone o Invio."""
        titolo = self.entry.get().strip()
        if titolo == "":
            return
        self.manager.aggiungi(titolo)
        self.entry.delete(0, "end")        # svuota la casella di testo
        self.refresh()

    def refresh(self):
        """Ridisegna la lista: cancella le righe vecchie e le ricrea."""
        for widget in self.lista.winfo_children():
            widget.destroy()

        if not self.manager.tasks:
            vuoto = ctk.CTkLabel(
                self.lista, text="Nessuna attività. Aggiungine una qui sopra!",
                font=style.FONT_TEXT, text_color=style.MUTED,
            )
            vuoto.pack(pady=40)
            return

        for task in self.manager.tasks:
            simbolo = "✓" if task.fatto else "•"
            riga = ctk.CTkLabel(
                self.lista, text=f"{simbolo}  {task.titolo}",
                font=style.FONT_TEXT, anchor="w",
            )
            riga.pack(fill="x", padx=10, pady=4)
```

**`app.py`**

```python
# app.py  (Step 15)
# La finestra principale di FocusFlow.
import customtkinter as ctk

import style
from tasks import TaskManager
from ui_tasks import TaskPanel


class FocusFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=style.BG)
        ctk.set_appearance_mode("system")      # segue il tema chiaro/scuro di Windows

        self.title("FocusFlow")
        self.geometry("560x680")
        self.minsize(460, 520)

        self.manager = TaskManager()           # la stessa classe dello step 14!

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tasks_panel = TaskPanel(self, self.manager)
        self.tasks_panel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
```

**`main.py`** *(nuovo)*

```python
# main.py  (Step 15)
# Il punto di partenza dell'app: avvia la finestra.
import customtkinter as ctk

from app import FocusFlowApp


def main():
    ctk.set_default_color_theme("blue")
    app = FocusFlowApp()
    app.mainloop()          # la finestra resta aperta finché non la chiudi


if __name__ == "__main__":
    main()
```

### Cosa fa questo codice

- **`prova_gui.py`**: crea una finestra (`ctk.CTk()`), un'etichetta e un bottone con `command=al_click`. Ogni clic chiama `al_click`, che aumenta il contatore e cambia il testo con `.configure(text=...)`.
- **`style.py`**: un posto solo per i colori (rosso pomodoro `#E5533D`, verde, grigi) e i font. Se vuoi cambiare lo stile, cambi qui.
- **`ui_tasks.py`**: la classe `TaskPanel` è un riquadro con titolo, casella di testo (`CTkEntry`), bottone **Aggiungi** e una lista scorrevole (`CTkScrollableFrame`).
  - `on_add` legge il testo, chiede al `manager` di aggiungere il task, svuota la casella e ridisegna.
  - Premere **Invio** nella casella fa la stessa cosa (`bind("<Return>", ...)`).
  - `refresh()` **cancella** le righe vecchie (`winfo_children()` e `destroy()`) e le **ricrea** dal `manager`: è lo schema che useremo sempre.
- **`app.py`**: la finestra principale `FocusFlowApp` (eredita da `ctk.CTk`). Crea il `TaskManager` dello Step 14 (**stessa classe, zero modifiche**) e dentro la finestra mette il `TaskPanel`.
- **`main.py`**: sceglie il tema colori (`"blue"`), crea la finestra e chiama `mainloop()`.

### Come eseguirlo

Prima l'esperimento (con l'ambiente virtuale attivo, `(.venv)` nel prompt):

```powershell
python prova_gui.py
```

Si apre una piccola finestra: clicca il bottone e guarda il contatore salire. Chiudila, poi avvia FocusFlow:

```powershell
python main.py
```

Si apre la finestra di FocusFlow (chiara o scura, a seconda del tema di Windows): un riquadro con titolo **"Le tue attività"**, la casella di testo, il bottone rosso **Aggiungi** e la lista, con un segno **✓** davanti ai task completati e **•** davanti agli altri. Scrivi un task, premi Invio: compare in lista. **Chiudi e riapri**: i task ci sono ancora (li salva `TaskManager`).

### Errori comuni

- **`ModuleNotFoundError: No module named 'customtkinter'`**: l'ambiente virtuale non è attivo (manca `(.venv)` nel prompt) o non hai installato i requisiti. Rivedi lo Step 12.
- **La finestra si apre e si chiude subito**: manca `mainloop()`.
- **L'azione parte appena avvii il programma, non al clic**: hai scritto `command=al_click()` con le parentesi. Deve essere `command=al_click`.
- **Il widget non compare**: ti sei dimenticato `.pack()` o `.grid()`.
- **`_tkinter.TclError: cannot use geometry manager pack inside ... which already has slaves managed by grid`**: nello stesso contenitore stai mischiando `pack` e `grid`. Sceglierne uno.
- **Se rinomini `main.py` in `cli.py` e poi vuoi la versione a testo**: `python cli.py` funziona ancora.

### Esercizio

Copia `prova_gui.py` in `esercizi\prova_gui2.py` e aggiungi un secondo bottone **"Azzera"** che riporta il contatore a 0 e scrive "Contatore azzerato" nell'etichetta. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow è una **vera finestra** che mostra e salva i task. Commit consigliato: `git add .`, `git commit -m "Step 15: prima finestra"`, `git push`.

---

## Step 16 — Task completabili, eliminabili e filtrabili

**Obiettivo:** rendere la lista davvero utile: spunta per completare, categorie, filtri, elimina, contatori e "pulisci".

### Concetti in 2 minuti

- Nuovi widget: **`CTkCheckBox`** (la spunta), **`CTkOptionMenu`** (menu a tendina), **`CTkSegmentedButton`** (i pulsanti affiancati dei filtri).
- **Callback con argomento**: il bottone × di ogni riga deve sapere *quale* task eliminare. Si usa una **lambda**, una mini-funzione senza nome: `command=lambda t=task: self.on_delete(t)`. Il `t=task` è importante: "fotografa" il task di *quel* giro del ciclo (senza, tutte le righe userebbero l'ultimo task).
- **Callback verso l'alto (`on_change`)**: il pannello non sa chi altro ha bisogno di sapere che i task sono cambiati (lo servirà al timer, Step 17). Riceve quindi una funzione e la chiama quando cambia qualcosa: "avvisa chi è interessato".
- **`ctk.CTkFont(..., overstrike=True)`** barra il testo (task completato).
- **`@staticmethod`**: metodo che sta dentro la classe ma non usa `self` (`accorcia` taglia i titoli troppo lunghi).
- Riquadri dentro riquadri: ogni riga della lista è un `CTkFrame` con checkbox, categoria, pomodori e bottone ×.

### Dove lavori

Sostituisci **tutto il contenuto** di `ui_tasks.py` e di `app.py`. Gli altri file non cambiano.

### Il codice

**`ui_tasks.py`**

```python
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
```

**`app.py`**

```python
# app.py  (Step 15)
# La finestra principale di FocusFlow.
import customtkinter as ctk

import style
from tasks import TaskManager
from ui_tasks import TaskPanel


class FocusFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=style.BG)
        ctk.set_appearance_mode("system")      # segue il tema chiaro/scuro di Windows

        self.title("FocusFlow")
        self.geometry("620x700")
        self.minsize(560, 520)

        self.manager = TaskManager()           # la stessa classe dello step 14!

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tasks_panel = TaskPanel(self, self.manager)
        self.tasks_panel.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
```

### Cosa fa questo codice

- **Riga 1 del pannello**: casella di testo + menu delle categorie (da `CATEGORIE_BASE` di `tasks.py`) + bottone **Aggiungi**.
- **Filtri** "Tutte / Da fare / Fatte": `on_filter` salva il filtro scelto; `task_visibili()` restituisce solo i task che lo rispettano (con list comprehension).
- **`refresh()`** ridisegna la lista e aggiorna il contatore in basso ("2 da fare · 1 completate").
- **`crea_riga(task)`** costruisce una riga: la spunta (barrata e grigia se fatto), la categoria, i pomodori (rossi, solo se > 0) e il ×.
- **`on_toggle`, `on_delete`, `on_pulisci`, `on_add`** chiamano il `manager` (che salva da solo) e poi `aggiorna_tutto()`: ridisegna e avvisa tramite `on_change`.
- **`app.py`** cambia solo la dimensione della finestra: ha spazio per le nuove colonne.

### Come eseguirlo

```powershell
python main.py
```

Prova tutto: aggiungi task con categorie diverse, spunta e deseleziona, usa i filtri in alto, elimina con la ×, clicca **Pulisci completate**. I task completati appaiono in grigio e barrati; chiudi e riapri: lo stato resta.

### Errori comuni

- **Spunti un task e se ne modifica un altro (o sempre l'ultimo)**: hai scritto `lambda: self.on_toggle(task)` senza `t=task`. Usa `lambda t=task: self.on_toggle(t)`.
- **La lista non si aggiorna dopo un'azione**: manca la chiamata a `self.refresh()` (o `aggiorna_tutto()`).
- **`_tkinter.TclError: bad window path name`**: stai usando un widget che hai già distrutto con `destroy()`. Dopo il ridisegno, usa i widget nuovi.
- **Il testo nel menu categorie è invisibile in tema scuro**: servono colori a due valori `(chiaro, scuro)`, come in `text_color=("gray10", "gray90")`.
- **`AttributeError: 'Task' object has no attribute 'completato'`**: usa i nomi veri degli attributi: `fatto`, `titolo`, `categoria`, `pomodori`.

### Esercizio

Aggiungi un bottone **"Segna tutte"** accanto a "Pulisci completate" che segna *tutte* le attività come fatte. Ti servono: un metodo `segna_tutti_fatti()` in `TaskManager` e un bottone + un metodo `on_tutti` in `TaskPanel`. *(Soluzione in fondo.)*

### Il progetto finora

La lista dei task è **completa**: aggiungi, spunta, filtra, elimina, categorie, contatori. Commit: `git commit -m "Step 16: lista task completa"`.

---

## Step 17 — Il timer Pomodoro

**Obiettivo:** aggiungere a destra un timer Pomodoro che conta i secondi, suona a fine fase, assegna i pomodori al task scelto e li registra nelle statistiche.

### Concetti in 2 minuti

- **Logica separata dalla grafica.** Scriviamo prima `pomodoro.py`: una classe `PomodoroTimer` che sa solo di numeri (fase, secondi rimasti, regole: ogni 4 pomodori pausa lunga). Non conosce finestre né bottoni. Il vantaggio: è semplice da capire e da provare.
- **Fasi del timer**: `focus` → `pausa` → `focus` → … → ogni 4° pomodoro `lunga`. Alla fine di ogni fase il timer **si ferma** ed è l'utente a premere *Avvia* per la fase successiva.
- **Come far scorrere il tempo in una finestra**: **non** si usa `time.sleep()` (bloccherebbe la finestra: sembrerebbe congelata). Si usa **`self.after(1000, funzione)`**: "tra 1000 millisecondi chiama questa funzione". Ogni chiamata (un **tick**) richiede il tick successivo. `after_cancel(id)` annulla un tick già programmato.
- **`winsound`** è un modulo che esiste solo su Windows (suono di sistema). Il `try / except ImportError` lo importa se c'è; altrimenti si usa il beep di Tk.
- **File JSON per impostazioni e statistiche**: `settings.py` (durate del timer, tema) e `stats.py` (pomodori per giorno, come dizionario `{"2026-10-02": 3}`). Usano il nostro `storage.py`.
- `divmod(754, 60)` restituisce `(12, 34)`: minuti e secondi. `f"{x:02d}"` scrive un numero con almeno 2 cifre (`05`).
- **`CTkProgressBar`**: barra di avanzamento; `set(0.4)` la riempie al 40%.

### Dove lavori

Crea **4 file nuovi**: `pomodoro.py`, `settings.py`, `stats.py`, `ui_timer.py`. Poi **sostituisci tutto** `app.py`. Gli altri non cambiano.

### Il codice

**`pomodoro.py`**

```python
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
```

**`settings.py`**

```python
# settings.py
# Le impostazioni dell'app (durate del timer, tema), salvate in settings.json.
import storage

SETTINGS_FILE = "settings.json"

DEFAULTS = {
    "focus": 25,        # minuti di concentrazione
    "pausa": 5,         # minuti di pausa breve
    "lunga": 15,        # minuti di pausa lunga
    "tema": "system",   # "system", "light" oppure "dark"
}


def carica_settings():
    """Parte dai valori predefiniti e sovrascrive quelli trovati nel file."""
    settings = dict(DEFAULTS)                      # copia del dizionario
    salvate = storage.carica_json(SETTINGS_FILE, {})
    if isinstance(salvate, dict):                  # sicurezza: deve essere un dizionario
        settings.update(salvate)
    if settings["tema"] not in ("system", "light", "dark"):
        settings["tema"] = DEFAULTS["tema"]        # valore strano nel file? torna al predefinito
    return settings


def salva_settings(settings):
    storage.salva_json(SETTINGS_FILE, settings)
```

**`stats.py`**

```python
# stats.py
# Statistiche: quanti pomodori hai completato ogni giorno (in stats.json).
from datetime import date, timedelta

import storage

STATS_FILE = "stats.json"


def carica_stats():
    """Restituisce un dizionario come {"2026-10-02": 3, "2026-10-01": 5}."""
    dati = storage.carica_json(STATS_FILE, {})
    return dati if isinstance(dati, dict) else {}


def registra_pomodoro():
    """Aggiunge 1 ai pomodori di oggi."""
    dati = carica_stats()
    oggi = date.today().isoformat()
    dati[oggi] = dati.get(oggi, 0) + 1
    storage.salva_json(STATS_FILE, dati)


def pomodori_oggi():
    return carica_stats().get(date.today().isoformat(), 0)


def pomodori_totali():
    return sum(carica_stats().values())


def ultimi_giorni(quanti=7):
    """Lista di tuple (data, pomodori) degli ultimi giorni, dal più vecchio a oggi."""
    dati = carica_stats()
    oggi = date.today()
    risultato = []
    for indietro in range(quanti - 1, -1, -1):
        giorno = oggi - timedelta(days=indietro)
        risultato.append((giorno, dati.get(giorno.isoformat(), 0)))
    return risultato
```

**`ui_timer.py`**

```python
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
```

**`app.py`**

```python
# app.py  (Step 17)
# La finestra principale: a sinistra i task, a destra il timer.
import customtkinter as ctk

import style
from settings import carica_settings
from tasks import TaskManager
from ui_tasks import TaskPanel
from ui_timer import TimerPanel


class FocusFlowApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=style.BG)
        ctk.set_appearance_mode("system")

        self.title("FocusFlow")
        self.geometry("1000x680")
        self.minsize(900, 600)

        self.manager = TaskManager()
        self.settings = carica_settings()

        # Due colonne: i task (più larga) e il timer
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.tasks_panel = TaskPanel(self, self.manager, on_change=self.on_tasks_changed)
        self.tasks_panel.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="nsew")

        self.timer_panel = TimerPanel(
            self, self.manager, self.settings, on_pomodoro=self.on_pomodoro_done,
        )
        self.timer_panel.grid(row=0, column=1, padx=(10, 20), pady=20, sticky="nsew")

    def on_tasks_changed(self):
        """I task sono cambiati: aggiorna il menu del timer."""
        self.timer_panel.aggiorna_lista_task()

    def on_pomodoro_done(self):
        """Un pomodoro è finito: ridisegna la lista (il contatore dei pomodori)."""
        self.tasks_panel.refresh()
```

### Cosa fa questo codice

- **`PomodoroTimer`**: `avvia()`, `ferma()`, `reset()`, `salta()`; `tick()` toglie un secondo e, se la fase finisce, **restituisce il nome della fase finita** (o `None`). `testo_tempo()` dà "24:59", `progresso()` un numero da 0 a 1.
- **`settings.py`**: parte da `DEFAULTS` (25/5/15 minuti, tema "system") e vi "sovrappone" ciò che trova nel file (`dict.update`).
- **`stats.py`**: `registra_pomodoro()` aggiunge 1 ai pomodori di oggi; `pomodori_oggi()`, `pomodori_totali()`; `ultimi_giorni(7)` restituisce una **lista di tuple** `(data, pomodori)` per il grafico dello Step 18.
- **`TimerPanel`** (`ui_timer.py`): costruisce l'interfaccia (menu del task, nome della fase, grande orologio, barra, bottoni *Avvia/Pausa*, *Reset*, *Salta*, contatore di oggi) e **collega il timer alla grafica**:
  - `_tick()` viene chiamato ogni secondo da `after`, fa avanzare il timer e aggiorna la schermata (`aggiorna()`);
  - quando finisce un *focus*: suona, registra il pomodoro nelle statistiche, lo aggiunge al **task scelto nel menu** e avvisa l'app con `on_pomodoro`;
  - `aggiorna_lista_task()` riempie il menu con i task ancora da fare.
- **`app.py`**: due colonne, **task a sinistra** e **timer a destra**. Fa da "centralino": quando i task cambiano aggiorna il menu del timer; quando finisce un pomodoro ridisegna la lista (il contatore dei pomodori del task).

### Come eseguirlo

**Per provarlo in fretta**, apri `settings.py` e cambia temporaneamente `"focus": 25` in `"focus": 1` (un minuto). *Ricordati di rimetterlo a 25: allo Step 18 lo farai con un cursore.*

```powershell
python main.py
```

1. A destra, nel menu in alto, scegli un task.
2. Clicca **Avvia**: il bottone diventa **Pausa**, l'orologio scende e la barra rossa si riempie.
3. Dopo un minuto: **suono**, messaggio *"Pomodoro completato! Fai una pausa."*, il task nella lista mostra **1 pomodoro**, e in basso leggi **"Pomodori di oggi: 1"**. Ora la fase è *PAUSA BREVE* (barra verde): premi **Salta** per tornare al focus.
4. Controlla il file `C:\Users\TuoNome\FocusFlow\stats.json`: c'è la data di oggi con il numero di pomodori.

### Errori comuni

- **L'orologio va il doppio più veloce**: stai avviando due catene di `after`. `_pianifica_tick()` prima chiama `_ferma_tick()` proprio per evitarlo: non rimuoverla.
- **La finestra si "congela"**: hai usato `time.sleep()` o un ciclo lungo dentro la grafica. Nelle finestre usa `after`.
- **Non senti il suono**: `winsound.MessageBeep()` usa il suono di sistema di Windows. Controlla volume e *Impostazioni → Sistema → Suono*.
- **Il pomodoro non viene conteggiato sul task**: nel menu era selezionato *"Nessun task (focus libero)"*. In quel caso conta solo nelle statistiche.
- **`AttributeError: 'TimerPanel' object has no attribute 'timer'`**: l'ordine delle righe nel costruttore è cambiato: `self.timer = PomodoroTimer(...)` deve venire prima di usare `self.timer`.
- **`KeyError: 'focus'`**: stai leggendo un dizionario di impostazioni senza `DEFAULTS`. Lascia `carica_settings()` com'è.

### Esercizio

Fai comparire il tempo che scorre **nel titolo della finestra** (per esempio `24:59 · FocusFlow`) mentre il timer è in corso, così lo vedi anche dalla barra delle applicazioni a finestra ridotta. *(Suggerimento: alla fine di `aggiorna()` in `ui_timer.py`, `self.winfo_toplevel()` restituisce la finestra principale e `.title("...")` ne cambia il titolo. Soluzione in fondo.)*

### Il progetto finora

FocusFlow ha un **timer Pomodoro funzionante**, collegato ai task e alle statistiche. Commit: `git commit -m "Step 17: timer Pomodoro"`.

---

## Step 18 — Impostazioni, statistiche e tema scuro

**Obiettivo:** rifinire l'app con tre schede a destra (Timer, Statistiche, Impostazioni), cursori per le durate, grafico degli ultimi 7 giorni e tema chiaro/scuro salvato.

### Concetti in 2 minuti

- **`CTkTabview`**: un contenitore a schede; `tabs.add("Nome")` crea una scheda e `tabs.tab("Nome")` restituisce il suo riquadro dove mettere i widget.
- **`CTkSlider`**: un cursore. Con `from_`, `to`, `number_of_steps` scegli i valori; la callback riceve il valore **come float** (per esempio `25.0`): lo trasformiamo in intero con `int(round(valore))`.
- **`ctk.set_appearance_mode("dark" | "light" | "system")`** cambia **subito** l'aspetto di tutta l'app.
- **Dizionario di traduzione**: `TEMI = {"Scuro": "dark", ...}` collega il testo mostrato al valore salvato.
- **Il "grafico"** degli ultimi 7 giorni è fatto con 7 barre di avanzamento verticali: l'altezza è `pomodori / massimo`. Il giorno della settimana viene da `data.weekday()` (0 = lunedì).
- **Pattern "centralino"**: i pannelli non si conoscono tra loro; la finestra `FocusFlowApp` riceve gli avvisi (`on_tasks_changed`, `on_pomodoro_done`, `on_settings_changed`) e aggiorna chi serve. Così ogni pannello resta indipendente e facile da cambiare.

### Dove lavori

Crea **2 file nuovi**: `ui_settings.py` e `ui_stats.py`. **Sostituisci tutto** `app.py`. Se allo Step 17 avevi messo `"focus": 1` in `settings.py`, **rimettilo a `25`**.

### Il codice

**`ui_settings.py`**

```python
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
```

**`ui_stats.py`**

```python
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
```

**`app.py`**

```python
# app.py  (Step 18)
# La finestra principale: intestazione, task a sinistra, schede (timer/statistiche/impostazioni) a destra.
import customtkinter as ctk

import style
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

    # ---------- Callback: i pannelli si "parlano" tramite la finestra ----------

    def on_tasks_changed(self):
        self.timer_panel.aggiorna_lista_task()
        self.stats_panel.aggiorna()

    def on_pomodoro_done(self):
        self.tasks_panel.refresh()
        self.stats_panel.aggiorna()

    def on_settings_changed(self):
        self.timer_panel.applica_durate(self.settings)
```

### Cosa fa questo codice

- **`SettingsPanel`**: tre cursori (focus 1–60 min, pausa breve 1–30, pausa lunga 5–45) creati da un ciclo su una lista di tuple, e un selettore **Sistema / Chiaro / Scuro**. Ogni modifica viene **salvata** in `settings.json` (`salva_settings`) e comunicata all'app.
- **`StatsPanel`**: mostra i pomodori di oggi in grande, il totale, i task completati e il **grafico degli ultimi 7 giorni** con il numero sopra ogni barra e il nome del giorno sotto.
- **`app.py`**: aggiunge l'**intestazione** (nome in rosso e sottotitolo), legge le impostazioni all'avvio (compreso il **tema salvato**), crea il `CTkTabview` con le tre schede e collega i pannelli tramite le callback.

### Come eseguirlo

```powershell
python main.py
```

1. Vai nella scheda **Impostazioni**, porta **Focus** a 1 minuto, poi torna su **Timer**: l'orologio mostra `01:00`. (Se il timer era in corso premi **Reset**: le nuove durate si applicano a timer fermo.)
2. Avvia un pomodoro e aspettalo. Poi apri **Statistiche**: il numero di oggi cresce e la barra di oggi si alza.
3. In **Impostazioni** scegli **Scuro**: cambia tutto subito. **Chiudi e riapri l'app**: tema e durate sono ricordati.
4. Rimetti **Focus a 25**.
5. Apri la cartella `C:\Users\TuoNome\FocusFlow`: ora contiene `tasks.json`, `settings.json` e `stats.json`.

### Errori comuni

- **Una scheda è vuota**: manca `.pack(fill="both", expand=True)` del pannello dentro la scheda.
- **Cambi le durate ma l'orologio non cambia**: il timer è in corso. Premi **Reset** (o aspetta la fine della fase).
- **Il grafico è tutto vuoto**: non hai ancora completato pomodori. Fai un pomodoro da 1 minuto per vederlo.
- **Qualche elemento resta chiaro in tema scuro**: usa colori a due valori `(chiaro, scuro)`, come in `style.py`.
- **`json.JSONDecodeError` avviando l'app**: un file JSON è stato modificato a mano e si è rotto. Cancella quel file (per esempio `settings.json`) e riparte con i valori predefiniti.

### Esercizio

Nella scheda **Statistiche**, mostra anche la **media di pomodori al giorno negli ultimi 7 giorni** (per esempio *"Media ultimi 7 giorni: 3.4 al giorno"*). Aggiungi una funzione `media_ultimi_giorni()` in `stats.py` e una riga nel testo di `StatsPanel.aggiorna()`. *(Soluzione in fondo.)*

### Il progetto finora

**L'app è completa**: task, timer, statistiche, impostazioni, tema chiaro/scuro, dati salvati. Rimane da trasformarla in un programma che parte con un doppio clic. Commit: `git commit -m "Step 18: impostazioni e statistiche"` e `git push`.


---

# PARTE D — Dall'app all'eseguibile (step 19–20)

L'app funziona, ma per usarla serve ancora Python. Ora la trasformiamo in un programma che parte con un doppio clic e che puoi passare a chiunque.

## Step 19 — Icona ed eseguibile (`.exe`) con PyInstaller

**Obiettivo:** creare la cartella `dist\FocusFlow` con `FocusFlow.exe`, funzionante su un PC senza Python.

### Concetti in 2 minuti

- **PyInstaller** (gratuito) impacchetta insieme il tuo codice, l'interprete Python e le librerie in una cartella: l'utente non deve installare nulla.
- Opzioni che useremo:
  - `--windowed`: **niente finestra nera** del terminale dietro l'app;
  - `--name FocusFlow`: nome dell'app;
  - `--icon assets\icon.ico`: icona del file `.exe`;
  - `--collect-all customtkinter`: include tutti i file della libreria (temi, font): senza, l'app si aprirebbe vuota o non partirebbe;
  - `--add-data "assets;assets"`: copia la cartella `assets` (con l'icona) dentro l'app. Su Windows i due pezzi sono separati da `;`;
  - `--noconfirm --clean`: sovrascrive senza chiedere e ripulisce la cache.
- Di default PyInstaller crea una **cartella** (`--onedir`): si avvia in fretta ed è meno sospettata dagli antivirus. Esiste anche `--onefile` (un solo `.exe`), ma è più lento a partire e più soggetto ai falsi allarmi: in questa guida usiamo la cartella.
- **File dentro l'`.exe`**: quando l'app è impacchettata, i file vengono scompattati altrove e `__file__` non punta più dove pensi. Il modulo `resources.py` con `resource_path()` trova il percorso giusto sia da Python sia dall'`.exe`.
- **File `.ico`**: l'icona di Windows, che contiene più dimensioni (16, 32, 48… 256 px). La disegniamo con **Pillow** (libreria gratuita per le immagini).
- **File `.bat`**: un elenco di comandi di Windows da eseguire uno dopo l'altro (`REM` = commento).
- CustomTkinter, appena la finestra parte, imposta una sua icona; per questo cambiamo la nostra icona con un piccolo ritardo, `self.after(300, ...)`.

### Dove lavori

1. Nel terminale, con l'ambiente attivo, installa gli strumenti per costruire l'app (sono in `requirements-dev.txt`):

```powershell
pip install -r requirements-dev.txt
```

2. Crea 3 file nuovi: `resources.py`, `make_icon.py`, `build.bat`.
3. **Sostituisci tutto** `app.py`.

### Il codice

**`resources.py`**

```python
# resources.py
# Trova i file inclusi nell'app (come l'icona), sia quando lanci "python main.py"
# sia quando l'app è diventata un .exe creato con PyInstaller.
import sys
from pathlib import Path


def resource_path(relativo):
    """Restituisce il percorso completo di un file, per esempio resource_path("assets/icon.ico")."""
    # Dentro l'.exe, PyInstaller scompatta i file in una cartella indicata da sys._MEIPASS
    base = getattr(sys, "_MEIPASS", None)
    if base is None:
        base = Path(__file__).parent       # esecuzione normale: la cartella di questo file
    return Path(base) / relativo
```

**`make_icon.py`**

```python
# make_icon.py
# Disegna l'icona di FocusFlow con Pillow e la salva in assets/icon.ico (e icon.png).
# Si lancia una volta sola:  python make_icon.py
from pathlib import Path

from PIL import Image, ImageDraw

ROSSO = (229, 83, 61, 255)
BIANCO = (255, 255, 255, 255)


def disegna(lato):
    img = Image.new("RGBA", (lato, lato), (0, 0, 0, 0))     # sfondo trasparente
    d = ImageDraw.Draw(img)

    margine = lato // 16
    d.rounded_rectangle(
        (margine, margine, lato - margine, lato - margine),
        radius=lato // 4, fill=ROSSO,
    )

    centro = lato / 2
    raggio = lato * 0.28
    spessore = max(2, lato // 14)
    d.ellipse(                                               # il quadrante dell'orologio
        (centro - raggio, centro - raggio, centro + raggio, centro + raggio),
        outline=BIANCO, width=spessore,
    )
    d.line((centro, centro, centro, centro - raggio * 0.7), fill=BIANCO, width=spessore)   # lancetta lunga
    d.line((centro, centro, centro + raggio * 0.5, centro), fill=BIANCO, width=spessore)   # lancetta corta
    return img


def main():
    cartella = Path(__file__).parent / "assets"
    cartella.mkdir(exist_ok=True)

    grande = disegna(256)
    grande.save(cartella / "icon.png")
    grande.save(
        cartella / "icon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )
    print("Icona creata in:", cartella)


if __name__ == "__main__":
    main()
```

**`app.py`**

```python
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
```

**`build.bat`**

```bat
@echo off
REM build.bat - crea l'eseguibile di FocusFlow (da lanciare con l'ambiente virtuale attivo)

echo === 1/3 Creo l'icona ===
python make_icon.py

echo === 2/3 Creo l'eseguibile con PyInstaller ===
python -m PyInstaller --noconfirm --clean --windowed --name FocusFlow --icon assets\icon.ico --collect-all customtkinter --add-data "assets;assets" main.py

echo === 3/3 Fatto! ===
echo Trovi l'app in:  dist\FocusFlow\FocusFlow.exe
pause
```

### Cosa fa questo codice

- **`resources.py`**: `resource_path("assets/icon.ico")` restituisce il percorso del file, che tu stia lanciando `python main.py` oppure l'`.exe` (PyInstaller mette i file in `sys._MEIPASS`).
- **`make_icon.py`**: disegna con Pillow un quadrato rosso arrotondato con un orologio bianco, a più dimensioni, e lo salva in `assets\icon.ico` (e `icon.png`).
- **`app.py`**: aggiunge `imposta_icona()`, che su Windows assegna l'icona alla finestra (barra del titolo e barra delle applicazioni). Il resto non cambia.
- **`build.bat`**: crea l'icona, lancia PyInstaller con le opzioni descritte sopra e ti dice dove trovare l'app.

### Come eseguirlo

Prima l'icona e una prova da Python (nella barra del titolo deve comparire la nuova icona):

```powershell
python make_icon.py
python main.py
```

Poi l'eseguibile (da PowerShell, con l'ambiente attivo, dentro la cartella del progetto):

```powershell
.\build.bat
```

Ci vuole circa **1–3 minuti** e scorrono tante righe `INFO`: è normale. Alla fine trovi:

```text
dist\FocusFlow\FocusFlow.exe
```

Fai **doppio clic** su `FocusFlow.exe`: l'app si apre senza console, con la tua icona, e ritrova i tuoi dati (`C:\Users\TuoNome\FocusFlow`). La cartella `dist\FocusFlow` pesa tra i 50 e i 100 MB: dentro c'è tutto Python.

Compariranno anche le cartelle `build` e `dist` e il file `FocusFlow.spec`: li ha creati PyInstaller, e il `.gitignore` dello Step 13 li esclude da Git.

### Errori comuni

- **`'python' non è riconosciuto` dentro `build.bat`** o `No module named PyInstaller`: l'ambiente virtuale non è attivo o non hai fatto `pip install -r requirements-dev.txt`. Controlla `(.venv)` nel prompt e lancia `build.bat` dallo **stesso terminale**.
- **L'`.exe` si apre e si richiude subito**: c'è un errore che non vedi perché non c'è la console. Costruisci una versione di diagnosi *con* console e avviala dal terminale per leggere l'errore:

  ```powershell
  python -m PyInstaller --noconfirm --name FocusFlowDebug --collect-all customtkinter --add-data "assets;assets" main.py
  .\dist\FocusFlowDebug\FocusFlowDebug.exe
  ```

- **Windows Defender (o l'antivirus) blocca o cancella l'`.exe`**: è un **falso positivo**, frequente con i programmi creati con PyInstaller. Apri *Sicurezza di Windows → Protezione da virus e minacce → Cronologia protezione*, ripristina il file e, se vuoi, aggiungi la cartella `dist` alle esclusioni. Evita `--onefile`, che ne scatena di più.
- **`PermissionError` mentre ricostruisci**: l'app è ancora aperta. Chiudila e rilancia `build.bat`.
- **Hai copiato solo `FocusFlow.exe` su un altro PC e non parte**: l'`.exe` ha bisogno della cartella `_internal` accanto. Copia **tutta** la cartella `dist\FocusFlow`.
- **L'icona non cambia in Esplora file**: Windows tiene le icone in cache. Rinomina la cartella o riavvia Esplora risorse.

### Esercizio

Cambia il colore dell'icona: in `make_icon.py` modifica `ROSSO` in un blu, per esempio `(52, 120, 246, 255)`. Rilancia `python make_icon.py`, poi `build.bat`, e controlla la nuova icona. *(Soluzione in fondo.)*

### Il progetto finora

FocusFlow ha una **icona** e un **eseguibile**. Commit: `git add .`, `git commit -m "Step 19: icona ed eseguibile"`, `git push`.

---

## Step 20 — Distribuire FocusFlow: zip, prova su un altro PC e GitHub Releases

**Obiettivo:** impacchettare l'app in un file zip, provarla su un PC senza Python e pubblicarla su GitHub, con un link da dare a chiunque.

### Concetti in 2 minuti

- Un'app si distribuisce come **file zip** della cartella `dist\FocusFlow`: l'utente lo estrae e avvia `FocusFlow.exe`.
- **GitHub Releases** è la sezione del repository in cui allegare file scaricabili (gratis). Ogni release ha una **versione** (`v1.0.0`) e un **tag** (un'etichetta Git su un commit preciso).
- **Numeri di versione** `maggiore.minore.correzione`: `1.0.0` è la prima versione stabile, `1.0.1` una correzione, `1.1.0` una novità.
- **SmartScreen**: Windows mostra un avviso per le app non firmate. La firma digitale è a pagamento, quindi la tua app ne è priva: è normale e basta cliccare *Ulteriori informazioni → Esegui comunque*.
- **I dati** di ogni utente restano nella sua cartella `C:\Users\Nome\FocusFlow`, separati dall'app: cancellare o sostituire l'app non fa perdere i task.

### Dove lavori

Aggiorna due file: **`.gitignore`** (aggiungi in fondo le ultime tre righe: ignora i file zip) e **`README.md`** (presentazione finale con istruzioni di download).

### Il codice

**`.gitignore`**

```text
# Ambiente virtuale: si ricrea sempre con "pip install", non va su Git
.venv/

# File temporanei di Python
__pycache__/
*.pyc

# Cartelle create da PyInstaller (le useremo alla fine)
build/
dist/
*.spec

# File dell'editor
.vscode/

# File zip da distribuire (si caricano su GitHub Releases, non nel codice)
*.zip
```

**`README.md`**

````markdown
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
````

### Cosa fa questo codice

- `.gitignore`: gli `.zip` da distribuire non finiscono nel codice del repository, ma nelle *Releases*.
- `README.md`: presenta l'app, spiega a un utente come scaricarla e avviarla, dove sono i dati, e a uno sviluppatore come eseguirla dal codice e rifare l'eseguibile.

### Come eseguirlo

**1. Crea lo zip** (nel terminale, nella cartella del progetto, dopo `build.bat`):

```powershell
Compress-Archive -Path dist\FocusFlow -DestinationPath FocusFlow-windows.zip -Force
```

**2. Prova su un altro PC** (o su un altro utente Windows senza Python): copia lo zip con una chiavetta o un servizio cloud, **estrai tutto** (tasto destro → *Estrai tutto…*) e apri `FocusFlow\FocusFlow.exe`. Se compare l'avviso blu *"Windows ha protetto il PC"*: **Ulteriori informazioni → Esegui comunque**. L'app deve partire **senza installare Python**.

**3. Salva il lavoro su GitHub:**

```powershell
git add .
git commit -m "Release 1.0.0: README e .gitignore"
git push
```

**4. Pubblica la release.** Nella pagina del tuo repository su GitHub, nella colonna di destra clicca **Releases → Create a new release**. Poi:

1. In **Choose a tag** scrivi `v1.0.0` e scegli *Create new tag*.
2. Come titolo scrivi `FocusFlow 1.0.0`.
3. Nella descrizione elenca le funzioni (puoi riusare quelle del README).
4. **Trascina `FocusFlow-windows.zip`** nella zona "Attach binaries by dropping them here".
5. Clicca **Publish release**.

Ora chiunque può scaricare l'app dal tuo repository. **Per una nuova versione**: modifichi il codice, rifai `build.bat`, ricrei lo zip e pubblichi una release `v1.0.1` (o `v1.1.0`).

### Errori comuni

- **`Compress-Archive` non trova il percorso**: non hai ancora fatto `build.bat` o sei nella cartella sbagliata. Controlla che esista `dist\FocusFlow`.
- **Su un altro PC l'app non parte, o manca qualcosa**: hai estratto solo l'`.exe`. Serve l'intera cartella `FocusFlow` (con `_internal`).
- **Windows blocca il file scaricato**: tasto destro sullo zip → *Proprietà* → spunta **Sblocca** → OK, *prima* di estrarlo.
- **L'antivirus lo segnala**: vedi lo Step 19 (falso positivo). Dillo a chi scarica l'app.
- **GitHub rifiuta lo zip**: il limite è di 2 GB per file, ampiamente sopra i tuoi 50–100 MB. Controlla di aver allegato lo zip alla *release* e non di averlo trascinato nel repository.
- **Hai committato per sbaglio `build`, `dist` o lo zip**: `git rm -r --cached dist build`, commit e push (il `.gitignore` aggiornato impedisce che ricapiti).

### Esercizio

Fai uno screenshot dell'app (**Win + Maiusc + S**), salvalo come `assets\screenshot.png` e mostralo nel `README.md` con la riga `![FocusFlow](assets/screenshot.png)` subito sotto il titolo. Poi commit e push, e guarda su GitHub come cambia la pagina. *(Soluzione in fondo.)*

### Il progetto finora

**Hai finito!** FocusFlow è un'app gratuita, con interfaccia grafica, salvataggio dati, timer, statistiche, tema scuro, icona, eseguibile, pubblicata su GitHub e distribuibile da un PC all'altro senza installare Python.

Sono 20 step: hai imparato variabili, tipi, input/output, condizioni, cicli, liste, tuple, dizionari, set, funzioni, errori, file, moduli, `pip`, ambienti virtuali, Git/GitHub, classi, interfacce grafiche ed eseguibili. Complimenti!

### Idee per continuare (se ti va)

- **Modifica del titolo** di un task con doppio clic e **data di scadenza**.
- **Notifica** di Windows a fine pomodoro e icona nell'area di notifica.
- **Esportare** i task in un file CSV.
- **Test automatici** con `pytest` (un test per `PomodoroTimer` è semplicissimo, perché non ha grafica).
- Un vero **installer** con *Inno Setup* (gratuito).
- Far costruire l'eseguibile a **GitHub Actions** a ogni nuova versione.


---

## Soluzioni degli esercizi

> Prova SEMPRE a risolvere da solo prima di guardare qui. Se la tua soluzione è diversa ma funziona, va benissimo: in programmazione esistono molte strade giuste.


### Step 1 — Riquadro con il tuo nome

```python
# esercizi/step01.py
print("*" * 30)
print("  Ciao, sono Marco!")
print("  Sto imparando Python!")
print("*" * 30)
```

Cambia `Marco` con il tuo nome. Lancia con `python esercizi\step01.py`.

### Step 2 — Minuti totali di 4 pomodori

```python
# esercizi/step02.py
pomodori = 4
minuti_focus = 25
minuti_pausa = 5

# 4 pomodori e 3 pause (dopo l'ultimo pomodoro non serve la pausa)
minuti_totali = pomodori * minuti_focus + (pomodori - 1) * minuti_pausa
ore = minuti_totali / 60

print(f"Minuti totali: {minuti_totali}")
print(f"Ore: {ore:.2f}")
print(type(minuti_totali), type(ore))
```

Risultato: `Minuti totali: 115`, `Ore: 1.92`, e i tipi `int` e `float`. Il `(pomodori - 1)` conta le pause: ce ne sono sempre una in meno dei pomodori.

### Step 3 — Ore e minuti lavorati

```python
# esercizi/step03.py
pomodori = int(input("Quanti pomodori hai completato oggi? "))
minuti_ciascuno = int(input("Quanti minuti dura ogni pomodoro? "))

totale = pomodori * minuti_ciascuno
ore = totale // 60            # ore intere
minuti = totale % 60          # minuti che avanzano

print(f"Hai lavorato {ore} ore e {minuti} minuti ({totale} minuti in tutto).")
```

Con 5 pomodori da 25 minuti: `Hai lavorato 2 ore e 5 minuti (125 minuti in tutto).`

### Step 4 — Un messaggio per ogni livello

```python
# esercizi/step04.py
pomodori = int(input("Quanti pomodori hai completato oggi? "))

if pomodori == 0:
    print("Inizia con un pomodoro: i primi 25 minuti sono i più difficili!")
elif pomodori <= 3:
    print("Buon inizio, continua così!")
elif pomodori <= 7:
    print("Ottimo lavoro!")
else:
    print("Fenomenale! Ricordati di riposare.")
```

L'ordine delle condizioni conta: Python esegue **il primo** blocco la cui condizione è vera, quindi `elif pomodori <= 3` scatta solo se non era 0.

### Step 5 — Somma delle sessioni

```python
# esercizi/step05.py
sessioni = 0
totale = 0

while True:
    minuti = int(input("Minuti di questa sessione (0 per finire): "))
    if minuti == 0:
        break
    sessioni += 1
    totale += minuti

print(f"Sessioni: {sessioni} - minuti totali: {totale}")
```

Con 25, 30, 0 stampa `Sessioni: 2 - minuti totali: 55`.

### Step 6 — Lista della spesa e tupla dei giorni

```python
# esercizi/step06.py
GIORNI = ("lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica")
print("Il terzo giorno della settimana è", GIORNI[2])

spesa = []
while True:
    prodotto = input("Prodotto (scrivi 'fine' per terminare): ").strip()
    if prodotto == "fine":
        break
    if prodotto != "":
        spesa.append(prodotto)

if spesa:
    ultimo = spesa.pop()                      # toglie l'ultimo inserito
    print(f"Ho tolto l'ultimo prodotto: {ultimo}")
    spesa.sort()                              # ordine alfabetico
    for numero, prodotto in enumerate(spesa, start=1):
        print(f"{numero}. {prodotto}")
    print(f"Totale prodotti: {len(spesa)}")
else:
    print("Lista vuota.")
```

`GIORNI[2]` è il **terzo** elemento perché gli indici partono da 0.

### Step 7 — Dizionario e set

```python
# esercizi/step07.py
pomodori_per_giorno = {"lunedì": 4, "martedì": 6, "mercoledì": 3}
pomodori_per_giorno["giovedì"] = 7           # aggiungo una coppia chiave -> valore

migliore = None
massimo = -1
for giorno, numero in pomodori_per_giorno.items():
    if numero > massimo:
        massimo = numero
        migliore = giorno
print(f"Giorno migliore: {migliore} con {massimo} pomodori")

frase = "studiare python è bello e studiare ogni giorno è meglio"
parole_uniche = set(frase.split())           # split() spezza la frase in parole
print(f"Parole diverse: {len(parole_uniche)} -> {sorted(parole_uniche)}")
```

Risultato: `Giorno migliore: giovedì con 7 pomodori` e 8 parole diverse (le ripetizioni di "studiare" ed "è" contano una volta sola).

### Step 8 — Funzioni con `return`

```python
# esercizi/step08.py
def ore_e_minuti(minuti):
    """Trasforma i minuti in una tupla (ore, minuti)."""
    return minuti // 60, minuti % 60


def messaggio_pomodori(n):
    if n == 0:
        return "Inizia!"
    elif n < 4:
        return "Buon inizio"
    return "Grande!"


ore, minuti = ore_e_minuti(135)
print(f"135 minuti = {ore} ore e {minuti} minuti")
print(messaggio_pomodori(0), "|", messaggio_pomodori(2), "|", messaggio_pomodori(9))
```

`return minuti // 60, minuti % 60` restituisce una **tupla**, e `ore, minuti = ore_e_minuti(135)` la "spacchetta".

### Step 9 — Divisione sicura

```python
# esercizi/step09.py
while True:
    try:
        divisore = int(input("Dividi 100 per: "))
        risultato = 100 / divisore
    except ValueError:
        print("Scrivi un numero intero, per favore.")
    except ZeroDivisionError:
        print("Non si può dividere per zero!")
    else:                                   # "else" parte solo se NON ci sono stati errori
        print(f"100 / {divisore} = {risultato:.2f}")
        break
```

Il ciclo `while True` ripete la domanda finché non ci sono errori; solo allora `else` stampa il risultato e il `break` esce.

### Step 10 — Diario

```python
# esercizi/step10.py
from datetime import date
from pathlib import Path

file_diario = Path("diario.txt")

frase = input("Scrivi una frase per il diario di oggi: ")
with open(file_diario, "a", encoding="utf-8") as f:      # "a" = append: aggiunge in fondo
    f.write(f"{date.today().isoformat()} - {frase}\n")

print("\n--- Il tuo diario ---")
with open(file_diario, "r", encoding="utf-8") as f:
    for riga in f:
        print(riga.rstrip())                              # rstrip toglie l'"a capo" in più
```

Il modo `"a"` **aggiunge** in fondo senza cancellare il contenuto. Il file `diario.txt` nasce nella cartella da cui lanci il comando.

### Step 11 — Il tuo modulo `utils`

**`esercizi\utils.py`**

```python
# esercizi/utils.py
def formatta_durata(minuti):
    """Per esempio 135 -> '2h 15min'."""
    ore, resto = divmod(minuti, 60)
    if ore == 0:
        return f"{resto}min"
    return f"{ore}h {resto:02d}min"
```

**`esercizi\step11_prova.py`**

```python
# esercizi/step11_prova.py
import random

from utils import formatta_durata

FRASI = ("Un passo alla volta.", "Inizia adesso.", "Ce la puoi fare!", "Poco ma ogni giorno.")

print(formatta_durata(135))
print(formatta_durata(45))
print(random.choice(FRASI))
```

Si lancia con `python esercizi\step11_prova.py` (da dentro la cartella `esercizi` se Python non trova `utils`: `cd esercizi`, poi `python step11_prova.py`).

### Step 12 — Prova con `rich`

```python
# esercizi/step12_rich.py  (serve:  pip install rich)
from rich import print
from rich.table import Table

print("[bold red]FocusFlow[/bold red] funziona anche con [green]i colori[/green]!")

tabella = Table(title="I miei pomodori")
tabella.add_column("Giorno")
tabella.add_column("Pomodori", justify="right")
tabella.add_row("Lunedì", "4")
tabella.add_row("Martedì", "6")
print(tabella)
```

Se hai l'ambiente attivo e `pip install rich`, vedrai una frase colorata e una tabella nel terminale. Ricorda: è solo una prova, non va in `requirements.txt`.

### Step 13 — Commit del README

Aggiungi in fondo a `README.md`:

```markdown
## Diario di bordo

- Ho imparato a usare Git e a pubblicare il progetto su GitHub.
```

Poi nel terminale:

```powershell
git add .
git commit -m "Aggiorno il README"
git push
git log --oneline
```

Il `git log --oneline` mostra ora due (o più) righe: ogni commit è un punto di ripristino.

### Step 14 — La classe `Abitudine`

```python
# esercizi/step14.py
class Abitudine:
    def __init__(self, nome):
        self.nome = nome
        self.giorni_di_fila = 0

    def segna_oggi(self):
        self.giorni_di_fila += 1

    def azzera(self):
        self.giorni_di_fila = 0

    def __str__(self):
        return f"{self.nome}: {self.giorni_di_fila} giorni di fila"


lettura = Abitudine("Leggere 10 pagine")
lettura.segna_oggi()
lettura.segna_oggi()
print(lettura)
corsa = Abitudine("Correre")
corsa.segna_oggi()
print(corsa)
lettura.azzera()
print(lettura)
```

Output: `Leggere 10 pagine: 2 giorni di fila`, `Correre: 1 giorni di fila`, `Leggere 10 pagine: 0 giorni di fila`. Ogni oggetto ha i **suoi** attributi: azzerare `lettura` non tocca `corsa`.

### Step 15 — Il bottone "Azzera"

```python
# esercizi/prova_gui2.py
import customtkinter as ctk

contatore = 0


def al_click():
    global contatore
    contatore += 1
    etichetta.configure(text=f"Hai cliccato {contatore} volte")


def azzera():
    global contatore
    contatore = 0
    etichetta.configure(text="Contatore azzerato")


finestra = ctk.CTk()
finestra.title("Prova GUI 2")
finestra.geometry("320x220")

etichetta = ctk.CTkLabel(finestra, text="Non hai ancora cliccato", font=("Roboto", 16))
etichetta.pack(pady=(30, 10))
ctk.CTkButton(finestra, text="Cliccami!", command=al_click).pack(pady=5)
ctk.CTkButton(finestra, text="Azzera", fg_color="gray40", command=azzera).pack(pady=5)

finestra.mainloop()
```

La funzione `azzera` usa `global contatore` per modificare la variabile creata fuori; il bottone la riceve con `command=azzera` (senza parentesi).

### Step 16 — "Segna tutte"

**1. In `tasks.py`**, dentro la classe `TaskManager` (per esempio sopra `pulisci_completati`):

```python
    def segna_tutti_fatti(self):
        for task in self.tasks:
            task.fatto = True
        self.salva()
```

**2. In `ui_tasks.py`**, nel costruttore, **prima** del `self.pulisci_button = ...` aggiungi il nuovo bottone, e sposta "Pulisci completate" nella colonna 2:

```python
        self.tutti_button = ctk.CTkButton(
            piede, text="Segna tutte", width=110, height=30,
            fg_color="transparent", border_width=1, border_color=style.MUTED,
            text_color=style.MUTED, hover_color=style.ROW,
            command=self.on_tutti,
        )
        self.tutti_button.grid(row=0, column=1, padx=(0, 8), sticky="e")
```

e cambia la riga che posiziona il vecchio bottone in:

```python
        self.pulisci_button.grid(row=0, column=2, sticky="e")
```

**3. Sempre in `ui_tasks.py`**, accanto agli altri eventi:

```python
    def on_tutti(self):
        self.manager.segna_tutti_fatti()
        self.aggiorna_tutto()
```

### Step 17 — Il tempo nel titolo della finestra

Alla **fine** del metodo `aggiorna()` in `ui_timer.py`, dopo l'ultima riga esistente, aggiungi:

```python
        titolo = "FocusFlow"
        if self.timer.in_corso:
            titolo = f"{self.timer.testo_tempo()} · FocusFlow"
        self.winfo_toplevel().title(titolo)       # winfo_toplevel() = la finestra principale
```

Mentre il timer corre, il titolo diventa per esempio `24:59 · FocusFlow`; in pausa torna `FocusFlow`.

### Step 18 — Media dei pomodori

**In `stats.py`**, in fondo:

```python
def media_ultimi_giorni(quanti=7):
    """Media di pomodori al giorno negli ultimi giorni."""
    giorni = ultimi_giorni(quanti)
    totale = sum(numero for _, numero in giorni)
    return totale / quanti
```

**In `ui_stats.py`**, nel metodo `aggiorna()`, sostituisci l'istruzione `self.dettagli.configure(...)` con:

```python
        self.dettagli.configure(
            text=f"Totale pomodori: {stats.pomodori_totali()}\n"
                 f"Media ultimi 7 giorni: {stats.media_ultimi_giorni():.1f} al giorno\n"
                 f"Task completati: {self.manager.quanti_fatti()} su {len(self.manager.tasks)}"
        )
```

### Step 19 — Un'icona blu

In `make_icon.py` cambia la prima costante:

```python
ROSSO = (52, 120, 246, 255)
```

(il nome della variabile può restare `ROSSO`, ma volendo rinominala ovunque in `COLORE`). Poi `python make_icon.py` e `.\build.bat`.

### Step 20 — Lo screenshot nel README

Salva l'immagine come `assets\screenshot.png` e subito sotto il titolo di `README.md` aggiungi:

```markdown
![FocusFlow](assets/screenshot.png)
```

Poi `git add .`, `git commit -m "Aggiungo lo screenshot"`, `git push`. GitHub mostrerà l'immagine nella pagina del progetto.


---

## Se mi blocco

### Il metodo in 6 passi (funziona sempre)

1. **Non farti prendere dal panico: è normale.** Un programmatore passa molto tempo con messaggi d'errore sullo schermo.
2. **Leggi l'ultima riga del messaggio** (il traceback si legge dal basso): dice il *tipo* di errore e il motivo. Sopra c'è il **file** e il **numero di riga**.
3. **Vai a quella riga** (in VS Code: Ctrl+G, scrivi il numero). Guarda anche la riga *prima*: spesso l'errore vero è lì (una parentesi, una virgoletta o i due punti dimenticati).
4. **Confronta il tuo codice con quello della guida**: indentazione (4 spazi), maiuscole/minuscole, virgolette, trattini bassi, `:` a fine riga.
5. **Fai parlare il programma**: aggiungi un `print(variabile)` prima della riga sospetta e guarda cosa contiene davvero. Per un controllo più preciso, usa il **debugger di VS Code**: clicca a sinistra del numero di riga (compare un pallino rosso = *breakpoint*), premi **F5** e usa **F10** per avanzare una riga alla volta, guardando i valori delle variabili.
6. **Cerca l'ultima riga dell'errore su internet** (meglio in inglese, tra virgolette): quasi certamente qualcuno ha già avuto lo stesso problema.

### Gli errori più comuni

| Messaggio | Cosa significa | Cosa fare |
| --- | --- | --- |
| `'python' non è riconosciuto…` | Python non è nel PATH | Reinstalla spuntando "Add python.exe to PATH", riapri VS Code (Step 1) |
| `SyntaxError` | Frase scritta male | Controlla la riga indicata e quella prima: virgolette, parentesi, `:` |
| `IndentationError` | Spazi sbagliati | Blocchi indentati di 4 spazi; non mischiare Tab e spazi |
| `NameError: name 'x' is not defined` | Variabile/funzione mai creata o nome diverso | Controlla l'ortografia; definiscila *prima* di usarla |
| `TypeError` | Tipi che non vanno d'accordo (testo + numero…) | Usa f-string o `int(...)`/`str(...)` |
| `ValueError: invalid literal for int()` | Hai convertito in numero un testo che non lo è | Controlla cosa scrive l'utente; usa `try / except` (Step 9) |
| `IndexError: list index out of range` | Posizione che non esiste in una lista | Ricorda: si parte da 0; controlla `len(lista)` |
| `KeyError: 'chiave'` | Chiave non presente nel dizionario | Controlla il nome; usa `.get("chiave", valore)` |
| `AttributeError: 'X' object has no attribute 'y'` | Nome dell'attributo/metodo sbagliato, o `self.` dimenticato | Controlla l'ortografia e `self.` (Step 14) |
| `ModuleNotFoundError: No module named 'x'` | Modulo non trovato | Tuo file? Stessa cartella di `main.py`. Libreria? `pip install` con `(.venv)` attivo |
| `FileNotFoundError` | Il percorso non esiste | Controlla nome e cartella; usa `Path.home() / ...` |
| `json.decoder.JSONDecodeError` | File JSON rovinato | Cancella il file (verrà ricreato) |
| `_tkinter.TclError` | Problema con la finestra/widget | Widget distrutto, `pack` e `grid` mischiati, o percorso icona sbagliato |
| `Activate.ps1 non può essere caricato` | PowerShell blocca gli script | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| `! [rejected] … fetch first` (Git) | Il repository remoto ha già dei file | Ricrea il repo vuoto, o `git pull origin main --allow-unrelated-histories` |

### Problemi di ambiente: lista di controllo

- Nel prompt c'è `(.venv)`? Se no: `.venv\Scripts\Activate.ps1`.
- `python --version` dice 3.13? E `python check_env.py` dice "SÌ" e mostra la versione di customtkinter?
- VS Code usa l'interprete giusto? **Ctrl+Shift+P → Python: Seleziona interprete → `.venv`**.
- Hai salvato **tutti** i file (File → Salva tutto)?
- Sei nella **cartella del progetto** (`dir` mostra `main.py`)?
- **Ricominciare l'ambiente da capo** non è grave: cancella la cartella `.venv`, poi `python -m venv .venv`, attivalo e `pip install -r requirements.txt`.

### Tornare a uno stato funzionante con Git

- `git status` → cosa è cambiato rispetto all'ultimo commit.
- `git diff` → *cosa* è cambiato, riga per riga.
- `git restore nome_file.py` → riporta quel file all'ultimo commit (le modifiche non salvate in Git vanno perse).
- `git log --oneline` → l'elenco dei tuoi salvataggi.

Per questo ti ho chiesto di fare un commit a ogni step: puoi sempre tornare all'ultimo punto in cui funzionava.

### Dove sono i miei dati? Come ripartire da zero?

I dati di FocusFlow sono in `C:\Users\TuoNome\FocusFlow` (`tasks.json`, `settings.json`, `stats.json`). Per azzerare tutto, chiudi l'app e **cancella quella cartella**. Per azzerare solo le impostazioni, cancella `settings.json`.

### Come chiedere aiuto (a un forum, a un amico, a un assistente AI)

Una buona richiesta contiene sempre:

1. **Cosa volevi ottenere** e **cosa succede invece**.
2. **Il messaggio d'errore completo** (copia e incolla, non una foto sfocata).
3. **Il codice** del file coinvolto (o la parte rilevante) e **quale step** della guida stai seguendo.
4. **Versioni**: `python --version`, Windows 10 o 11, e se l'ambiente virtuale è attivo.
5. **Cosa hai già provato.**

Con questa guida puoi anche incollare il tuo codice accanto a quello dello step e chiedere "cosa cambia?": spesso la differenza è un solo carattere.

### Risorse ufficiali e gratuite

- Tutorial e documentazione di Python (anche in italiano): <https://docs.python.org/it/3/>
- CustomTkinter: <https://customtkinter.tomschimansky.com>
- Git (libro ufficiale, in italiano): <https://git-scm.com/book/it/v2>
- PyInstaller: <https://pyinstaller.org>
- GitHub Docs: <https://docs.github.com>


---

## Checklist finale: cosa hai imparato

Spunta le voci man mano. Se una non ti torna, il numero tra parentesi è lo step da ripassare.

### Strumenti e ambiente
- [ ] Ho installato Python (con PATH) e VS Code con l'estensione Python (1)
- [ ] So aprire il terminale di VS Code ed eseguire `python file.py` (1)
- [ ] So creare e attivare un **ambiente virtuale** e riconoscerlo dal `(.venv)` (12)
- [ ] So installare librerie con `pip` e usare `requirements.txt` (12)
- [ ] So usare **Git**: `init`, `add`, `commit`, `push`, `status`, `log` (13)
- [ ] Ho un account GitHub e un repository con il mio progetto (13)

### Basi di Python
- [ ] Variabili e tipi: `str`, `int`, `float`, `bool`, e le f-string (2)
- [ ] `input()` e `print()`, e la conversione con `int()` (3)
- [ ] Operatori `+ - * / // %` e confronti `== != < > <= >=` (3–4)
- [ ] `if / elif / else` e `and / or / not` (4)
- [ ] Cicli `while`, `for`, `range`, `break` (5)
- [ ] **Liste** (`append`, `pop`, indici, `len`) e **tuple** (6)
- [ ] **Dizionari** (chiave → valore, `.get`) e **set** (7)
- [ ] **Funzioni**: `def`, parametri, `return`, valori predefiniti (8)
- [ ] **Errori**: leggere un traceback, `try / except / finally` (9)
- [ ] **File**: `open`, `with`, **JSON**, `pathlib.Path` (10)
- [ ] **Moduli**: `import`, `from … import`, dividere il codice in più file (11)
- [ ] **Classi e oggetti**: `class`, `__init__`, `self`, metodi, `__str__` (14)

### Interfaccia grafica
- [ ] Widget, `mainloop()` e programmazione a eventi (15)
- [ ] Callback con `command=` e lambda con argomento (15–16)
- [ ] Layout con `grid` e `pack` (15)
- [ ] Ridisegnare una lista con `refresh()` (15–16)
- [ ] Separare logica e grafica (`pomodoro.py` vs `ui_timer.py`) (17)
- [ ] Far scorrere il tempo con `after()` senza bloccare la finestra (17)
- [ ] Schede, cursori, tema chiaro/scuro e impostazioni salvate (18)

### Distribuzione
- [ ] Ho creato l'icona con Pillow (19)
- [ ] Ho creato l'eseguibile con PyInstaller (19)
- [ ] Ho provato l'app su un PC **senza Python** (20)
- [ ] Ho pubblicato una **release** su GitHub con lo zip (20)

### Il progetto
- [ ] FocusFlow gestisce task con categorie, filtri, spunte ed eliminazione
- [ ] FocusFlow ha un timer Pomodoro collegato ai task
- [ ] FocusFlow mostra statistiche degli ultimi 7 giorni
- [ ] FocusFlow salva dati e impostazioni tra un avvio e l'altro
- [ ] FocusFlow è un `.exe` che posso passare a chiunque

---

**Bravo/a.** Sei partito da `print("Ciao")` e hai costruito un'app vera. La cosa più importante che hai imparato non è una libreria, ma il metodo: scrivere un pezzetto, provarlo, leggere gli errori, sistemare, salvare con un commit. Con questo metodo puoi costruire qualunque cosa.

<!-- Fine della guida -->
