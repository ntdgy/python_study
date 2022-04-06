def main():
    print('Please enter two numbers:')
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print('The sum of {} and {} is {}'.format(a, b, add(a, b)))

def add(a, b):
    return a + b


if __name__ == "__main__":
    main()


