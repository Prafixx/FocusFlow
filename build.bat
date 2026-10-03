@echo off
REM build.bat - crea l'eseguibile di FocusFlow (da lanciare con l'ambiente virtuale attivo)

echo === 1/3 Creo l'icona ===
python make_icon.py

echo === 2/3 Creo l'eseguibile con PyInstaller ===
python -m PyInstaller --noconfirm --clean --windowed --name FocusFlow --icon assets\icon.ico --collect-all customtkinter --add-data "assets;assets" main.py

echo === 3/3 Fatto! ===
echo Trovi l'app in:  dist\FocusFlow\FocusFlow.exe
pause
