a = float(input('Enter first number: '))
b = float(input('Enter first number: '))
op = input('Select {- + / * pow mod div}: ')

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == 'pow':
    print(a ** b)
elif op in ('/', 'mod', 'div') and b == 0:
    print("Division by 0!")
elif op == '/':
    print(a / b)
elif op == 'mod':
    print(a % b)
elif op == 'div':
    print(a // b)
    