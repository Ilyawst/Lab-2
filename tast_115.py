a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if (a or b) > 999:
    print('Enter number in 1 - 1000!!!')
elif a > b:
    print(a)
else:
    print(b)
    