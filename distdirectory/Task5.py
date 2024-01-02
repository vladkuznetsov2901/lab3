import os
import shutil
from multiprocessing import Process, freeze_support

def copy_file(src_path, dest_path):
    try:
        shutil.copy(src_path, dest_path)
        print(f"File '{src_path}' copied to '{dest_path}' successfully.")
    except Exception as e:
        print(f"Error copying file '{src_path}': {e}")

def copy_files_parallel(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    processes = []
    for file_name in os.listdir(source_dir):
        src_path = os.path.join(source_dir, file_name)
        dest_path = os.path.join(destination_dir, file_name)

        process = Process(target=copy_file, args=(src_path, dest_path))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == '__main__':
    freeze_support()
    source_directory = r"D:\Studies\OperationSystems\lab3"
    destination_directory = r"D:\Studies\OperationSystems\lab3\distdirectory"
    copy_files_parallel(source_directory, destination_directory)
