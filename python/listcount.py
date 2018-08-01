# checks to see if elements from list_2 are in or missing from list_1 

from collections import Counter

list_1 = ['a', 'd', 'e']

list_2 = ['a', 'b', 'c', 'd', 'd']

list_3 = set(list_1) and set(list_2)


table_format = '{:<10} {:<10}'
print(table_format.format('list_1', 'list_2'))
print('-' * 20)
for elem in sorted(list_3):
    if elem in list_1:
        if elem in list_2:
            print(table_format.format(elem, elem))
        else:
            print(table_format.format(elem, 'Missing'))
    else:
        print(table_format.format('Missing', elem))