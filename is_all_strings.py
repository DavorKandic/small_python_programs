""" a function is_all strings that accepts a single iterable and returns True if
it contains only strings. Otherwise, it should return False. Use any/all."""

# using all
def is_all_strings(itr):
    return all([type(x) == str for x in itr])
    



assert is_all_strings(['a', 'b', 'c']) == True
assert is_all_strings([2, 'a', 'b', 'c']) == False
assert is_all_strings(['hello', 'goodbye']) == True
assert is_all_strings(['a', 'b', True]) == False
print('All tests are OK!')


# using any
def is_all_strings(itr):
    return not any([type(x) != str for x in itr])


assert is_all_strings(['a', 'b', 'c']) == True
assert is_all_strings([2, 'a', 'b', 'c']) == False
assert is_all_strings(['hello', 'goodbye']) == True
assert is_all_strings(['a', 'b', True]) == False
print('All tests are OK!')
