h1, m1, s1 = map(int, input("Enter the first time (hours minutes seconds): ").split())
h2, m2, s2 = map(int, input("Enter the second time (hours minutes seconds): ").split())

time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

difference = time2 - time1

print("Difference in seconds:", difference)