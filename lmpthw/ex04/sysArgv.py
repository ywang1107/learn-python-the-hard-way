import sys

arguments = sys.argv

for argv in arguments:
    if argv in ["--help","-h"]:
        print("Help msg")
    elif argv == "--flag1":
        print("Turn on flag 1")
    elif argv == "--flag2":
        print("Turn on flag 2")
    elif argv == "--flag3":
        print("Turn on flag 3")
    elif "--hello" in argv:
        for i in range(int(argv[8:])):
            print("hello")