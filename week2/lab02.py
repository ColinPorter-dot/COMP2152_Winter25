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
            userGuess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if userGuess == targetNumber:
                print(f"Congratulations, you guessed it in {attempts} tries!")
            elif userGuess < targetNumber:
                if (userGuess - targetNumber) <= 5:
                    print("Too low, you're really close!")
                else:
                    print("Too low, try again.")
            else:
                if (targetNumber - userGuess) >= 5:
                    print("Too high, you're really close!")
                else:
                    print("Too high, try again.")
            return True
        except ValueError:
            print("Invalid input. Please try again, between 1 and 100.")
    print(f"Game Over. The target number is {targetNumber}.")
    play = input()
    return True

number_guessing_game()