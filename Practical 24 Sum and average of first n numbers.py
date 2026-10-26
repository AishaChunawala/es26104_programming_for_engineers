
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

average = total / n

print("Sum =", total)
print("Average =", average)
