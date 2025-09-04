import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input('Enter a number between 1 and 100: '))
        if guessed_number < number_to_guess:
            print('Too low!')
        elif guessed_number > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number!')
            break
    except ValueError:
        print('Invalid input, please enter a valid number.')
