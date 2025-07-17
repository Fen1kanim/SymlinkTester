import os
import subprocess
choice = input("choose neededThing.txt (1) or importantThing.conf (2): ")

def change_file():
    with open("testSym", "w") as f:
        f.write("text ONLY for neededThing.txt")
    input("type Enter to continue...")
    with open("testSym", "w") as f:
        f.write("text for ONLY and ONLY neededThing.txt")

if os.path.islink("testSym") or os.path.exists("testSym"):
    os.remove("testSym")

if choice == "1":
    subprocess.run(["ln", "-s", "./neededThing.txt", "testSym"])
    change_file()

elif choice == "2":
    subprocess.run(["ln", "-s", "./importantThing.conf", "testSym"])
    change_file()

input()

with open("neededThing.txt", "w") as f:
    f.write("")

with open("importantThing.conf", "w") as f:
    f.write("")
