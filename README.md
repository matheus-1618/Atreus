# Atreus
<div align="center" >
<img src='assets/atreus.png' style="width:25rem;"/>

Anti-Ransomware Ryuk software.

Disclaimer: Not intended to be a production Counter Measure, only a good approach to identify and mitigate Ryuk actions.
</div>

## Build
:warning: Python required
To Build Atreus, follow the steps above:

```bash
python -m venv env
venv_name\Scripts\activate
pip install -r requirements.txt
python install.py
pyinstaller --onefile watchdog.py
pyinstaller --onefile trace_registry.py
pyinstaller --onefile trace_suspect_files.py
```
Enter in the **dist/** folder, and copy the executables files on the Atreus root folder. Execute them.

## About
Ryuk is a Ransomware from Hermes family, and has some typical behaviours analysed in this [research](www.google.com), such as:
* Multi-thread, calling CreateRemoteThread
* Process Injection through multiples process in the Machine
* AES256 encryption of files
* Envelope encryptation of each AES key inside the file with RSA1 key.
* Change of the registry keys using "sycho" for persistence
* Dropping it's executable in the "C:/Users/<user_name>/Public" folder

## How Atreus work
Atreus creates multiple honeypots files invisible to the user, with the intent of Ryuk open it and encryptates. Once Ryuk open one of these files, Atreus stops the process responsible for it and dump it's information. Also, it monitorates other informations, such as:
* Registry Keys
* DLL's imported for process
* CreateRemoteThread calls over the process
* Process with handles to files

