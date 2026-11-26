import subprocess
import os
import getpass
import socket

while True:
    un = getpass.getuser()
    hn = socket.gethostname()
    print("policy switcher")
    a = input("1) Remove\n" \
    "2) Revert" \
    "\n" + un + "@" + hn + ":~$ ")
    os.chdir(os.path.expanduser("~/"))
    if a == "1":
        b = input("Are you sure(y\\n)\n" + un + "@" + hn + ":~$ ").lower()
        if b in ("yes", "y"):
            print("Removing policy scripts...")
            print("Downloading files...")
            subprocess.run(["curl", "-OL", "https://sudorayen.github.io/mac-tool/recon15.plist"])
            subprocess.run(["curl", "-OL", "https://sudorayen.github.io/mac-tool/reconstartup.plist"])
            print("Removing files...")
            subprocess.run(["sudo", "rm", "-rf", "/Library/LaunchDaemons/com.jamf.management.startup.plist"])
            subprocess.run(["sudo", "rm", "-rf", "/Library/LaunchDaemons/com.jamfsoftware.task.1.plist"])
            print("Moving files...")
            subprocess.run(["sudo", "mv", os.path.expanduser("~/recon15.plist"), "/Library/LaunchDaemons"])
            subprocess.run(["sudo", "mv", os.path.expanduser("~/reconstartup.plist"), "/Library/LaunchDaemons"])
            print("Renaming files...")
            subprocess.run(["sudo", "mv", "/Library/LaunchDaemons/recon15.plist", "com.jamfsoftware.task.1.plist"])
            subprocess.run(["sudo", "mv", "/Library/LaunchDaemons/reconstartup.plist", "com.jamf.managment.startup.plist"])
            print("Making files permanent...")
            subprocess.run(["sudo", "chflags", "schg", "/Library/LaunchDaemons/com.jamf.managment.startup.plist"])
            subprocess.run(["sudo", "chflags", "schg", "/Library/LaunchDaemons/com.jamfsoftware.task.1.plist"])
            print("Finished")
        elif b in ("no", "n"):
            print("canceled")
            break
        else:
            print("invalid statement type a number")
            continue
    elif a == "2":
        c = input("Are you sure(y\\n)" + un + "@" + hn + ":~$ ").lower()
        if c in ("yes", "y"):
            print("Adding policy scripts")
            print("Downloading files...")
            subprocess.run(["curl", "-OL", "https://sudorayen.github.io/mac-tool/policy15.plist"])
            subprocess.run(["curl", "-OL", "https://sudorayen.github.io/mac-tool/policystartup.plist"])
            print("Removing modified files...")
            subprocess.run(["sudo", "chflags", "noschg", "com.jamf.managment.startup.plist"])
            subprocess.run(["sudo", "chflags", "noschg", "com.jamfsoftware.task.1.plist"])
            subprocess.run(["sudo", "rm", "-rf", "/Library/LaunchDaemons/com.jamf.managment.startup.plist"])
            subprocess.run(["sudo", "rm", "-rf", "/Library/LaunchDaemons/com.jamfsoftware.task.1.plist"])
            print("Moving original files...")
            subprocess.run(["sudo", "mv", os.path.expanduser("~/policy15.plist"), "/Library/LaunchDaemons/"])
            subprocess.run(["sudo", "mv", os.path.expanduser("~/policystartup.plist"), "/Library/LaunchDaemons/"])
            print("Renaming files...")
            subprocess.run(["sudo", "mv", "/Library/LaunchDaemons/policy15.plist", "com.jamfsoftware.task.1.plist"])
            subprocess.run(["sudo", "mv", "/Library/LaunchDaemons/policystartup.plist", "com.jamf.managment.startup.plist"])
            print("Running Jamf scripts...")
            subprocess.run(["sudo", "jamf", "manage"])
            subprocess.run(["sudo", "jamf", "policy"])
            print("Finished")
        elif c in ("n", "no"):
            print("canceled")
            break
        else:
            print("invalid statement type a number")
            continue
    else:
        print("invalid statement type a number")
        continue