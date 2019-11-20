"""Write a function called includes which accepts a collection, a value, and
an optional starting index. The function should return True if the value exists
in the collection when we search starting from the starting index. Otherwise, it
should return False. The collection can be a string, a list or a dictionary. If
the collection is a string or array, the third parameter is a starting index
for where to search from. If the collection is a dictionary, the function
searches for the value among values in the dictionary; since objects have no
sort order, th third parameter is ignored."""


def includes(col, tgt, start=None):
    if type(col) == dict:
        return (tgt in col.values())
    else:
        return (tgt in col[start:])



assert includes([1, 2, 3], 1) == True 
assert includes([1, 2, 3], 1, 2) == False 
assert includes({ 'a': 1, 'b': 2 }, 1) == True 
assert includes({ 'a': 1, 'b': 2 }, 'a') == False
assert includes('abcd', 'b') == True
assert includes('abcd', 'e') == False
print('All tests passed!')
