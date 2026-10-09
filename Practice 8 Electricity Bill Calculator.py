units = int(input("Enter the number of units consumed: "))
rate = float(input("Enter the rate per unit: "))

bill = units * rate

blocks = units // 100

remaining = units % 100

print("Bill =", bill)

print("100-unit blocks", blocks)

print("Remaining units =", remaining)