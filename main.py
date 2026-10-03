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
