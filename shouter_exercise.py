def shouter (string = 'default string',number = 5):
    counter = 1

    if number > 10:
        print('you are too loud')
    else:
        while counter <= number:
            print(string.upper())
            counter += 1
    
    return 'done'

    
# Para que e que isto é util !?

shouter('ola')