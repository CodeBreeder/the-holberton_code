#!/usr/bin/python3

if __name__ == '__main__':
"""
This code imports a function 'add' from the 'add_0' module and 
demonstrates its usage by adding two numbers and printing the result.

Usage:
    - The 'add' function is imported from the 'add_0' module.
    - Two variables 'a' and 'b' are initialized with the values 1 
    and 2, respectively.
    - The 'add' function is called with arguments 1 and 2, 
    which adds the two numbers together.
    - The result of the addition is printed to the console.

Example:
    If 'add(1, 2)' is called, it will print '3' 
    to the console, which is the sum of 1 and 2.
"""
from add_0 import add

a = 1
b = 2

print("{} + {} = {}".format(a, b, add(a, b)))
