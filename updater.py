import subprocess

bashCommand = "git log"

process = subprocess.run(bashCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                         universal_newlines=True)
output = process.stdout

keyStart = output.find(" ") + 1
keyEnd = output.find("\n")
key = output[keyStart:keyEnd];
print(key)
print(output)
print(key == "29ca5d46f179b767fd7be91cd5af77f56b5f83c9")
