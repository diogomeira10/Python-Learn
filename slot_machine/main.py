# text base sloth machine

# the user is able to deposit an amount of money and to bet on the lines of the slot machine

# the user is going to continue to play, until he wants to cash out, or run out of money



#constant value
MAX_LINES = 3 # max value of lines

def spin():
    pass

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')

    return amount

def get_number_of_lines():
    while True:
        lines = input(f'What is the amount of lines to bet on (1-{MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES: # same as lines > 0 and lines < MAX_LINES
                break
            else:
                print('The number of lines should be in between 1-3')
        else:
            print('Please enter a number.')
    return lines



def main():
    balance = deposit()
    lines = get_number_of_lines()

    return balance, lines


print(main())

