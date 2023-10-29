#!/usr/bin/python3

# Print the combination of two digits number
for number in range(0, 100):
    for inner_number in range(number):
        if inner_number != 8 and number != 9:
            print(inner_number)