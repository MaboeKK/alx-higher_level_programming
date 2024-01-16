#!/usr/bin/python3
def uppercase(s):
    result = ''.join(chr(ord(i) - 32) if 'a' <= i <= 'z' else i for i in s)
    print(result)
