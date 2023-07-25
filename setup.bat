@echo off

REM Step 1: Install virtualenv via pip
pip install virtualenv

REM Step 2: Create a virtual environment named "env"
python -m virtualenv env

REM Step 3: Activate the virtual environment
env\Scripts\activate.bat

REM Step 4: Install packages from requirements.txt
pip install -r requirements.txt

REM Step 5: Run the Python scripts
python -m pyinstaller --onefile --distpath . --icon assets\atreus.png install.py
python -m pyinstaller --onefile --distpath . --icon assets\atreus.png  trace_registry.py
python -m pyinstaller --onefile --distpath . --icon assets\atreus.png  watchdog.py
python -m pyinstaller --onefile --distpath . --icon assets\atreus.png  trace_suspect_files.py
python -m pyinstaller --onefile --distpath . --icon assets\atreus.png  complex_interface.py

REM Step 6: Delete the build folder
rmdir /s /q build

REM Step 7: Deactivate the virtual environment (optional, if you want to exit the virtual environment after running the scripts)
deactivate
