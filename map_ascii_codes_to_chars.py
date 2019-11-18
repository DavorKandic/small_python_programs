"""Map the ASCII codes to relevant characters via dictionary in which ASCII code
is key and its character is a value. Do this for uppercase letters only."""

i = 65
alphabet =''
while i < 91:
    alphabet += chr(i)
    i += 1
answer = {ord(k):k for k in alphabet}

print(answer)

# And now, (of course ;)) one-liner dict comprehension!
ans = {code:chr(code) for code in range(65,91)}

print('*' * 80)
print(ans)
