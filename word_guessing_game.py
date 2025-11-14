import random

name = input("Enter your name: ")
print("Good Luck !", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the character.")
guesses = ""
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
            print("You won")
            print("Your guess word is: ", word)
            break

    print()
    guess = input("Enter a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong. You have", + turns , "turns left.")
    if turns == 0:
        print("you loose")



