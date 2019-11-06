"""Reverses user-entered string using  python generators"""
def rev_str(string):
    l = len(string)
    for i in range(l-1, -1, -1):
        yield string[i]


if __name__ == '__main__':
    print('Enter some text: ')
    usr_inp = input()
    for i in rev_str(usr_inp):
        print(i, end='')
