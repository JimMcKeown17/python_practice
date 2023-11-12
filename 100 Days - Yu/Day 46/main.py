import requests
from bs4 import BeautifulSoup

year = input("What year would you like to travel to (YYYY-MM-DD): ")
URL_start = "https://www.billboard.com/charts/hot-100/"
url = f"{URL_start}/{year}"

response = requests.get(url)
site = response.text
soup = BeautifulSoup(site, "html.parser")

song_list = []
songs = soup.select("li ul li h3")
for song in songs:
    song_title = song.getText().strip()
    song_list.append(song_title)

print(song_list)
