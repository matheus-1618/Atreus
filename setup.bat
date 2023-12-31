@echo off
echo Installing Atreus dependencies and running it

REM Step 1: Install virtualenv via pip
pip install virtualenv
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the installation of virtualenv.
    exit /b 1
)

REM Step 2: Create a virtual environment named "env"
python -m virtualenv env
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the creation of the virtual environment.
    exit /b 1
)

REM Step 3: Activate the virtual environment
call env\Scripts\activate
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while activating the virtual environment.
    exit /b 1
)

REM Step 4: Install packages from requirements.txt
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the installation of packages from requirements.txt.
    exit /b 1
)

REM Step 5: Run PyInstaller for specific .py files
pyinstaller  --onefile --distpath . --icon assets\atreus.png src\install.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for install.py.
    exit /b 1
)

pyinstaller  --onefile --distpath . --icon assets\atreus.png src\trace_registry.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for trace_registry.py.
    exit /b 1
)

pyinstaller  --onefile --distpath . --icon assets\atreus.png src\watchdog.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for watchdog.py.
    exit /b 1
)

pyinstaller  --onefile --distpath . --icon assets\atreus.png src\trace_executables.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for trace_executables.py.
    exit /b 1
)

pyinstaller --noconsole --onefile --distpath . --icon assets\atreus.png src\atreus.py
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred during the PyInstaller build for atreus.py.
    exit /b 1
)

REM Step 6: Delete the build folder
rmdir /s /q build
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while deleting the build folder.
    exit /b 1
)

REM Step 7: Delete all .spec files in the current directory
for %%i in (*.spec) do (
    del "%%i"
)

REM Step 8: Delete the env folder
rmdir /s /q env
IF %ERRORLEVEL% NEQ 0 (
    echo An error occurred while deleting the build folder.
    exit /b 1
)

REM Step 9: Execute all the executables
powershell -Command "Start-Process -FilePath \"install.exe\" -Verb RunAs -Wait"
powershell -Command "Start-Process -FilePath \"watchdog.exe\" -Verb RunAs"
powershell -Command "Start-Process -FilePath \"trace_registry.exe\" -Verb RunAs"
powershell -Command "Start-Process -FilePath \"trace_executables.exe\" -Verb RunAs"
powershell -Command "Start-Process -FilePath \"atreus.exe\" -Verb RunAs"

