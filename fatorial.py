# Calculate the factorial of a given number

def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

print(factorial(8))