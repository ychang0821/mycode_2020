#!/usr/bin/env python3


dict = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"},
         "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"},
         "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
answer = " "
while answer != "q":
    char_name = input("Which character do you want to know about? (Flash, Batman, Superman)")
    if char_name.lower() == "flash":
        char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")
        if char_stat.lower() == "strength":
            print(f"Flash's strength is: {dict['flash']['strength']}")
        elif char_stat.lower() == "speed":
            print(f"Flash's speed is: {dict['flash']['speed']}")
        elif char_stat.lower() == "intelligence":
            print(f"Flash's intelligence is: {dict['flash']['intelligence']}")
        else:
            print("Wrong input, please try again")

    elif char_name.lower() == "batman":
        char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")
        if char_stat.lower() == "strength":
            print(f"Batman's strength is: {dict['batman']['strength']}")
        elif char_stat.lower() == "intelligence":
            print(f"Batman's intelligence is: {dict['batman']['intelligence']}")
        else:
            print("Wrong input, please try again")

    elif char_name.lower() == "superman":
        char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")
        if char_stat.lower() == "strength":
            print(f"Superman's strength is: {dict['superman']['strength']}")
        elif char_stat.lower() == "speed":
            print(f"Superman's speed is: {dict['superman']['speed']}")
        elif char_stat.lower() == "intelligence":
            print(f"Superman's intelligence is: {dict['superman']['intelligence']}")
        else:
            print("Wrong input, please try again")
    else:
        print("Wrong input, please try again")

    answer = input("\n Press ENTER to try again or press Q to quit!")
    answer = answer.lower()
