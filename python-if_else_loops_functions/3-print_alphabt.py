#!/usr/bin/python3

# Print alphabets excluding `e and q`
for letter in range(ord('a'), ord('z')):
    if letter != ord('e') and letter != ord('q'):
        print(chr(letter), end='')
