#!/usr/bin/python3

import random

# Evaluate assigned random numbers
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is 0")
else:
    print(f"{number} is negative")
