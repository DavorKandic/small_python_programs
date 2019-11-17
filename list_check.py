"""CHALLENGE: Write a function called list_check, which accepts a list
and returns True if each value in the list is a list. Otherwise the function
should return False."""

def list_check(lst):
    flag = True
    for el in lst:
        if type(el) != list:
            flag = False
    return flag


assert list_check([[],[1],[2,3], (1,2)]) == False
assert list_check([1, True, [],[1],[2,3]]) == False
assert list_check([[],[1],[2,3]]) == True
print('All tests OK!')
