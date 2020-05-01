#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{} argument{}{}".format(len(sys.argv) - 1, "s" if len(sys.argv) != 2 else "\
", ":" if len(sys.argv) > 1 else "."))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
