###  Lesson 1 Notes: Input, Random Numbers, While loops, If statements

'''
For the lesson today you will scroll through the below program.
Make sure to complete the tasks.
Upload the completed document when finished.
You will need to save it as a .txt to upload in Schoology.
'''
# ---input: strings vs int---
# Uncomment below (delete the single quotes)
'''
string = input("Enter a string: ")
num = int(input("Enter an integer: "))
print("This is a String", string)
print("This is a number that I can mulitiply by 2: ", num, " ,num x 2: ",num*2)
'''
# Comment out the above either use 3 single quotes or # infront of each line.
# ---Random numbers---
# Uncomment below (delete the single quotes)
'''
import random #this line usually goes at the top of a document/program
randomNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20, can you guess what it is?")
print("My number is ", randomNumber, " did you guess correctly?")
'''
# Comment out the above either use 3 single quotes or # infront of each line.
# ---while loop---
# Q1: Using the above code as an example, create a program below that will...
#       1) generate a number from 10 to 30
#       2) allow a user a place to input a number
#       3) Use the while loop to check if the guess is correct
#       4) Use the while loop to allow the user to keep guessing until they guess correctly
# hint: make sure to get input so the user will be able to guess.
# Uncomment below (delete the single quotes)
'''
import random #this line usually goes at the top of a document/program
randomNumber = random.randint(10,30)
guessNumber = int(input("Guess a number between 10 and 30. "))

while (guessNumber != randomNumber):
    guessNumber = int(input("Sorry wrong guess, guess again. "))

print("Correct")
'''
# Comment out the above either use 3 single quotes or # infront of each line.
# --- if conditional statements AND modulo %---
# we use modulo to show the remainder after devision.
# we can use modulo to determine if a number is even or odd.
# Q2:  Add code that will allow a user to input a number (the if statement is provided)
# Uncomment below (delete the single quotes)

number = int(input("Enter a whole number: "))
if (number % 2 == 0):
    print(number ," is even")
else:
    print(number ," is odd")

## Save this document as a .txt and upload to Schoology
## Look for practice programs in Schoology.
