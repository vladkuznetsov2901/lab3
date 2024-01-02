import os
import subprocess
import time

def run_processes(directory):
    while True:
        files = [f for f in os.listdir(directory) if f.endswith(('.exe', '.bat', '.cmd'))]

        if not files:
            print("No files found. Waiting for files...")
            time.sleep(5)
            continue

        for file in files:
            file_path = os.path.join(directory, file)
            try:
                subprocess.run(file_path, check=True)
                print(f"Process '{file_path}' completed successfully. Deleting...")
                os.remove(file_path)
            except subprocess.CalledProcessError:
                print(f"Process '{file_path}' failed to execute.")
                continue

def main():
    directory = input("Enter the directory path: ")
    run_processes(directory)

if __name__ == "__main__":
    main()
