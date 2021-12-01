"""CLI application for a prefix-notation calculator."""

from arithmetic import *

# Replace this with your code
while True:
    input_string = input("enter equation:")
    split_input_string = input_string.split(" ")

    if ("q" in split_input_string):
        print("exiting calculator application")
        break

    elif (len(split_input_string) < 2):
        print("not enough input")
        continue
        
    operator = split_input_string[0]
    num1 = split_input_string[1]
    num2 = split_input_string[2]

    result = None

    if (not num1.isdigit() or not num2.isdigit()):
        print("Those aren't numbers!")
        continue

    elif operator == "+":
        result = add(float(num1), float(num2))

    else:
        result = "Please enter an operator followed by two integers."
        break
    print(result)
    

