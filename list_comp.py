#!/usr/bin/python

import string
import numpy as np

lower = string.ascii_lowercase

first_ten = [lower[i] for i in range(10)]
print(first_ten)

but_six = [first_ten[i] for i in range(10) if i != 5]
print(but_six)

repeated_but_six = [but_six[i]*(j+1)  for i in range(9) for j in range(3)]
print(repeated_but_six)

letter_list = []
f = lambda index : [repeated_but_six[index], repeated_but_six[index+1], repeated_but_six[index+2]]
gridded = [f(i*3) for i in range(9)]
print(gridded)

