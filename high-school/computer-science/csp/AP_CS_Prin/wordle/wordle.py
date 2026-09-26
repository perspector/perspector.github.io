import random
from colorama import Fore, Back

#Takes a text file and fills a list with its contents
wordList = []
with open('5LetterWords.txt','r') as file:
    for line in file:
        for word in line.split():
            wordList.append(word)

#Picks a random word from the file
#randNum = random.randint(1, 5757)

solution = random.choice(wordList)
while solution[-1] == "s":  # eliminate plurals
    solution = random.choice(wordList)


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(solution)

attempts = 1
print(f"\n\n==========| Attempt {attempts} |==========")
guess = input("Enter a 5 letter word: ")

while len(guess) != 5:
    guess = input("The guess must be 5 letters long.\nEnter a 5 letter word: ")

while attempts < 6:
    attempts += 1
    
    if guess != solution:
        for letter in range(len(guess)):
            if guess[letter] == solution[letter]:
                print(f"{Back.GREEN}{guess[letter]}{Back.RESET}", end="")
            elif guess[letter] in solution:
                print(f"{Back.YELLOW}{guess[letter]}{Back.RESET}", end="")
            else:
                print(Back.RESET + guess[letter], end="")
        print("\n")  # skips 2 lines, whitespace
        print(f"\n\n==========| Attempt {attempts} |==========")
        guess = input("Enter a 5 letter word: ")

        while len(guess) != 5:
            guess = input("The guess must be 5 letters long.\nEnter a 5 letter word: ")
    else:
        if attempts - 1 == 1:
            print(f'{Fore.GREEN}Correct! Congratulations! You got the word "{solution}" in {str(attempts-1)} attempt.{Fore.RESET}{Back.RESET}')
        else:
            print(f'{Fore.GREEN}Correct! Congratulations! You got the word "{solution}" in {str(attempts-1)} attempts.{Fore.RESET}{Back.RESET}')
        break

if attempts >= 6:
    print(f"{Fore.RED}Whoops, out of guesses. The solution was {Fore.YELLOW}{solution}.{Fore.RESET}", end="")
