counter = 0

list = (1,2,3,4,5)
for number in list:
    if number == 2:
        print('the value is 2')
    if number != 2:
        print('the value is not 2')
    if number == 5:
        while counter < 6:
            print('last item')
            counter += 1