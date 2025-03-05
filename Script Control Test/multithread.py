import subprocess
import threading
from queue import Queue, Empty

# Start the Python interpreter as a subprocess
process = subprocess.Popen(
    ['python', '-i'],  # Interactive mode
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Create a queue to store the output from the subprocess
output_queue = Queue()

# Function to read output from the subprocess and store it in the queue
def read_output(pipe, queue):
    for line in iter(pipe.readline, ''):  # Keep reading lines until the pipe closes
        queue.put(line)
    pipe.close()

# Start a thread to read stdout
thread = threading.Thread(target=read_output, args=(process.stdout, output_queue))
thread.daemon = True  # Ensure the thread closes when the main program exits
thread.start()

# Helper function to send commands and get responses
def run_command(command):
    process.stdin.write(command + '\n')  # Send command
    process.stdin.flush()

    # Collect output until there's no more (brief timeout for responsiveness)
    output = []
    while True:
        try:
            line = output_queue.get(timeout=0.1)  # Timeout to avoid blocking
            output.append(line)
        except Empty:  # No more output available
            break
    return ''.join(output)

# Example commands
print("Response from Python:", run_command('print("Hello from the subprocess!")'))
print("Response from Python:", run_command('x = 5'))
print("Response from Python:", run_command('x + 10'))
print("Response from Python:", run_command('exit()'))  # Exit the interpreter

# Wait for the subprocess to finish
process.wait()
