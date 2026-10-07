N = int(input("Enter the value of N: "))

numbers = list(map(int, input("Enter the list of numbers: ").split()))

expected = N * (N + 1) // 2
actual = sum(numbers)

missing = expected - actual

print(missing)