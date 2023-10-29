#!/usr/bin/python3

# prints all possible different combinations of two digits
for number in range(10):
    for i in range(number + 1, 10):
        if i != number:
            if number == 8 and i == 9:
                print("{}{}".format(number, i), end=' ')
            else:
                print("{}{}".format(number, i), end=', ')
