#!/usr/bin/python3
comb_output = ', '.join('{}{}'.format(x, y) for x in range(0, 10) for y in range(x + 1, 10))
print(comb_output)

