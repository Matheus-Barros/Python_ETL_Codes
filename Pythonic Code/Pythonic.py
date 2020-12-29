import this

'''
@Author: Matheus Barros
Date: 28/12/2020

'''
print('\n----------------------\n')
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

#========== Print the list created by looping over the contents of names ==========
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print('Non-Pythonic code:',better_list)


#========== Print the list created by using list comprehension ==========
best_list = [name for name in names if len(name) >= 6]
print('\nPythonic code:',best_list)