''' Make a game guess the number
Generate random number between 1 to 10 and the u guess what that number can be
only three chance are allowed else print msg "You lost the game"
'''



import random

for i in range (1, 11):
    number= random.randint(1, 10)
    chances = 3

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 to 10. You have 3 chances to guess it.")

    for i in range(chances):
        guess = int(input("Enter your guess: "))
        
        if guess == number_to_guess:
            print("Congratulations! You've guessed the correct number.")
        else:
            print("Wrong guess. Try again.")

    print("You lost the game. The number was:", number)
    break
