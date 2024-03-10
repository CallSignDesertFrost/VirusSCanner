import os
import subprocess

def scan_file(file_path):
    # Use the clamscan command to scan the file
    command = "clamscan -r -i " + file_path
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"File {file_path} is clean.")
    else:
        print(f"Virus found in file {file_path}:")
        print(stderr.decode())

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            scan_file(file_path)

if __name__ == "__main__":
    # Scan a directory or file provided as a command-line argument
    if len(os.sys.argv) == 1:
        print("Please provide a directory or file to scan.")
    else:
        path = os.sys.argv[1]
        if os.path.isdir(path):
            scan_directory(path)
        elif os.path.isfile(path):
            scan_file(path)
        else:
            print(f"{path} is not a valid file or directory.")