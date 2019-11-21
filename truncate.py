"""Write a function called truncate that will shorten a string to a specified
length, and add '...' to the end. Given a string and a number n, truncate the
string to a shorter string containing at most n characters (including '...') So,
the smallest value of n should be 3. If n is less than 3 function truncate
should return 'Truncation must be at least 3 characters.' If n is greater than
number of characters in given string truncate should return that string"""




def truncate(txt, l):
    if l < 3:
        return 'Truncation must be at least 3 characters.'
    elif l > len(txt):
        return txt
    else:
        end = l - 3
        return txt[:end] + '...'
    


assert truncate("Super cool", 2) == "Truncation must be at least 3 characters."
assert truncate("Super cool", 1) == "Truncation must be at least 3 characters."
assert truncate("Super cool", 0) == "Truncation must be at least 3 characters."
assert truncate("Hello World", 6) == "Hel..."
assert truncate("Problem solving is the best!", 10) == "Problem..."
assert truncate("Another test", 12) == "Another t..."
assert truncate("Woah", 4) == "W..."
assert truncate("Woah", 3) == "..."
assert truncate("Yo",100) == "Yo"
assert truncate("Holy guacamole!", 152) == "Holy guacamole!"
print('All tests are OK!')
