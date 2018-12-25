print("______________CALCULATOR______________")

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('1. Addition      2. Difference: '))

if c == 1:
    d = a + b
    print("\nSum: ", d)
elif c == 2:
    d = a - b
    print("\nDifference: ", d)
else:
    print('Error')
