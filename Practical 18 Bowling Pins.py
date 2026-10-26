N, K = map(int, input("Enter the number of pins and balls: ").split())

pins = ["I"] * N

for _ in range(K):
    L, R = map(int, input("Enter the range L and R: ").split())

    for i in range(L - 1, R):
        pins[i] = "."

print("".join(pins))