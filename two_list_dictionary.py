"""Write a function called two_list_dictionary which accepts two lists of varying lengths. The first
list consists of keys and the second one consists of values. Your function should return a dictionary
created from the keys and values. If there are not enough values, the remaining keys should have a
value of None. If there not enough keys, just ignore the remaining values."""


def two_list_dictionary(keys, vals):
    dicty = {}
    lk = len(keys)
    lv = len(vals)
    if lk <= lv:
        i = 0
        while i < lk:
            dicty[keys[i]] = vals[i]
            i += 1
    elif lk > lv:
        i = 0
        while i < lv:
            dicty[keys[i]] = vals[i]
            i += 1
        while i < lk:
            dicty[keys[i]] = None
            i += 1       
    return dicty
            

test_keys = ['a','b','c']
test_vals = [1, 2, 3]

print(two_list_dictionary(test_keys, test_vals))

test_longer_keys = ['as','sd','df','fe']
test_shorter_vals = [10, 20]

print(two_list_dictionary(test_longer_keys, test_shorter_vals))

test_shorter_keys = ['abc', 'def']
test_longer_vals = [5,10,15,20,25,30]

print(two_list_dictionary(test_shorter_keys, test_longer_vals))

assert two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3, 'd': None}
assert two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) == {'a': 1, 'b': 2, 'c': 3}
assert two_list_dictionary(['x', 'y', 'z']  , [1,2]) == {'x': 1, 'y': 2, 'z': None}
print('All tests are OK!')
