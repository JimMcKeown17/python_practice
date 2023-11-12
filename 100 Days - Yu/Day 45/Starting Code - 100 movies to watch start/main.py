import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
site = response.text
# Write your code below this line 👇
soup = BeautifulSoup(site, "html.parser")
title_list = []
titles = soup.select("h3.title")

print(titles)
# for title in titles:
#     movie = title.getText()
#     title_list.append(movie)
#
# title_list.reverse()
#
# with open("top_movies.txt", "w") as file:
#     for movie in title_list:
#         file.writelines(f"{movie}\n")
#
# print(title_list)

