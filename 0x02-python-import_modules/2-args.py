#!/usr/bin/python3
import sys

def main():
    arg_length = len(sys.argv)
    plural_suffix = 's' if arg_length != 2 else ''

    print(f"{arg_length - 1} argument{plural_suffix}:")

    for i in range(1, arg_length):
        print(f"{i}: {sys.argv[i]}")

if __name__ == "__main__":
    main()
