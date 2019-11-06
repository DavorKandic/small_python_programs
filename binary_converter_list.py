"""Converts binary number(base 2) that user enters to decimal(base 10).
It uses self-generated list of powers of two (up to 2**8). I first wrote this
code on SoloLearn app"""
# message for user
print('Enter a binary number: ') # up to eight bits or one byte
orig_bin = input()
to_8 = range(9) # will be used for creation of list
n = len(orig_bin)
rev_bin = orig_bin[::-1] # reverse the string which contains user binary number
pows_of_2 = [2**n for n in to_8] # create list via list comprehension
# list contains powers of two from 1 to 255(inclusive)
sum1 = 0 # name of var is not just 'sum' because it will override builtin func
for i in range(n):
    sum1 += (pows_of_2[i] * int(rev_bin[i]))
print(f'{orig_bin} equals {sum1} in decimal') # on SL I have used .format method
# because their code playground doesn't support f-strings.
