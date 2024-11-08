#Magic Number Guessing Game

import random

number = random.randint(0, 20)
guess = -1

while guess != number:
    guess = int(input("Guess the magic number between 0 and 20: "))
    if guess == number:
        print("Congratulations!You choose right ")
    else:
        print("Guess again!")
