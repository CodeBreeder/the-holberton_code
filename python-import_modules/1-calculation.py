#!/usr/bin/pythob3

"""
This code block demonstrates basic arithmetic operations 
using a calculator module (calculator_1) when the script 
is executed as the main program.

Usage:
    - The 'calculator_1' module is imported as 'calc'.
    - Two variables 'a' and 'b' are initialized 
    with the values 10 and 5, respectively.
    - The code calculates and prints the results of four operations: 
    addition, subtraction, multiplication, and division using the 
    'add', 'sub', 'mul', and 'div' functions from the 'calculator_1' module.
    - The results are printed to the console in a human-readable format.

Example:
    If executed as the main program, this code block will print the 
    results of the following operations:
    - 10 + 5 = 15
    - 10 - 5 = 5
    - 10 * 5 = 50
    - 10 / 5 = 2.0
"""
if __name__ == '__main__':
    import calculator_1 as calc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
