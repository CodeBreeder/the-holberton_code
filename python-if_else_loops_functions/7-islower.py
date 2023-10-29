#!/usr/bin/python3

# Print True for lowercase otherwise False
def islower(c):
    lower = range(65, 91)
    upper = range(97, 123)
    if isinstance(c, str):
        c = ord(c)
    if c in lower:
        return False
    elif c in upper:
        return True
    else:
        return
