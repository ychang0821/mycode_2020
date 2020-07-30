#!/usr/bin/env python3
filename = input("Please type the name of file to load ")
## create file object in "r"ead mode
configfile = open("/home/student/mycode/cfgread" + filename, "r")

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

number = len(configlist)
print("Number of lines in file: ", number)

print(len(configlist))
## Always close your file
configfile.close()

