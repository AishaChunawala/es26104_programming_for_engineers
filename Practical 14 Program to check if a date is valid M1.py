day, month, year = map(int, input().split())

if month < 1 or month > 12:
    print("Invalid date")

elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        max_days = 29
    else:
        max_days = 28

    if 1 <= day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")

elif month in [4, 6, 9, 11]:
    if 1 <= day <= 30:
        print("Valid date")
    else:
        print("Invalid date")

else:
    if 1 <= day <= 31:
        print("Valid date")
    else:
        print("Invalid date")