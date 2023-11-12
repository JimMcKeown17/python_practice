age = input("How old are you: ")
age = int(age)

years_left = 90 - age
months_left = years_left * 52
days_left = years_left * 365

print(f"You have {years_left} years left, {months_left} weeks left, and {days_left} days left")