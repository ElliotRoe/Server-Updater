import subprocess
import time

fetchCommand = "git fetch origin"
diffCommand = "git diff origin/master"
resetCommand = "git reset --hard origin/master && sudo cp /home/pi/personalWebsite/. /var/www/html/"

while 1 == 1:
    fetchProcess = subprocess.run(fetchCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, check=True,
                                  universal_newlines=True)
    time.sleep(1)
    diffProcess = subprocess.run(diffCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, check=True,
                                 universal_newlines=True)
    time.sleep(0.4)
    foutput = fetchProcess.stdout
    doutput = diffProcess.stdout
    if len(doutput) != 0:
        print("need to update")
        resetProcess = subprocess.run(resetCommand.split(), cwd=r'/home/pi/personalWebsite', stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, check=True,
                                      universal_newlines=True)
        time.sleep(5)
    else:
        print("no differences found")
