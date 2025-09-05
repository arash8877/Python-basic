import random

options = ('r', 'p', 's')
emojis = {'r': '🪨', 'p': '📃', 's': '✂︎'}

while True:
    user_choice = input('Enter rock, paper, or scissors r/p/s: ').lower()

    if user_choice not in options:
        print('Invalid input, please enter r, p, or s.')
        continue

    computer_choice = random.choice(options)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print('You win!')
    else:
        print('Computer won!')

    play_again = input('Play again? (y/n): ').lower()
    if play_again != 'y':
        print('Thank you for playing!')
        break
