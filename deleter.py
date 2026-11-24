import time
import subprocess

print("*Deleter*\n" \
"(type a number)")
while True:
    a = input("" \
    "1) iMovie      4) Company Portal\n" \
    "2  Sphero Edu  5) Google Chrome\n" \
    "3) GarageBand  6) Microsoft Edge\n"
    "=> ")

    if a == "1":
        print("*iMove*")
        one = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if one == "1":
            print("blocking iMovie...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/iMovie.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/iMovie.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/iMovie.app"])
            print("succesfully blocked")
        elif one == "2":
            print("Unblocking iMovie...")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/iMovie.app"])
            subprocess.run(["sudo", "chflags", "nohidden", "/Applications/iMovie.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/iMovie.app"])
            print("succesfully unblocked")
        else:
            print("Give a valid answer")
    if a == "2":
        print("*Sphero Edu*")
        two = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if two == "1":
            print("Blocking Sphero Edu...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Sphero Edu.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/Sphero Edu.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/Sphero Edu.app"])
            print("succesfully Blocked")
        elif two == "2":
            print("Unblocking Sphero Edu")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/Sphero Edu.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Sphero Edu.app"])
            print("succesfully Unblocked")
        else:
            print("Give a valid answer")
    if a == "3":
        print("*GarageBand*")
        three = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if three == "1":
            print("Blocking GarageBand...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/GarageBand.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/GarageBand.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/GarageBand.app"])
            print("succesfully Blocked")
        elif three == "2":
            print("Unblock GarageBand...")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/GarageBand.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/GarageBand.app"])
            print("succesfully Unblocked")
        else:
            print("Give a valid answer")

    if a == "4":
        print("*Company Portal*")
        four = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if four == "1":
            print("Blocking Company Portal...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Company Portal.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/Company Portal.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/Company Portal.app"])
            print("succesfully Blocked")
        elif four == "2":
            print("Unblocking Company Portal...")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/Company Portal.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Company Portal.app"])
            print("succesfully Unblocked")
        else:
            print("Give a valid answer")

    if a == "5":
        print("*Google Chrome*")
        five = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if five == "1":
            print("Blocking Google Chrome...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Google Chrome.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/Google Chrome.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/Google Chrome.app"])
            print("succesfully Blocked")
        elif five == "2":
            print("Unblocking Google Chrome...")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/Google Chrome.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Google Chrome.app"])
            print("succesfully Unblocked")
        else:
            print("Give a valid answer")

    if a == "6":
        print("*Microsoft Edge*")
        six = input("1) Block\n" \
        "2) Unblock\n" \
        "=> ")
        if six == "1":
            print("Blocking Microsoft Edge...")
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Microsoft Edge.app/Contents"])
            subprocess.run(["sudo", "chflags", "hidden", "/Applications/Microsoft Edge.app"])
            subprocess.run(["sudo", "chflags", "schg", "/Applications/Microsoft Edge.app"])
            print("succesfully Blocked")
        elif six == "2":
            print("Unblocking Microsoft Edge...")
            subprocess.run(["sudo", "chflags", "noschg", "/Applications/Microsoft Edge.app"])
            subprocess.run(["sudo", "rm", "-rf", "/Applications/Microsoft Edge.app"])
            print("succesfully Unblocked")