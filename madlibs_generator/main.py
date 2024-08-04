# slicing and replace


with open("story.txt",'r') as story:
    story = story.read()

words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1] # string slicing using  ':' , this gives us the entire word to be replaced, for example <place>
        words.add(word)
        start_of_word = -1

for word in words:
    print(word)
    option = input(f'What is the word you want for {word}: ')
    story = story.replace(word, option)


print(story)
# print(list(enumerate(story.split()))) # creates a list of a enumerated object of each word present in the story, example: [(0, 'In'), (1, 'the'), (2, '<adjective1>'), (3, 'land'), (4, 'of'), ... ]