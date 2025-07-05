# rock, paper,scissors game
import random

options = ("rock", "paper", "scissors")
playing = True
while playing:
    player = None
    bot = random.choice(options)
    while player not in options:
        player = input("Pick between (rock or paper or scissors): ")

        print(f"Player: {player}")
        print(f"Bot: {bot}") 

    if player == bot:
        print("It's a tie!")
    elif player == "rock" and bot == "paper":
        print("The bot WON!!!")
    elif player == "rock" and bot == "scissors":
        print("The player WON!!!")
    elif player == "paper" and bot == "scissors":
        print("The player WON!!!")
    elif player == "paper" and bot == "rock":
        print("The bot WON!!!")
    elif player == "scissors" and bot == "rock":
        print("The player WON!!!")
    elif player == "scissors" and bot == "paper":
        print("The bot WON!!!")
    
    if input("PLay again? (y/n): ").lower() == "n":
        playing = False
print("Thanks for playing")