import random

num = random.randrange(1000, 10000)
num_str = str(num)
# print(num)  # Uncomment for testing

guess_count = 1
n = input("Enter a 4-digit number (XXXX): ")

while n != num_str:
    # Input validation
    if not n.isdigit() or len(n) != 4 or n[0] == '0':
        print("Invalid input! Enter a 4-digit number (first digit cannot be 0).")
        n = input("Try again: ")
        continue

    correct = 0
    your_digit = ['X']*4

    for i in range(4):
        if n[i] == num_str[i]:
            correct += 1
            your_digit[i] = n[i]

    output = ''.join(your_digit)
    print("***********|||||||||**********")
    if correct == 0:
        print("None of the digits are correct.")
    else:
        print(f"{correct} digit(s) are correct. That is: {output}")
    print("Try guessing other numbers.\n")

    guess_count += 1
    n = input("Enter your next guess: ")

print("***********|||||||||**********")
print(f"🎉 Congratulations! You guessed the number {num_str} in {guess_count} tries.")
