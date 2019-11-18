"""What does this code produce?"""


def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    return(l) 

#   Questions:
#   f(2)?
#   f(3,[3,2,1])?
#   f(3)?
print(f(2))
print(f(3))
assert f(2) == [0, 1]
assert f(3,[3,2,1]) == [3,2,1,0,1,4]
assert f(3) == [0,1,4]
print('All tests are OK!')
