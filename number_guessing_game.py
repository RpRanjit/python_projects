import random
print(f"Let's start number guessing game. \n Lte's start!!")
low = int(input("Enter the lower number: "))
high = int(input("Enter the heigher number: "))

num = random.randint(low, high)
count = 0
guess_count = 7

while count < guess_count:
    count += 1
    guess = int(input("Enter you guess: "))

    if guess == num:
        print(f"Congralutation you have guess right number that is {num}. You find the number in {count} counts.")
        break

    elif count >= guess_count and guess != num:
        print(f"you lost you chance try again")
    
    elif guess < num:
        print(f"Your guess number {guess} is too low. Try with a higher number") 
    elif guess > num:
        print(f"Your guess number {guess} is too high. Try with a lower number") 
    
        
