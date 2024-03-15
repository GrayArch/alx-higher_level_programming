#!/usr/bin/python3
if __name__ == '__main__':
    import sys as sy
    length = len(sy.argv) - 1
    if length != 1:
        if length == 0:
            print('{} arrguments.' .format(length))
        else:
            print('{} arguments:'.format(length))
    else:
        print('{} argument:'.format(length))
    for i in range(1, (length + 1)):
        print("{}: {}".format(i, sy.argv[i]))
