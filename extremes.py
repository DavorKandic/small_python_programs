"""Write a function called extremes which accepts an iterable. It should return
a tuple containing the minimum and maximum elements."""


def extremes(itr):
    return (min(itr), max(itr))


assert extremes([1,2,3,4,5]) == (1,5)
assert extremes([99,25,30,-7]) == (-7,99)
assert extremes('alcatraz') == ('a','z')
print('All tests passed!')
