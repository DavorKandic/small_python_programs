"""Print Fibonacci's numbers up N (user input)inclusive. Pure classic."""

def fibo(n):
    a, b = 0, 1
    for i in range(0, n+1):
        print(a)
        a, b = b, a+b


def main():
    while True:
        print('This program prints Fibonacci\'s sequence up to number of your choice:')
        user_input = input('Please enter an integer: ')
        if user_input == 'q':
            print('Thank you, come again!\nBye-bye!')
            break
        else:
            fibo(int(user_input))

if __name__ == '__main__':
    main()
