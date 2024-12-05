# Create a program that generates a random number from 1 to 100.
# A user will then guess a number.
# The program will output if the number is correct or if the guess is
# higher than the random number or if the number is
# lower than the random number.
# The user will keep guessing until they get the correct answer.

import random

randNum = random.randint(1, 100)

guess = int(input("Enter an integer between 1 and 100: "))

while guess != randNum:
    if guess > randNum:
        print("\n\nLOWER ~ ", end="")
    elif guess < randNum:
        print("\n\nHIGHER ~ ", end="")

    guess = int(input("Enter an integer between 1 and 100: "))
print("\n\n~~~~~~~~~~\nCORRECT!!!\n~~~~~~~~~~\n")
