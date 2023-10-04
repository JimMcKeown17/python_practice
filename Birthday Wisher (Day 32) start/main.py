import smtplib

my_email = 'qhawelamawele@gmail.com'
password = "lacf gooc gmsn waoq"


import datetime as dt
from random import choice

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()

date_of_birth = dt.datetime(year = 1982, month=3, day=24)
print(date_of_birth)

with open("quotes.txt") as file:
    quotes = file.readlines()

if day == 0:
    monday_quote = choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="mckeown.james@gmail.com",
                            msg=f"Subject: Monday Motivation\n\n{monday_quote}")
