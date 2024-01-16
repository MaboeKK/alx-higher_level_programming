#!/usr/bin/python3
hex_output = '\n'.join('{} = 0x{:x}'.format(num, num) for num in range(0, 99))
print(hex_output)

