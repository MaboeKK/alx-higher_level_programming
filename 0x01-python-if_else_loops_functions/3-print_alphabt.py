#!/usr/bin/python3
result = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in {'e', 'q'})
print(result)

