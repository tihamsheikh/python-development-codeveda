from random import randint
from os import system 


secret_number = randint(1, 100)

max_attempts = 10
attempts = 0


system('cls' if system == 'nt' else 'clear')
print("A CLI Number Guessing Game\n")   
while attempts <= max_attempts:

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        continue

    attempts += 1

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100.")
        continue

    if guess < secret_number:
        print("Too low!\n")
        print(f"Attempts left: {max_attempts - attempts}\n")
    elif guess > secret_number:
        print("Too high!\n")
        print(f"Attempts left: {max_attempts - attempts}\n")
    else:
        print(f"\nYou guessed the number: {secret_number}\nYour attempsts: {attempts}\n")
        break

    
    

if guess != secret_number:
    print(f"Game over! The correct number was {secret_number}.\n")
