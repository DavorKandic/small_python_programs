"""Write a function called remove_every_other that accepts a list and
returns a new list with every second value removed"""

# DANGER! Strange bug is detected if you use for loop! Check the code below.
##def remove_every_other(lst):
##    return [el for el in lst if lst.index(el) % 2 == 0]

##def show_indices(lst):
##    for el in lst:
##        print(f'Index of {el} is: {lst.index(el)}')
##    print('-' * 30)
##    print()
##
##show_indices([1,2,3,4,5])
##show_indices([5,1,2,4,1])

def remove_every_other(lst):
    lst_1 = []
    i = 0
    while i < len(lst):
        if i % 2 == 0:
            lst_1.append(lst[i])
        i += 1
    return lst_1

print(remove_every_other([1,2,3,4,5]))
assert remove_every_other([1,2,3,4,5]) == [1,3,5]
print(remove_every_other([5,1,2,4,1]))
assert remove_every_other([5,1,2,4,1]) == [5,2,1]
assert remove_every_other([1]) == [1]
print('All tests OK!')
