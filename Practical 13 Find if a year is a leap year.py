year = int(input("Enter a year to check if it's a leap year: "))

if year % 400 == 0:
    print("The entered year is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("The entered year is a leap year")
else:
    print("The entered year is not a leap year")