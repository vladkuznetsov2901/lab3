import subprocess


def run_process_with_redirected_streams():
    try:
        with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
            process = subprocess.Popen(
                'Test.exe',
                stdin=input_file,
                stdout=output_file,
                stderr=subprocess.PIPE,
                text=True
            )
            process.communicate()

        if process.returncode == 0:
            print("Process completed successfully.")
        else:
            print(f"Process failed with return code {process.returncode}.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_process_with_redirected_streams()
