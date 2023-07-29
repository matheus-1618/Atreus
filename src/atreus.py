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


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.first_update()
        self.controller = Controller()
        

        # configure window
        self.title("Atreus")
        self.geometry(f"{1200}x{680}")
        
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
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
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
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.tabview.add("Logs")
        self.tabview.add("Dumps")
        self.tabview.add("Files")
        self.tabview.tab("Logs").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Dumps").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Logs"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Logs"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Dumps"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)


        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
      
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
       
      

        # create scrollable frame
        #self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="About Ryuk")
        #self.scrollable_frame.grid(row=1, column=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        #self.scrollable_frame.grid_columnconfigure(0, weight=1)
        #self.textbox1 = customtkinter.CTkTextbox(master=self.scrollable_frame,height=250)
        #self.textbox1.grid(padx=(0, 0), pady=(0, 0), sticky="nsew")
        #self.textbox1.insert("0.0",ryuk_ransomware_description)
        ryuk_ransomware_description = """Ryuk ransomware is a sophisticated and notorious strain of ransomware that emerged in August 2018. It is known for its highly targeted attacks on large organizations, especially in the corporate and government sectors. Ryuk is believed to be operated by a cybercrime group known as Wizard Spider.

The primary purpose of Ryuk ransomware is to encrypt the victim's files, making them inaccessible. Once the files are encrypted, Ryuk displays a ransom note, typically in a "RyukReadMe.txt" file, containing instructions on how to pay the ransom to obtain the decryption key.

Key characteristics of Ryuk ransomware include:

1. Targeted Attacks: Ryuk targets specific organizations and infects their systems after gaining unauthorized access. These attacks often follow an initial infection by other malware, such as TrickBot or Emotet, which are used to gain a foothold in the network.

2. High Ransom Demands: Ryuk's ransom demands are usually significantly higher than those of other ransomware strains. This is because the attackers tailor the ransom amount based on the victim's perceived ability to pay, often demanding millions of dollars.

3. Manual Execution: Ryuk is often manually deployed by the attackers, enabling them to assess the network's value and select the most critical systems to target.

4. Custom Encryption: Ryuk employs a sophisticated encryption algorithm to lock files, making it challenging to decrypt them without the unique decryption key held by the attackers.

5. Evolving Tactics: The Ryuk ransomware is continually evolving, with the attackers refining their techniques to evade detection and increase their success rate.

It's important to note that paying the ransom does not guarantee that the attackers will provide the decryption key or that the files will be recovered. Moreover, it encourages and funds further criminal activities. To defend against ransomware attacks like Ryuk, organizations should focus on proactive cybersecurity measures, such as regular data backups, robust security protocols, and employee training to prevent phishing and social engineering attacks."""

        
        self.tabview1 = customtkinter.CTkTabview(self, width=250,height=300)
        self.tabview1.grid(row=1, column=2, padx=(20, 10), pady=(20, 0), sticky="nsew")
        self.tabview1.add("Ryuk Ransomware")
        self.tabview1.add("About Atreus")
        self.tabview1.tab("Ryuk Ransomware").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview1.tab("About Atreus").grid_columnconfigure(0, weight=1)
        #self.label_tab_3 = customtkinter.CTkLabel(self.tabview1.tab("Ryuk Ransomware"), text=ryuk_ransomware_description)
        self.textbox1 = customtkinter.CTkTextbox(master=self.tabview1.tab("Ryuk Ransomware"),height=300)
        self.textbox1.grid(padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.textbox1.insert("0.0",ryuk_ransomware_description)
        
        #self.label_tab_3.grid(row=0, column=0, padx=20, pady=20)
        self.label_tab_4 = customtkinter.CTkLabel(self.tabview1.tab("About Atreus"), text="Atreus")
        self.label_tab_4.grid(row=0, column=0, padx=20, pady=20)
        #
        
    
        # set default values
        self.sidebar_button_3.configure(state="disabled", text="Run registry Scan")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("CTkOptionmenu")
        #self.slider_1.configure(command=self.progressbar_2.set)
        #self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        process_detail = self.controller.detail_process(os.getpid())
        tab = PrettyTable(list(process_detail.keys()))
        tab.add_row(list(process_detail.values()))
        self.textbox.insert("0.0", tab)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

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
        #current_text = self.textbox.get("1.0", tkinter.END)
        # Check if the file has changed
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
            
        process_detail = self.controller.detail_process(os.getpid())
        tab = PrettyTable(list(process_detail.keys()))
        tab.add_row(list(process_detail.values()))
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert("1.0", tab)
        self.after(3000, self.update)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
