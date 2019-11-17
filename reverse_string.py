"""CHALLENGE: Write a function called reverse_string which accepts a string
and returns a new string with all the characters reversed."""


# There many ways to implement reverse_ string(), but I think that this one
# is the most pythonic.
def reverse_string(normal):
    return normal[::-1]


assert reverse_string('awesome') == 'emosewa'
assert reverse_string('Colt') == 'tloC'
assert reverse_string('Elie') == 'eilE'
print('All tests passed!')
