import subprocess
import time

def run_process(command, timeout):
    global process
    try:
        start_time = time.time()
        process = subprocess.Popen(command, shell=True)
        process.communicate(timeout=timeout)
        end_time = time.time()

        if process.returncode == 0:
            print(f"Process '{command}' completed within {timeout} seconds.")
        else:
            print(f"Process '{command}' did not complete successfully within {timeout} seconds.")

        print(f"Elapsed time: {end_time - start_time} seconds\n")
    except subprocess.TimeoutExpired:
        process.terminate()
        print(f"Process '{command}' timed out after {timeout} seconds and was terminated.\n")


def main():
    with open('processes', 'r') as file:
        lines = file.readlines()

    for line in lines:
        command, timeout = line.strip().split(',')
        timeout = int(timeout)

        run_process(command, timeout)


if __name__ == "__main__":
    main()

