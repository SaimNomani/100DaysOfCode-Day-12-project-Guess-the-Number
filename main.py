import random
from art import logo


def set_difficulty():
    difficulty = (input("Chose a difficulty. Type 'easy' or 'hard': ")).lower()
    if difficulty == 'easy':
        attempts = 10
        return attempts
    elif difficulty == 'hard':
        attempts = 5
        return attempts
    else:
        return 0


def check_guess(number, guess, attempts):
    if guess == number:
        print(f"You got it. It was {guess}")
        return -1
    elif guess > number:
        print("Too High")
        attempts -= 1
        return attempts
    elif guess < number:
        print("Too low")
        attempts -= 1
        return attempts


def play():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I am thinking a number between 1 and 100")
    attempts = set_difficulty()
    if attempts != 0:
        number = random.randint(1, 100)
        guess = 0
        while attempts > 0:
            print(f"you have {attempts} attempts left")
            guess = int(input("Make a guess: "))
            attempts = check_guess(number, guess, attempts)
            if attempts == -1:
                break
            if attempts > 0:
                print("Guess again: ")
            if attempts == 0:
                print(f"You've run out of guesses, you lose. Actual number was: {number}")
                break
    else:
        print('Wrong request')
    choice = (input("Do you want to start again: type 'y' to start or 'n' to exit: ")).lower()
    if choice == 'y':
        play()


play()
