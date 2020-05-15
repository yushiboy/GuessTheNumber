import random
print("Welcome to the guessing game!")
print("You will have to guess a number between 0 and 10")
guess = 11
number = random.randint(0,10)
userguess = input("What is your guess?")
guess = int(userguess)
while guess != number:
    if guess < number:
        print("Guess too low")
        userguess = input("What is your guess?")
        guess = int(userguess)
    elif guess > number:
        print("Guess too high")
        userguess = input("What is your guess?")
        guess = int(userguess)
print("You successfully guessed the number")