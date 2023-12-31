import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image
import os
import sys
from config.monitor_registry import check_registry
from prettytable import PrettyTable
from controller import *
import threading
import ctypes
from functools import partial
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.first_update()
        self.controller = Controller()
        
        # configure window
        self.title("Atreus")
        self.geometry(f"{700}x{680}")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # Get the base path of the executable or script
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Join the base path with the "assets" folder name
        image_path = os.path.join(base_path, "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "atreus.png")), size=(250, 150))
        self.after(200, lambda: self.iconbitmap(os.path.join(image_path, "atreus.ico")))
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="",image=self.logo_image,compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Activate Watchdog", command=self.watchdog_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Run Static Scan", command=self.static_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.registry_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, 
                                                     text_color=("gray10", "#DCE4EE"))
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.tabview.add("Logs")
        self.tabview.add("Dumps")
        self.tabview.add("Files")
        self.tabview.tab("Logs").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Dumps").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Files").grid_columnconfigure(0, weight=1)

        #Logs files
        self.look_for_logs()
        
        #Dumps files
        self.look_for_dumps()

        #Suspected files
        self.look_for_files()
        
        #Progress Bar
        self.progressbar_1 = customtkinter.CTkProgressBar(self)
        self.progressbar_1.grid(row=1, column=1, padx=(20, 10), pady=(20, 10), sticky="ew")
      

        ryuk_ransomware_description = """Ryuk ransomware is a sophisticated and notorious strain of ransomware that emerged in August 2018. It is known for its highly targeted attacks on large organizations, especially in the corporate and government sectors. Ryuk is believed to be operated by a cybercrime group known as Wizard Spider.

The primary purpose of Ryuk ransomware is to encrypt the victim's files, making them inaccessible. Once the files are encrypted, Ryuk displays a ransom note, typically in a "RyukReadMe.txt" file, containing instructions on how to pay the ransom to obtain the decryption key.

Key characteristics of Ryuk ransomware include:

1. Targeted Attacks: Ryuk targets specific organizations and infects their systems after gaining unauthorized access. These attacks often follow an initial infection by other malware, such as TrickBot or Emotet, which are used to gain a foothold in the network.

2. High Ransom Demands: Ryuk's ransom demands are usually significantly higher than those of other ransomware strains. This is because the attackers tailor the ransom amount based on the victim's perceived ability to pay, often demanding millions of dollars.

3. Manual Execution: Ryuk is often manually deployed by the attackers, enabling them to assess the network's value and select the most critical systems to target.

4. Custom Encryption: Ryuk employs a sophisticated encryption algorithm to lock files, making it challenging to decrypt them without the unique decryption key held by the attackers.

5. Evolving Tactics: The Ryuk ransomware is continually evolving, with the attackers refining their techniques to evade detection and increase their success rate.

It's important to note that paying the ransom does not guarantee that the attackers will provide the decryption key or that the files will be recovered. Moreover, it encourages and funds further criminal activities. To defend against ransomware attacks like Ryuk, organizations should focus on proactive cybersecurity measures, such as regular data backups, robust security protocols, and employee training to prevent phishing and social engineering attacks."""

        atreus_description = """
Atreus Anti-Ransomware: Your Defense Against Ryuk Ransomware

Atreus is a open-source anti-ransomware software specifically designed to protect against the notorious Ryuk ransomware. Ryuk is a highly targeted and dangerous strain of ransomware known for its devastating attacks on large organizations. Developed as a result of extensive undergraduate research at my university, Atreus aims to provide an additional layer of defense against Ryuk and its malicious activities.

Key Features of Atreus Anti-Ransomware:

1. Detecting Suspicious "CreateRemoteThread" Calls:

Atreus keeps a vigilant eye on system processes, especially monitoring for suspicious "CreateRemoteThread" calls. These calls are commonly associated with Ryuk's attempt to inject its malicious code into other processes, enabling the ransomware to spread and cause widespread damage. By identifying and alerting about such behavior, Atreus helps you detect and respond to potential Ryuk attacks early on.

2. Detecting Registry Changes for Persistence:

Ryuk relies on modifying registry settings to maintain persistence on infected systems, ensuring that it remains active even after system reboots. Atreus is equipped with advanced monitoring capabilities that can detect and flag any unauthorized changes to critical registry entries, allowing you to identify potential ransomware activity and take immediate action.

3. Detecting Suspected Files with YARA Rules:

Utilizing the power of YARA rules, Atreus employs customizable and intelligent pattern matching techniques to identify files that exhibit characteristics of Ryuk ransomware. These YARA rules are regularly updated to reflect the latest attack patterns and signatures used by Ryuk, ensuring a proactive defense against evolving threats.

4. Non-Production Solution:

Atreus is designed as a research and educational tool rather than a production-grade security solution. While it provides valuable insights into Ryuk ransomware detection, we encourage users to complement Atreus with other enterprise-grade security measures to create a comprehensive defense strategy.


(Note: Atreus is not intended for commercial use and should be treated as an educational and research tool. It is provided as-is without warranties or guarantees.)
"""
        
        self.tabview1 = customtkinter.CTkTabview(self, width=250,height=300)
        self.tabview1.grid(row=2, column=1, padx=(20, 10), pady=(10, 0), sticky="nsew")
        self.tabview1.add("Ryuk Ransomware")
        self.tabview1.add("About Atreus")
        self.tabview1.tab("Ryuk Ransomware").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview1.tab("About Atreus").grid_columnconfigure(0, weight=1)
  
        self.textbox1 = customtkinter.CTkTextbox(master=self.tabview1.tab("Ryuk Ransomware"),height=300)
        self.textbox1.grid(padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.textbox1.insert("0.0",ryuk_ransomware_description)
        
        self.textbox2 = customtkinter.CTkTextbox(master=self.tabview1.tab("About Atreus"),height=300)
        self.textbox2.grid(padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.textbox2.insert("0.0",atreus_description)
        
        # set default values
        self.appearance_mode_optionemenu.set("System")
        self.scaling_optionemenu.set("100%")


        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        

    def open_file(self,name):
        file_path = fr'logs\{name}'
        try:
            subprocess.run(['notepad', file_path], check=True)
        except subprocess.CalledProcessError:
            print("Error: Unable to open the file in Notepad.")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def watchdog_event(self):
        self.sidebar_button_1.configure(state="disabled", text="Watchdog Running")
        def run_as_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "watchdog.exe", None, None, 1)
        thread = threading.Thread(target=run_as_admin)
        thread.start() 
        
    def static_event(self):
        self.sidebar_button_2.configure(state="disabled", text="Static scanning")
        def run_as_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "trace_executables.exe", None, None, 1)
        thread = threading.Thread(target=run_as_admin)
        thread.start() 

    def registry_event(self):
        self.sidebar_button_3.configure(state="disabled", text="Registry scanning")
        def run_as_admin():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "trace_registry.exe", None, None, 1)
        thread = threading.Thread(target=run_as_admin)
        thread.start() 
        
    def first_update(self):
        # Schedule the function to run again after 5 seconds
        self.after(1000, self.update)

    def look_for_logs(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Logs"))
        self.scrollable_frame.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        logs_list = self.get_files_in_logs_directory("logs")
        self.logs_buttons = []
        self.logs_names = []
        if len(logs_list)>0:
            for i,bt in enumerate(logs_list):
                self.logs_names.append(bt)
                button = customtkinter.CTkButton(self.scrollable_frame, text=self.logs_names[i],
                                                               command=partial(self.open_file,self.logs_names[i]))
                button.grid(row=i, column=0,padx=(100, 20), pady=(20, 0))
                self.logs_buttons.append(button)
        else:
            button = customtkinter.CTkButton(self.scrollable_frame, text="No logs available",state="disabled")
            button.grid(row=0, column=0,padx=(100, 20), pady=(20, 0))

    def look_for_dumps(self):
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Dumps"))
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.scrollable_frame1 = customtkinter.CTkScrollableFrame(self.tabview.tab("Dumps"))
        self.scrollable_frame1.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        dumps_list = self.get_files_in_logs_directory("dump")
        self.dump_buttons = []
        self.dump_names = []
        if len(dumps_list)>0:
            for i,bt in enumerate(dumps_list):
                self.dump_names.append(bt)
                button = customtkinter.CTkButton(self.scrollable_frame1, text=self.dump_names[i],state="disabled")
                button.grid(row=i, column=0,padx=(100, 20), pady=(20, 0))
                self.dump_buttons.append(button)
        else:
            button = customtkinter.CTkButton(self.scrollable_frame1, text="No dumps available")
            button.grid(row=0, column=0,padx=(100, 20), pady=(20, 0))
    def look_for_files(self):
        self.scrollable_frame2 = customtkinter.CTkScrollableFrame(self.tabview.tab("Files"))
        self.scrollable_frame2.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        list1 = self.get_json_keys("sigcheck_detected_files.json")
        list2 = self.get_json_keys("yara_detected_files.json")
        files_list = list(set(list1) | set(list2))
        self.files_buttons = []
        self.files_names = []
        if len(files_list)>0:
            for i,bt in enumerate(files_list):
                self.files_names.append(bt)
                button = customtkinter.CTkButton(self.scrollable_frame2, text=self.files_names[i])
                button.grid(row=i, column=0,padx=(100, 20), pady=(20, 0))
                self.files_buttons.append(button)
        else:
            button = customtkinter.CTkButton(self.scrollable_frame2, text="No suspected files detected")
            button.grid(row=0, column=0,padx=(100, 20), pady=(20, 0))
        

    @staticmethod
    def get_json_keys(json_file_name):
        keys_list = []

        try:
            with open(json_file_name, 'r') as json_file:
                try:
                    data = json.load(json_file)
                    if isinstance(data, dict):
                        keys_list = list(data.keys())
                except json.JSONDecodeError:
                    print(f"Error: Unable to decode JSON from {json_file_name}.")
        except FileNotFoundError:
            print(f"Error: {json_file_name} not found.")

        return keys_list

    @staticmethod
    def get_files_in_logs_directory(directory_name):
        files_list = []
        current_directory = os.getcwd()
        logs_directory = os.path.join(current_directory, directory_name)
        if not os.path.exists(logs_directory) or not os.path.isdir(logs_directory):
            print("The 'logs' directory does not exist.")
            return files_list
        try:
            files_list = os.listdir(logs_directory)
        except OSError as e:
            print(f"Error while accessing files in the 'logs' directory: {e}")
            return files_list

        return files_list
        
    @staticmethod
    def is_process_running(process_name):
            try:
                result = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq {process_name}', '/NH'], 
                        capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
                output = result.stdout.strip()
                return process_name.lower() in output.lower()
            except Exception as e:
                print(f"Error checking process status: {e}")
                return False
        
    def update(self):
        watchdog_name = "watchdog.exe"
        trace_executables_name = "trace_executables.exe"
        trace_registry_name = "trace_registry.exe"
        #Checking if processes are running
        if self.is_process_running(watchdog_name):
            self.sidebar_button_1.configure(state="disabled", text="Watchdog Running")
        else:
            self.sidebar_button_1.configure(state="enabled", text="Activate Watchdog")

        if self.is_process_running(trace_executables_name):
            self.sidebar_button_2.configure(state="disabled", text="Static scanning")
        else:
            self.sidebar_button_2.configure(state="enabled", text="Run Static scan")

        if self.is_process_running(trace_registry_name):
            self.sidebar_button_3.configure(state="disabled", text="Registry scanning")
        else:
            self.sidebar_button_3.configure(state="enabled", text="Run Registry scan")
            
        #Checking Logs List
        self.look_for_logs()            
        #Checking dumps
        self.look_for_dumps()
        #Checking files
        self.look_for_files()
            
        self.after(3000, self.update)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
