import os


def execute_file(file_path):
    if os.access(file_path, os.X_OK):
        os.system(file_path)
    else:
        print(f"Error: The file '{file_path}' does not have execute permissions.")


file_to_execute = input("Enter file to execute: ")
execute_file(file_to_execute)
