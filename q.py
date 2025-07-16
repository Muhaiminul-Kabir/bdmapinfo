import subprocess

command = "dir"

# Run command as string
result = subprocess.run(command, shell=True, capture_output=True, text=True)

print("STDOUT:")
print(result.stdout)

print("STDERR:")
print(result.stderr)