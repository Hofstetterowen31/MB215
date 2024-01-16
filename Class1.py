#Owen Hofstetter
#Class 1 demo
#2024-01-16

import random

randomNum = random.randrange(1,100)
guessNum = 0
while True:
    sGuess = input("Guess a number: ")
    guess = int(sGuess)
    guessNum += 1
    if guess > randomNum:
        print("Lower!")
    elif guess < randomNum:
        print("Higher")
    else:
        print(f"Congrats you guessed the correct number, {randomNum }, in {guessNum} guesses!")
        exit()



