import random

# options = ('r', 'p', 's')
# emojis = {'r': '🪨', 'p': '📃', 's': '✂︎'}

# while True:
# user_choice = input('Enter rock, paper, or scissors r/p/s: ').lower()

# if user_choice not in options:
#     print('Invalid input, please enter r, p, or s.')
#     continue

# computer_choice = random.choice(options)

# print(f'You chose {emojis[user_choice]}')
# print(f'Computer chose {emojis[computer_choice]}')

# if user_choice == computer_choice:
#     print('It\'s a tie!')
# elif ((user_choice == 'r' and computer_choice == 's') or
#       (user_choice == 'p' and computer_choice == 'r') or
#       (user_choice == 's' and computer_choice == 'p')):
#     print('You win!')
# else:
#     print('Computer won!')

# play_again = input('Play again? (y/n): ').lower()
# if play_again != 'y':
#     print('Thank you for playing!')
#     break

ROCK = 'r' 
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '🪨', PAPER: '📃', SCISSORS: '✂︎'}
options = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input('Enter rock, paper, or scissors r/p/s: ').lower()

        if user_choice in options:
            return user_choice
        else:
            print('Invalid input, please enter r, p, or s.')
            continue


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif ((user_choice == ROCK and computer_choice == SCISSORS) or
          (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSORS and computer_choice == PAPER)):
        print('You win!')
    else:
        print('Computer won!')


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(options)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        play_again = input('Play again? (y/n): ').lower()
        if play_again != 'y':
            print('Thank you for playing!')
            break

play_game()