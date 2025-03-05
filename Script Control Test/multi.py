import subprocess

# Start the Python interpreter as a subprocess
process = subprocess.Popen(
    ['python', '-i'],  # -i flag starts the interpreter in interactive mode
    stdin=subprocess.PIPE,  # To send commands to the interpreter
    stdout=subprocess.PIPE,  # To receive outputs
    stderr=subprocess.PIPE,  # To capture errors
    text=True  # Use text mode for I/O
)
# Define a helper function to send commands and get responses
def run_command(command):
    process.stdin.write(command + '\n')  # Send the command
    print("hi")
    process.stdin.flush()  # Ensure it's sent immediately
    print("hi")
    # Capture the output
    output = []
    while True:
        line = process.stdout.readline()
        print("shit")
        if line.strip() == "":  # Break when there's no more immediate output
            print("ha?")
            break
        output.append(line)
        print("what?")
    return ''.join(output)

# Example commands
print("Response from Python:", run_command('print("Hello from the subprocess!")'))
print("Response from Python:", run_command('x = 5'))
print("Response from Python:", run_command('x + 10'))
print("Response from Python:", run_command('exit()'))  # Exit the interpreter

# Clean up
process.wait()
