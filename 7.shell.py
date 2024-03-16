import subprocess

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def main():
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            print("Exiting shell...")
            break
        elif ">" in user_input:
            command, output_file = user_input.split(">", 1)
            command = command.strip()
            output_file = output_file.strip()
            try:
                with open(output_file, "w") as f:
                    subprocess.run(command, shell=True, check=True, stdout=f)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")
        elif "<" in user_input:
            command, input_file = user_input.split("<", 1)
            command = command.strip()
            input_file = input_file.strip()
            try:
                with open(input_file, "r") as f:
                    subprocess.run(command, shell=True, check=True, stdin=f)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command: {e}")
        else:
            execute_command(user_input)

if __name__ == "__main__":
    print("Simple Shell - Type 'exit' to quit")
    main()
