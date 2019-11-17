"""CHALLENGE: Write a function called titleize which accepts a string of words
and returns a new string with the first letter of every word in the string
capitalized."""


def titleize(words):
    # string.title() also makes letters that come after first into lowercase! 
    ##return words.title()
    lst = words.split()
    n_lst = []
    for el in lst:
        # capitalize() also makes non-first chars in lowercase
        #n_lst.append(el.capitalize())
        first = el[0].upper()
        rest = el[1:]
        whole = first + rest
        n_lst.append(whole)
    return ' '.join(n_lst)



print(titleize('this is awesome'))
assert titleize('this is awesome') == "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt'))
assert titleize('oNLy cAPITALIZe fIRSt') == "ONLy CAPITALIZe FIRSt"
print('All tests are OK!')
