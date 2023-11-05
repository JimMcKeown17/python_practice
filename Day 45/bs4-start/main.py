from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# article_tag = soup.select(".titleline")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


# high = max(article_upvotes)
# high_index = article_upvotes.index(high)

high = 0
for index, vote in enumerate(article_upvotes):
    if vote > high:
        high_index = index

print(high_index)
print(article_texts[high_index])


