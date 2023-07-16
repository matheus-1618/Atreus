import urllib.request
import zipfile
import os
import subprocess


def get_sysmon():
    def install_sysmon(sysmon_path):
        try:
            subprocess.run([sysmon_path, "-accepteula", "-i"], check=True)
            print("Sysmon installation completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Sysmon installation failed: {e}")

    # Download and extract Sysmon utility
    url = 'https://download.sysinternals.com/files/Sysmon.zip'
    file_name = 'Sysmon.zip'
    extract_folder = 'Sysmon'
    try:
        urllib.request.urlretrieve(url, file_name)
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
        os.remove(file_name)
    except Exception as e:
        print(f"Error downloading and extracting Sysmon utility: {e}")
        exit()

    # Path to the Sysmon installer executable
    sysmon_path = os.path.join(extract_folder, 'Sysmon64.exe')

    # Call the function to install Sysmon
    install_sysmon(sysmon_path)

def get_pstools():
    # Download and extract PSTools utility
    if not os.path.exists('PSTools'):
        url = 'https://download.sysinternals.com/files/PSTools.zip'
        file_name = 'PSTools.zip'
        extract_folder = 'PSTools'

        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            os.remove(file_name)
            return True
        except Exception as e:
            print(f"Error downloading and extracting PSTools utility: {e}")
            return False
    return True

def get_sigcheck():
    if not os.path.exists('Sigcheck'):
        # Download and extract Sigcheck utility
        url = 'https://download.sysinternals.com/files/Sigcheck.zip'
        file_name = 'Sigcheck.zip'
        extract_folder = 'Sigcheck'
        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            os.remove(file_name)
            return True
        except Exception as e:
            print(f"Error downloading and extracting Sigcheck utility: {e}")
            return False
    return True

def get_procdump():
    if not os.path.exists('procdump.exe'):
        # Download and extract Procdump
        url = 'https://download.sysinternals.com/files/Procdump.zip'
        file_name = 'Procdump.zip'

        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall()
            os.remove(file_name)
            return True
        except Exception as e:
            print(f"Error downloading and extracting Procdump: {e}")
            return False
    return True

def get_handle():
    # Download and extract Handle utility
    if not os.path.exists('Handle.exe'):
        url = 'https://download.sysinternals.com/files/Handle.zip'
        file_name = 'Handle.zip'

        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall()
            os.remove(file_name)
            return True
        except Exception as e:
            print(f"Error downloading and extracting Handle utility: {e}")
            return False
    return True      

def get_listdlls():
    # Download and extract ListDlls utility
    if not os.path.exists('ListDlls.exe'):
        url = 'https://download.sysinternals.com/files/ListDlls.zip'
        file_name = 'ListDlls.zip'

        try:
            urllib.request.urlretrieve(url, file_name)
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall()
            os.remove(file_name)
            return True
        except Exception as e:
            print(f"Error downloading and extracting ListDlls utility: {e}")
            return False
    return True