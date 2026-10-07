H = int(input("Enter the hour: "))
M = int(input("Enter the minute: "))
S = int(input("Enter the second: "))

angle = 30 * H + 0.5 * M + S / 120

print(angle) 