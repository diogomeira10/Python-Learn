# Lists, tuples, dictionaries & sets

List = ['bob',123,'Lisa',('another list')]

# Tuples are immutable, they can not be changed
Tuple = ('bob',123,'Lisa', ('another list', 'number2', 1))
print(Tuple)


# Every entry is unique
Set = {1,2,3,'test'}
print(Set)

# Key value pair instead of single entries
Dictionary = {'name':'Bob',123:'test','Lisa':(1,2,3)}


# Examples

a_tuple = (1,2,3,'a string')
a_list = [1,2,3,'a string',2]
a_set = {1,2,3,4}
print('This is a tuple',a_tuple)
print('This is a list',a_list)

a_list.append('appended item')
print(a_list)

list_set = set(a_list)
print('original list', a_list)
print('Listed set',list_set)
print('set transformed into list',list(list_set))

a_dictionary = {'key': 'value', 123: [1,2,3]}
a_dictionary['newKey'] = 1.5 # adding new entry
print('dictionary: ', a_dictionary)


# Indexing

user_list = ['Lisa','Bob','Alex','Anna','John']
print(user_list[0]) # first item
print(user_list[-1]) #last item
print(user_list[0:3:1]) # slicing indexes 

print(a_dictionary[123])


# Exercise
#Create a list = (1,2,3,4,5,6,7,8,9,10)
# Create a new list : 8,6,4,2

tuple_list = (1,2,3,4,5,6,7,8,9,10)
print('Filtered tuple:', tuple_list[1:-2:2])
print('Easier',tuple_list[7:1:-2])
print('Picking the lowest value as the end',tuple_list[7::-2])
print(list(sorted(tuple_list[1:-2:2], reverse=True)))