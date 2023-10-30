#!/usr/bin/python3

# Function which prints the last digit of a number
def print_last_digit(number):
    """
    Print the last digit of a given number after converting it to its absolute value.

    Parameters:
    number (int): The input number.

    Returns:
    None
    """
    number = abs(number)
    last_digit = number % 10
    return last_digit
