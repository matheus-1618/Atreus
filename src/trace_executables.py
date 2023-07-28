import tkinter as tk
from PIL import Image, ImageTk
import ctypes
import os
from controller import Controller
import schedule
import time
import concurrent.futures
import sys
from utils import is_admin, hide_console_window, high_privileges,list_to_string_with_newlines,string_with_newlines_to_list,read_json_file,clear_json_file

controller = Controller()

def remove(files):
    files = string_with_newlines_to_list(files)
    for file_path in files:
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been successfully removed.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except PermissionError:
            print(f"Access denied. You may need administrator privileges to delete the file.")
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
    clear_json_file("suspected_files.json")

def scan_files():
    controller.scan_files()

def scan_files_sigcheck():
    controller.scan_files_with_sigcheck()

def show_popup(files,type):
    # Create the main Tkinter window
    root = tk.Tk()
    root.title(f"Atreus--{type} detection")

    # Set the window size and position it in the center of the screen
    window_width = 400
    window_height = 290 + len(string_with_newlines_to_list(files))*15
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set the icon for the window
    icon_path = "assets\\atreus.ico"
    root.iconbitmap(icon_path)

    # Load the image and resize it to fit the window
    image_path = "assets\\atreus.png"
    image = Image.open(image_path)
    image = image.resize((100, 100))
    image = ImageTk.PhotoImage(image)

    # Function to close the popup window and call the ignore function
    def on_ignore():
        root.destroy()
        controller.kill_process(os.getpid())

    # Function to close the popup window and call the remove function
    def on_remove():
        remove(files)
        root.destroy()

    # Create a frame to hold the label and image
    frame = tk.Frame(root)
    frame.pack(pady=20)

    # Display the image in the center of the frame
    image_label = tk.Label(frame, image=image)
    image_label.pack()

    # Create the label with the message and set the font
    label = tk.Label(frame, text=f"Atreus discovered suspect files:\n\n{files}\n\nWhat you want to do?", font=("Arial", 12))
    label.pack(pady=10)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(frame)
    button_frame.pack()

    # Create the "Remove" button
    remove_button = tk.Button(button_frame, text="Remove", font=("Arial", 12), command=on_remove)
    remove_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Create the "Ignore" button
    ignore_button = tk.Button(button_frame, text="Ignore", font=("Arial", 12), command=on_ignore)
    ignore_button.pack(side=tk.LEFT, padx=10, pady=5)

    # Run the Tkinter main loop
    root.mainloop()

def yara_scan():
    scan_files()
    schedule.every(1).minutes.do(scan_files)
    # Run the job continuously
    while True:
        schedule.run_pending()
        time.sleep(1)

def sigcheck_scan():
    scan_files_sigcheck()
    schedule.every(3).minutes.do(scan_files_sigcheck)
    # Run the job continuously
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    if not is_admin():
        print("This script requires administrator privileges to run.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    hide_console_window()
    high_privileges()

    # Create a ThreadPoolExecutor with max_workers=1
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Schedule the job to run every 1 minutes using submit method of ThreadPoolExecutor
        executor.submit(yara_scan)
        executor.submit(sigcheck_scan)

        while True:
            sigcheck_files = read_json_file("sigcheck_detected_files.json")
            yara_detected_files = read_json_file("yara_detected_files.json")
            if sigcheck_files:
                show_popup(list_to_string_with_newlines(list(sigcheck_files.keys())), "Sigcheck")
            elif yara_detected_files:
                show_popup(list_to_string_with_newlines(list(yara_detected_files.keys())), "Yara")
            time.sleep(1)
