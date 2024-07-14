# Classes are a way of organizing your code

# Classes are designed to create reusable objects

# Convention for class name are Camel Case

# Example where classes would be useful are games, by creating multiple instances of a monster class. It would make it easier to keep track of each value of the monsters


class TestClass:
    test_var = 'hello'
    another_var = [1,2,3]

    def test_function(self): # The self is a way of class to refer to itself, so we can access the instance variables.
        print(self.another_var)


test = TestClass()

print(test.test_var) # output is 'hello'
print(test.another_var) # output is [1,2,3]
test.another_var.append(4)
print(test.another_var) # output is [1,2,3,4]


# Another instance of the TestClass class

test2 = TestClass()
print(test2.test_var) #output is 'hello'
test2.test_function()


