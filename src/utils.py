import ctypes
import psutil
import os
import json

def read_json_file(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            if not data:  # Check if the data is empty or None
                print(f"JSON file '{filename}' is empty.")
                return False
            return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{filename}'.")
        return False

def clear_json_file(filename):
    try:
        with open(filename, "w") as file:
            json.dump({}, file)
        return True
    except Exception as e:
        print(f"Error clearing JSON file '{filename}': {e}")
        return False
    
def hide_console_window():
    console_window = ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(console_window, 0)

def high_privileges():
    process = psutil.Process(os.getpid())
    process.nice(psutil.HIGH_PRIORITY_CLASS)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False
    
def write_to_file(filename, content):
    try:
        # Open the file in append mode
        with open(filename, "a") as file:
            file.write(content)
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the content
        with open(filename, "w") as file:
            file.write(content)
            
def list_to_string_with_newlines(input_list):
    return '\n'.join(str(item) for item in input_list)

def string_with_newlines_to_list(input_string):
    return input_string.split('\n')

def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False

    for item1 in list1:
        if item1 not in list2:
            return False

    return True 