# create a function

def print_x_times (word = 'loop', loop_amount = 5): # = backup value
    counter = 0
    while(counter != loop_amount ):
        print(word)
        counter += 1
    
    return loop_amount
        

print(print_x_times('x'))



