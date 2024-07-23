# generate a random number and count the number of times the user takes to get the number right

import random

trys = 0

top_of_range = input('Choose a top number: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(1,top_of_range)


while True:
    user_guess = input('Guess a number: ')
    print(random_number)
    if(random_number == int(user_guess)):
        break


print("You are right, congratulations!")

