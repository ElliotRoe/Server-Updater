import subprocess

fetchCommand = "git fetch --all"
diffCommand = "git diff origin/master"
resetCommand = "git reset --hard origin/master"
copyCommand = "sudo cp /home/pi/personalWebsite/. /var/www/html/"

fetchProcess = subprocess.run(fetchCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, check=True,
                              universal_newlines=True)
diffProcess = subprocess.run(diffCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, check=True,
                             universal_newlines=True)

foutput = fetchProcess.stdout
doutput = diffProcess.stdout

if len(doutput) != 0:
    print("need to update")
    resetProcess = subprocess.run(resetCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, check=True,
                                  universal_newlines=True)
    routput = resetProcess.stdout
    copyProcess = subprocess.run(copyCommand.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True,
                                 universal_newlines=True)
    coutput = copyProcess.stdout
else:
    print("no differences found")
