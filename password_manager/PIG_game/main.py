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
    random_number = random.randint(1, 6) 
    return random_number

player1_score = 0
player2_score = 0
round = 1

while True:
    if round % 2 == 1:
        while True:
            choice = input('Player 1, is your time to play.Do you want to roll/pass?')
            if choice == 'roll':
                number = roll_dice()
                player1_score += number
                if(number == 1):
                    print('Bad Luck, 1 was rolled. You lost all your score.')
                    round += 1
                    break
                else:
                    print(f'You rolled {number}, your total score is {player1_score}') 
                    continue
            if choice == 'pass':
               round += 1
            break
    
    if round % 2 == 0:
        while True:
            choice = input('Player 2, is your time to play.Do you want to roll/pass?')
            if choice == 'roll':
                number = roll_dice()
                player1_score += number
                print(f'You rolled {number}, your total score is {player1_score}') 
                continue
            if choice == 'pass':
               round += 1
            break
        continue
    break

