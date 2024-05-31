import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
site = response.text

soup = BeautifulSoup(site, "html.parser")

titles = soup.select(selector=".gallery .title")
top100 = [title.getText()+ "\n" for title in titles]

top100_ordered = top100[::-1]

with open("top100.text", "w") as file:
    file.writelines(top100_ordered)