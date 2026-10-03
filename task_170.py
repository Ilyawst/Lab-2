n = input('Enter number: ')

if int(n) > 999:
    print('Enter number in 1 - 999!!')
else:
    if n[0] == n[1] == n[2]:
        print('3')
    elif (n[0] == n[1]) or (n[1] == n[2]) or (n[0] == n[2]):
        print('2')
    else:
        print('0')
        