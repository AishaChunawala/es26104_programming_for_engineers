a, b, c = map(int, input("Enter three numbers separated by spaces: ").split())

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print(maximum)