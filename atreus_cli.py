from controller import Controller
import ctypes
import os
import sys
from prettytable import PrettyTable

class InteractiveController:
    def __init__(self) -> None:
        self.controller = Controller()

    def print_options(self):
        print("Choose an action:")
        print("1. Dump process by PID")
        print("2. Get process details by PID")
        print("3. Get details of all running processes")
        print("4. Get DLLs from process by PID")
        print("5. Get DLLs from all running processes")
        print("6. Scan the registry")
        print("7. Scan specified directories for suspicious files")
        print("8. Monitor files created (Sysmon)")
        print("9. Trace CreateRemoteThread calls (Sysmon)")
        print("10. Suspend a process by PID")
        print("11. Resume a suspended process by PID")
        print("12. Kill a process by PID")
        print("0. Quit")

    def execute_action(self, option):
        if option == "1":
            pid = int(input("Enter the PID of the process to dump: "))
            self.controller.dump_process(pid)
        elif option == "2":
            pid = int(input("Enter the PID of the process to get details: "))
            print(self.controller.detail_process(pid))
        elif option == "3":
            print("\nScanning all processes...\n")
            processes_details = self.controller.detail_all_process()
            tab = PrettyTable(list(list(processes_details.values())[0].keys()))
            for process_detail in processes_details:
                tab.add_row(list(process_detail.values()))
            print(tab)
        elif option == "4":
            pid = int(input("Enter the PID of the process to get DLLs from: "))
            print(self.controller.dlls_from_process(pid))
        elif option == "5":
            print(self.controller.dlls_from_all_processes())
        elif option == "6":
            print("Registry scan result:", self.controller.scan_registry())
        elif option == "7":
            self.controller.scan_files()
            print("Results written to suspected_files.json")
        elif option == "8":
            count = int(input("Enter the number of files to monitor (default=100): "))
            print(self.controller.monitor_files_created(count))
        elif option == "9":
            print(self.controller.trace_create_remote_thread_call())
        elif option == "10":
            pid = int(input("Enter the PID of the process to suspend: "))
            print("Process suspended:", self.controller.suspend_process(pid))
        elif option == "11":
            pid = int(input("Enter the PID of the process to resume: "))
            print("Process resumed:", self.controller.resume_process(pid))
        elif option == "12":
            pid = int(input("Enter the PID of the process to kill: "))
            print("Process killed:", self.controller.kill_process(pid))
        elif option == "0":
            print("Exiting the interactive controller.")
            exit()
        else:
            print("Invalid option. Please try again.")

    def run(self):
        while True:
            self.print_options()
            option = input("Enter the option number: ")
            self.execute_action(option)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False

def main():
    if not is_admin():
        print("This script requires administrator privileges to run.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    atreus = r"""
    _______ _________ _______  _______           _______ 
    (  ___  )\__   __/(  ____ )(  ____ \|\     /|(  ____ \
    | (   ) |   ) (   | (    )|| (    \/| )   ( || (    \/
    | (___) |   | |   | (____)|| (__    | |   | || (_____ 
    |  ___  |   | |   |     __)|  __)   | |   | |(_____  )
    | (   ) |   | |   | (\ (   | (      | |   | |      ) |
    | )   ( |   | |   | ) \ \__| (____/\| (___) |/\____) |
    |/     \|   )_(   |/   \__/(_______/(_______)\_______)
                                                        
    """.center(80)
    print(atreus)
    print("Anti-Ransomware Ryuk software.".center(30))
    print()
    print("Disclaimer: Not intended to be a production Counter Measure, only a good approach to identify and mitigate Ryuk actions.".center(80))
    interactive_controller = InteractiveController()
    interactive_controller.run()

if __name__ == "__main__":
    main()
