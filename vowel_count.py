"""CHALLENGE: Write a function called vowel_count that accepts a string and
returns a dictionary with the keys as the vowels and values as the count of
times that vowel appears in the string"""


def vowel_count(word):
    word = word.lower()
    vows = 'aeiou'
    dicty = {}
    i = 0
    for vow in vows:
        if vow in word:
            if vow not in dicty:
                dicty[vow] = word.count(vow)
    return dicty





assert vowel_count('awesome') == {'a': 1, 'e': 2, 'o': 1}
assert vowel_count('Elie') == {'e': 2, 'i': 1}
assert vowel_count('Colt') == {'o': 1}
print('All tests OK!')
