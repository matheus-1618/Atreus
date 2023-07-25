@echo off

REM Step 1: Install virtualenv via pip
pip install virtualenv
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the installation of virtualenv.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 2: Create a virtual environment named "env"
python -m virtualenv env
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the creation of the virtual environment.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 3: Activate the virtual environment
call env\Scripts\activate
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while activating the virtual environment.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 4: Install packages from requirements.txt
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the installation of packages from requirements.txt.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 5: Run PyInstaller for specific .py files
pyinstaller --onefile --distpath . --icon assets\atreus.png src\install.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for install.py.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

pyinstaller --onefile --distpath . --icon assets\atreus.png src\trace_registry.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for trace_registry.py.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

pyinstaller --onefile --distpath . --icon assets\atreus.png src\watchdog.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for watchdog.py.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

pyinstaller --onefile --distpath . --icon assets\atreus.png src\trace_suspect_files.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for trace_suspect_files.py.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

pyinstaller --onefile --distpath . --icon assets\atreus.png src\complex_interface.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for complex_interface.py.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 6: Delete the build folder
rmdir /s /q build
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while deleting the build folder.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

REM Step 7: Deactivate the virtual environment (optional, if you want to exit the virtual environment after running the scripts)
deactivate
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while deactivating the virtual environment.
    REM You can add further actions or error handling here if needed.
    exit /b 1
)

