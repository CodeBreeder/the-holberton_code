#!/usr/bin/python3
# Print the combination of two digits number
for number in range(0, 100):
    if number != 99:
        print("{:02}".format(number), end=',')
    else:
        print("{}".format(number), end='')
