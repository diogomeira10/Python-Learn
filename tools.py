# f strings

user_name = 'Bob'
user_age = '10'
user_information = f'{user_name} is {user_age} years old'

print(user_information)


# Single line if statements

user_age = 20
user_status = 'an adult' if user_age >= 18 else 'a child'

print(f'{user_name} is {user_age} years old and it is {user_status}.')

# list comprehension

    # instead of doing this 
    # for i in range(0,11,1):
    #     simple_list.append(i)

# we can do this instead:
# simple_list = [f'{j}{i}' for i in range(0,10,1) for j in ('a','b','c') if j == 'a']

# print(simple_list)

#lambda functions

# instead of doing this:
# def double_value (number):
#     return number * 2

double_value = lambda num: num * 2

print(double_value(9))

# some functions want a function as an argument
random_list = [('Diogo',32),('Mafalda',29)]
sorted_list = sorted(random_list, key = lambda user: user[1] )

print(sorted_list)

