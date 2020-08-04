#!/usr/bin/python3
#range(x, y, z)

# x= number you begin counting from
# y= number you count UP (or down) just short of... this number will not be included in the range!
# z= the increment you'll move by- 1 goes up by one, -2 goes down by two.

for x in range(0, 10):
    print(x, end = " ")
print('\n')
for x in range(4, 31, 2):
    print(x, end = " ")
print('\n')

answer = " "
while answer != "q":
    bottles = int(input("Please input how many bottles of beer you're counting down from!"))
    if bottles <= 100:
        for x in range(bottles, 0, -1):
            print(f"{x} bottles of beer on the wall!")
            print(f"{x} bottles of beer on the wall! {x} bottles of beer! You take one down, pass it around!")
    else:
        print("You put a wrong number. Please put a number not greater than 100.")

    answer = input("\n Press ENTER to try again or press Q to quit!")
    answer = answer.lower()
