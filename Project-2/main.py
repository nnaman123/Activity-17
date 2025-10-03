import random
#rock paper scissors game
Playing = True
options = ["rock", "paper", "scissors"]
computer_wins = 0
user_wins = 0
ties = 0

while Playing:
    user_input = input("Type Rock/Paper/Scissors or Quit to quit\n").lower()
    if user_input == "quit":
        break
    if user_input not in options:
        print("Invalid input")
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
        ties += 1
    else:
        print("You lost!")
        computer_wins += 1
    print("You have", user_wins, "wins, the computer has", computer_wins, "wins and you have", ties, "ties.")
    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes":
        Playing = False
print("Thanks for playing!")