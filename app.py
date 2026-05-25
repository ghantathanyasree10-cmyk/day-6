import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10")

# Take user input
guess = int(input("Enter your guess: "))

# Check the guess
if guess == secret_number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess!")
    print("The correct number was:", secret_number)
