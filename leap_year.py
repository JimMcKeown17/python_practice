year = int(input("Give me a year: "))

if year % 400 == 0:
    if year % 100 == 0:
        if year % 4 == 0:
            print("It's a leap year")
else:
    print("Not a leap year")

