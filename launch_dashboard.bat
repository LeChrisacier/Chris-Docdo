@echo off
echo [*] Vérification de l'environnement Python...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Veuillez installer Python 3.
    pause
    exit /b
)

echo [*] Installation des dépendances...
pip install -r requirements.txt

echo [*] Lancement de l'application Flask...
python app.py

pause
