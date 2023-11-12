import datetime as dt
import pandas as pd
from random import randint, choice
import smtplib
my_email = 'qhawelamawele@gmail.com'
password = "lacf gooc gmsn waoq"
df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day

letters = ['letter_1.txt', 'letter_2.txt']

for index,row in df.iterrows():
    if row['month'] == month and row['day'] == day:
        letter_template = choice(letters)
        name = row['name']
        with open(letter_template) as file:
            letter = file.read()
            letter = letter.replace('[NAME]', name)
            print(letter)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="mckeown.james@gmail.com",
                                msg=f"Subject: Happy Birthday\n\n{letter}")