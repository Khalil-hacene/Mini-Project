# Number guessing game
import random

highest_num = 100
lowest_num = 1 
number = random.randint(lowest_num, highest_num)
guesses = 0

print("Welcome to python Number guessing game !!!")
print(f" Select a number between {lowest_num} and {highest_num}.")
print()
while True:
    guess = input("Enter your guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess == number:
            print(f"You have guessed the right number = {number} and after {guesses} Try.")
            break
        elif guess > number:
            print("You are to high!")
        elif guess < number:
            print("You are to low!")
        elif guess < lowest_num or guess > highest_num:
            print(f"Your guess is out of range ")
            print(f"Please put a number between {highest_num} and {lowest_num}.")
        else:
            print("Invalid guess")
            print(f"Please put a number between {highest_num} and {lowest_num}.")