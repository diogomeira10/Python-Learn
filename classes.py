# Classes are a way of organizing your code

# Classes are designed to create reusable objects

# Convention for class name are CamelCase

# Example where classes would be useful are games, by creating multiple instances of a monster class. It would make it easier to keep track of each value of the monsters


class TestClass:
    # variables in a class are called attributes
    test_var = 'hello'
    another_var = [1,2,3]

    # functions in a class are called methods
    def test_function(self): # The self is a way of class to refer to itself, so we can access the instance variables. self must be the first parameter for all methods
        print(self.another_var)
        self.another_function('hello') # accessing another function of the instance using the self parameter

    def another_function(self,test_paramater):
        print(test_paramater)


test = TestClass()

print(test.test_var) # output is 'hello'
print(test.another_var) # output is [1,2,3]
test.another_var.append(4)
print(test.another_var) # output is [1,2,3,4]


# Another instance of the TestClass class

test2 = TestClass()
print(test2.test_var) # output is 'hello'
test2.test_function()

test2.another_function('Hello World') # output is Hello World


# Dunder Methods
# Dunder Methods are special methods of a class

# This methods are called automatically and you can pass arguments into them
# __init is run when anm instance of the class is created - 
#__len__ gets called when the instance of the class is passed into the len function


# Mage Class Example

class Mage():
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        print('Mage class created!')

    def attack(self,target):
        target.health -= 10

class Monster():
    health = 40

    def __init__(self):
        print('40 health Monster created!')



mage1 = Mage(100,123) # Mage class created!
monster = Monster()

print(monster.health) # 40
mage1.attack(monster)
print(monster.health) # 30





# Inheritance

# With inheritance one class can get the methods and attributes of another class

# A class can also inherit from multiple classes and you can have entire family trees

class Human:

    def __init__(self,health):
        self.health = health

    def attack(self):
        print('Attack!!')
    

class Warrior(Human): # Inheriting the Human class
    def __init__(self,health,defense):
        super().__init__(health) # Passing the health argument to the Human parent class. Super refers to the class that is inherited, in this case the Human class
        self.defense = defense


class Barbarian(Human): 
    def __init__(self,health,damage):
        super().__init__(health)
        self.damage = damage





warrior = Warrior(50,2)
barbarian = Barbarian(20,2)
warrior.attack()
barbarian.attack()

print(warrior.health)
