#!/usr/bin/python3

# Print True for lowercase otherwise False
def islower(c):
    """
    Check if a character is a lowercase letter.

    Parameters:
    c (str): The character to be checked.

    Returns:
    bool: True if the character is a lowercase letter (a-z), False otherwise.
    """
    if isinstance(c, str):
        return ord(c) >= 97 and ord(c) <= 122
