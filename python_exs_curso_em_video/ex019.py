from random import choice

name1 = input('Say the name of the first student:')
name2 = input('Say the name of the second student:')
name3 = input('Say the name of the third student:')
name4 = input('Say the name of the fourth student:')
list = [name1, name2, name3, name4]
print('The student {} was the selected one'.format(choice(list)))

