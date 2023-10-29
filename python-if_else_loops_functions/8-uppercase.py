#!/usr/bin/python3

# Update string to uppercase letters
def uppercase(str):
    """
    Convert a string to uppercase, leaving non-alphabetical characters unchanged.

    Parameters:
    s (str): The input string to be converted to uppercase.

    Returns:
    str: The input string with all alphabetical characters converted to uppercase.
    """
    for letter in str:
        if 'a' <= letter <= 'z':
            char = ord(letter) - 32
            print("{}".format(chr(char)), end='')
        else:
            print("{}".format(letter), end='')
