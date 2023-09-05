#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % -10 if number < 0 else number % 10
phrase = "Last digit of " + str(number) + " is " + str(last_digit) + " and is"
if last_digit > 5:
    print(f"{phrase} greater than 5")
elif last_digit == 0:
    print(f"{phrase} 0")
else:
    print(f"{phrase} less than 6 and not 0")
