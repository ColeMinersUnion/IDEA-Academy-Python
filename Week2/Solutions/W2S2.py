
"""
Random number guesser game
"""

from random import randint
upper_bound = 20
lower_bound = 1
target = randint(lower_bound, upper_bound)

guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")
while guess != str(target):
    if int(guess) < target:
        print("Too low!")
    elif int(guess) > target:
        print("Too high!")
    guess = input(f"Guess a number between {lower_bound} and {upper_bound}: ")

print(f"Congratulations! You guessed the number: {target}")