n = int(input('Enter 1 number: '))
m = int(input('Enter 2 number: '))
k = int(input('Enter 3 number: '))

if k <= n * m and (k % n == 0 or k % m == 0):
    print("Yes")
else:
    print("No")
    