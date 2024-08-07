# randomly generate math questions
# ask the user those questions
# do not let the user continue until gets the correct answer

# My version:

# Questions
math_questions_answers = {
    "What is 5 + 3?": 8,
    "What is 12 - 4?": 8,
    "What is 6 * 2?": 12,
    "What is 15 / 3?": 5,
    "What is 9 + 6?": 15
}


for question in math_questions_answers.keys():
     while True:
        user_answer = input(question + ': ')
        if int(user_answer) == math_questions_answers[question]:
            print('Correct!')
            break
        else:
            print('incorrect')
            




# Class Version

# eval evaluates an expression, if its a legal python statement, it will be executed

import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr) # this is going to evauluate the mathematical expression, doing the calculation and giving me the result 
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time() 

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time() 
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")