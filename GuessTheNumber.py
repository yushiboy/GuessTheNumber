import random
print("Welcome to the guessing game!")
print("You will have to guess a number between 0 and 10")
number = random.randint(0,10)
guess = input("What is your guess?")
if guess > number:
    print("The guess was too high")
elif guess < number:
    print("The guess was too low")
else:
    print("Congradulations you guessed the number!")