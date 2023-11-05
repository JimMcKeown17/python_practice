from bs4 import BeautifulSoup
import lxml
import requests

import smtplib

my_email = 'qhawelamawele@gmail.com'
password = "lacf gooc gmsn waoq"

url = "https://www.amazon.com/Coding-Kids-Python-Awesome-Activities/dp/1641521759/ref=sr_1_6?crid=1G0PR6VPBK61T&keywords=coding+for+kids&qid=1699194293&sprefix=coding+for+kids%2Caps%2C79&sr=8-6"
url2 = "https://www.google.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=headers)
amazon_site = response.text

soup = BeautifulSoup(amazon_site, "lxml")
# price = soup.select("span .a-size-base a-color-price a-color-price")
price_full = soup.find(name="span", class_="a-offscreen").getText()
price = float(price_full.split("$")[1])
print(price)

price = 5
if price < 9.99:
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="mckeown.james@gmail.com",
                msg=f"Subject: Price Alert for Python Book {price}\n\n"
                    f"Check out how cheap the book is now at {url}"
            )
    except smtplib.SMTPException as e:
        print(f"An error occurred: {e}")