#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0

    if len(argv) - 1 == 0:
        sum = 0
        print("{}".format(sum))
    else:
        for i in range(1, len(argv)):
            sum += int(argv[i])

        print("{}".format(sum))
