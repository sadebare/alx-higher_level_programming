#!/usr/bin/python3
from math import remainder
import random
number = random.randint(-10000, 10000)
if number > 0:
    rem = number % 10
elif number < 0:
    rem = number % -10
print("Last digit of", number, "is", rem, end=' ')
if rem > 5:
    print("and is greater than 5")
elif rem == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")