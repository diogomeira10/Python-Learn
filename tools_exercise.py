#Exercise

list = [f'{j}{i}' for j in('A','B','C','D','E') for i in range(1,6,1) if f'{j}{i}' != 'C3']
print(list)