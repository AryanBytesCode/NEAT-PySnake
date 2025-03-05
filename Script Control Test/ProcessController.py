import subprocess

# Start a process and capture stdin and stdout
process = subprocess.Popen(["cmd.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Send commands to the terminal
process.stdin.write('cd "C:/Users/Ymir/Desktop/PARA/01 Projects/Python Snake Project/Script Control Test"')
process.stdin.write("python")
process.stdin.close()

# Get output
output, errors = process.communicate()
print("Output:")
print(output)
