#Write a short guessing game program using a while loop. The user should be prompted
#to guess a number between 1 and 100, and you should tell them whether their guess was
#too high or too low after each guess. The loop should keeping running until the user
#guesses the number correctly.

import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

# Start the game loop
while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            continue
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number correctly!")
            break  # Exit the loop
    except ValueError:
        print("Invalid input! Please enter a valid number.")
