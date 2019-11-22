def calculate(**kwargs):
    ops = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    key = kwargs['operation'] 
    exp = str(kwargs['first']) + ops[key] + str(kwargs['second'])
    res = eval(exp)
    if kwargs['make_float']:
        res = float(res)
    else:
        res = int(res)
    if 'message' in kwargs.keys():
        return kwargs['message']+' '+str(res)
    return 'The result is'+' '+str(res)


assert calculate(make_float=False, operation='add', message='You just added', first=2, second=4) == "You just added 6"
assert calculate(make_float=True, operation='divide', first=3.5, second=5) == "The result is 0.7"
print('All tests are OK!')
