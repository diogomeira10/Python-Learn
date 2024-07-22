print('Welcome to the quiz!')

playing = input('Do you wanna play? ')
if playing.lower() != 'yes':
    quit() # ends the execution of a Python program

print('Lets Play!')

score = 0
total_questions = 4

user_answer = input('What does CPU stand for? ')
correct_answer = 'central processing unit'
if user_answer.lower() == correct_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect Answer')


user_answer = input('What does HTTP stand for? ')
correct_answer = 'hyperText transfer protocol'
if user_answer.lower() == correct_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect Answer')


user_answer = input('What does the acronym "Wi-Fi" stand for? ')
correct_answer = 'wireless fidelity'
if user_answer.lower() == correct_answer:
    print('Correct!')
    score += 1
else:
    print('Incorrect Answer')


print(f'You got {score/total_questions * 100}%.')