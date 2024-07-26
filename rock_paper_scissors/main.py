import random

options = ['rock','paper','scissors']
wins = 0
losses = 0
rounds = 0


while True:
    
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if(user_input == 'q'):
        quit()
    
    if user_input not in options:
        print('Please type a valid choice')
        continue # goes back to the top of the loop

    
    user_index = options.index(user_input)
    random_number = random.randint(0,2)
    computer_pick = options [random_number]
    
    print(f'Computer picked {options[random_number]} and you picked {options[user_index]}')

    if(user_index == random_number):
        print('It\'s a draw! Let\'s go again!')
        continue

    if user_input == 'rock' and computer_pick == 'scissors':
        print('Round Won!')
        wins += 1
    elif user_input == 'rock' and computer_pick == 'paper':
        print('Round lost!')
        losses += 1

    if user_input == 'paper' and computer_pick == 'rock':
        print('Round Won!')
        wins += 1
    elif user_input == 'paper' and computer_pick == 'scissors':
        print('Round lost!')
        losses += 1

    if user_input == 'scissors' and computer_pick == 'paper':
        print('Round Won!')
        wins += 1
    elif user_input == 'scissors' and computer_pick == 'rock':
        print('Round lost!')
        losses += 1

    rounds += 1
    if rounds == 3:
        if wins > losses:
            print(f'Good job, you won the game!')
        else:
            print('Better luck next time!')
        break
    else:
        if rounds == 2:
            print('Match Point!!!')
            continue
        else:
            print(f'{rounds}/3 rounds! Keep playing! :)')
            continue

