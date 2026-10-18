
max_length = 0
current_length = 0
previous = None

while True:
    n = int(input())

    if n == 0:
        break

    if n == previous:
        current_length += 1
    else:
        current_length = 1

    if current_length > max_length:
        max_length = current_length

    previous = n

print(max_length)
