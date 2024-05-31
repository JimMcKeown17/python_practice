from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

name = soup.select(selector=".titleline")
score = soup.select(selector=".score")
# print(name)
names = [n.text for n in name]
scores = [int(s.text.split()[0]) for s in score]

high_score = max(scores)
index_hs = scores.index(496)

print(names[index_hs])

