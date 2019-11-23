import subprocess

fetchCommand = "git fetch --all"
diffCommand = "git diff origin/master"

fetchProcess = subprocess.run(fetchCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                              universal_newlines=True)
foutput = fetchProcess.stdout
doutput = ""

if len(foutput) != 16:
    diffProcess = subprocess.run(diffCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                                 universal_newlines=True)
    doutput = diffProcess.stdout
    if len(doutput) != 0:
        print("need to update")
    else:
        print("no differences found")
else:
    print("no update needed")