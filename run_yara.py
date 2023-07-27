import yara
import os

if __name__ == "__main__":
    target_directory = r"C:\Users\Matheus\Desktop"  # Replace with the directory you want to scan
    rules = yara.compile(r"c:\Users\Matheus\Desktop\rule.yar")

    # Check if the provided path is a directory
    if not os.path.isdir(target_directory):
        print("Error: The specified path is not a directory.")
    else:
        # Iterate through all files in the directory
        for file_name in os.listdir(target_directory):
            # Check if the item is a file (not a directory or symbolic link)
            file_path = os.path.join(target_directory, file_name)
            if os.path.isfile(file_path):
                matches = rules.match(file_path)
                if matches:
                    print(os.path.join(target_directory, file_name))
                    #print(matches)
