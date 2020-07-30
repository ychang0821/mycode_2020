#!/usr/bin/env python3
"""Calculator"""
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y


answer = " "
while answer != "q":
    try: 
        num1 = float(input("Type a number. "))
        num2 = float(input("Type second number. "))
        print(f"{num1} add {num2} is {add(num1, num2)}")
        print(f"{num1} subtract {num2} is {sub(num1, num2)}")
        print(f"{num1} multiply by {num2} is {mult(num1, num2)}")
        print(f"{num1} divided by {num2} is {div(num1, num2)}")
    except:
        print("You provided incorrect input.")
    answer = input("Press ENTER to type again, or press Q to quit!")
