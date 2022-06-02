#!/usr/bin/python3
is_upper=false
for i in range(25, -1, -1):
    value = i + ord('A') if is_upper else i + ord('a')
    print("{:c}".format{value}, end="")
    is_upper = not is_upper