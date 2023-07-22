import winreg

def check_registry():
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    value_name = "svchos"
    return_value = True
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path)
        value, value_type = winreg.QueryValueEx(registry_key, value_name)
        print(f"The value '{value_name}' exists in the registry key '{key_path}'.")
    except FileNotFoundError:
        print(f"The registry key '{key_path}' does not exist.")
        return_value = False
    except winreg.WindowsError:
        print(f"The value '{value_name}' does not exist in the registry key '{key_path}'.")
        return_value = False
    finally:
        return return_value
