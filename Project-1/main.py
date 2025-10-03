import random
Playing = True
number = str(random.randint(10, 20))

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 10 and 20.")
print("You have to guess the number and i will tell you if you are right or wrong and i will tell you how many guesses you took to get the right number and also tell you if your guess is too high or too low.")
guesses = 0

while Playing:
    guess = input("Enter your guess: ")
    guesses += 1
    if guess == number:
        print("Congratulations! You guessed the number in " + str(guesses) + " guesses.")
        Playing = False
    else:
        print("Wrong guess. Try again!")
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
print("Thanks for playing!")