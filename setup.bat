@echo off
title MultiTool - Setup
echo ============================================
echo   MultiTool - Installazione dipendenze
echo ============================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRORE] Python non trovato nel PATH.
    echo Installa Python da https://www.python.org/downloads/
    echo e assicurati di spuntare "Add Python to PATH" durante l'installazione.
    echo.
    pause
    exit /b 1
)

echo [*] Installazione librerie: rich, pyfiglet ...
pip install rich pyfiglet

echo.
echo [+] Installazione completata!
echo Ora puoi avviare il tool con "tool.bat"
echo.
pause
