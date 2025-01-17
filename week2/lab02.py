import random
# RNG, 1-100, save as targetNumber
# User guesses the number, userGuess
# print "too high" if userGuess > targetNumber
# print "too low" if userGuess < targetNumber
# print "congrats" if userGuess == targetNumber
# track number of guesses
def number_guessing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play a guessing game? (Y/N) ").strip().upper()

    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            return True
        except:
            print("")

    play = input()
    return True