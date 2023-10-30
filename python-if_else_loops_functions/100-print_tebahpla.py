#!/usr/bin/python3

# Print alphabet in alternating cases
def alpha_size():
    """
    Print the alphabet in alternating cases starting from 'z' in 
    lowercase and 'Z' in uppercase.
    The alphabet is constructed by iterating through the English 
    alphabet letters in reverse order.
    """
    alpha_cases = " ".join([chr(ord('z') - i) if i % 2 == 0 \
        else chr(ord('Z') - i) for i in range(26)])
    print(alpha_cases)
