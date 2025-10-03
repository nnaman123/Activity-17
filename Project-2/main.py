import random
#rock paper scissors game
options = ["rock", "paper", "scissors"]
computer_wins = 0
user_wins = 0
ties = 0

# A dictionary to define what beats what. The key beats the value.
win_conditions = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    user_input = input("Type Rock/Paper/Scissors or Quit to quit\n").lower()
    if user_input == "quit":
        break

    if user_input not in options:
        print("Invalid input")
        continue

    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
        ties += 1
    elif win_conditions[user_input] == computer_pick:
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

    print(f"You have {user_wins} wins, the computer has {computer_wins} wins, and there are {ties} ties.")

    play_again = input("Do you want to play again? (yes/no)").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")