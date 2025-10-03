import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 10 and 20.")
print("I will tell you if your guess is too high or too low.")

number = random.randint(10, 20)
guesses = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    guesses += 1

    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
    elif guess < number:
        print("Wrong guess. Your guess is too low. Try again!")
    else:
        print("Wrong guess. Your guess is too high. Try again!")

print("Thanks for playing!")