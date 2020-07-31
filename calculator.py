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

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

answer = " "
while answer != "q":
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Type a number. "))
            num2 = float(input("Type second number. "))
            if choice == '1':
                print(f"{num1} add {num2} is {add(num1, num2)}")
            if choice == '2':
                print(f"{num1} subtract {num2} is {sub(num1, num2)}")
            if choice == '3':
                print(f"{num1} multiply by {num2} is {mult(num1, num2)}")
            if choice == '4':
                print(f"{num1} divided by {num2} is {div(num1, num2)}")
        except:
            print("You provided wrong input.")
        answer = input("Press ENTER to calculate again, or press Q to quit!")
