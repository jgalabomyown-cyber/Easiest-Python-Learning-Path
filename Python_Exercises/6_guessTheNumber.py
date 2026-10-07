# This is guess the number game.
import random
secret_number = random.randint(1, 20)
print('Think of a number between 1 - 20')

# Ask for the player to guess 6 times
for guesses_taken in range(1, 6):
    print('\nYour Guess')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        # This condition is the correct guess!
        break

if guess == secret_number:
    print('Good Job! You got it in ' + str(guesses_taken) + ' guesses')
else:
    print('Nope! The number was ' + str(secret_number))