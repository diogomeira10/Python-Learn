'''Game Rules

Players: The game is typically played by two players.

Objective: The objective is to be the first player to reach 100 points.

Gameplay:
Players take turns to roll a six-sided die.
A player can roll the dice as many times as they like during their turn.
The points rolled on the die are accumulated to a temporary score for that turn.
If the player rolls a 1, they lose all the points accumulated during that turn, and their turn ends.
A player can choose to "hold" at any time during their turn, which means they add the accumulated points to their total score and end their turn.
The first player to reach or exceed 100 points wins the game.'''

import random

def roll_dice():
    return random.randint(1, 6)

player1_score = 0
player2_score = 0
turn = 1

while True:
    if player1_score >= 100:
        print(f'Congratulations Player 1, you won with {player1_score} points!')
        break
    elif player2_score >= 100:
        print(f'Congratulations Player 2, you won with {player2_score} points!')
        break

    if turn % 2 == 1:
        turn_score = 0
        print("Player 1's turn")
        while True:
            choice = input('Player 1, it is your turn. Do you want to roll/pass? ').strip().lower()
            options = ['roll', 'pass']

            if choice not in options:
                print('Please select a valid option: roll/pass')
                continue

            if choice == 'roll':
                number = roll_dice()
                print(f'You rolled a {number}')
                if number == 1:
                    print('Bad Luck, 1 was rolled. You lost all your turn score.')
                    turn += 1
                    break
                else:
                    turn_score += number
                    print(f'Your turn score is {turn_score}. If you pass, your total score will be {player1_score + turn_score}')
            elif choice == 'pass':
                player1_score += turn_score
                print(f'You end your turn with {player1_score} points.')
                turn += 1
                break


    else:
        turn_score = 0
        print("Player 2's turn")
        while True:
            choice = input('Player 2, it is your turn. Do you want to roll/pass? ').strip().lower()
            options = ['roll', 'pass']

            if choice not in options:
                print('Please select a valid option: roll/pass')
                continue

            if choice == 'roll':
                number = roll_dice()
                print(f'You rolled a {number}')
                if number == 1:
                    print('Bad Luck, 1 was rolled. You lost all your turn score.')
                    turn += 1
                    break
                else: 
                    turn_score += number
                    print(f'Your turn score is {turn_score}. If you pass, your total score will be {player2_score + turn_score}')
            elif choice == 'pass':
                player2_score += turn_score
                print(f'You end your turn with {player2_score} points.')
                turn += 1
                break

print('Game Over')
