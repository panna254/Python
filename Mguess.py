import random

number = random.randint(1, 100)
tries = 0
print("Welcome to the Musa Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Take a guess: ")
    tries += 1
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {tries} tries.")
        break 