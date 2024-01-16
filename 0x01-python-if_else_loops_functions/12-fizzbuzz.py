#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        output = ""
        if number % 3 == 0:
            output += "Fizz"
        if number % 5 == 0:
            output += "Buzz"
        print(output if output else number, end=" ")
