import requests

# This was just an example of how you can get HTML code back from any website
# url = "https://news.ycombinator.com"
# res = requests.get(url)
# print(res.text)

# Here's an example of a nice API that let's you receive plain text back (rather than all the HTML)
# Below we use headers to get back the plain text only.
# url = "https://www.icanhazdadjoke.com"
# response = requests.get(url, headers ={"Accept": "text/plain"})
#
# print(response.text)

# JSON example upcoming
url = "https://www.icanhazdadjoke.com/search"
response = requests.get(url,
                        headers ={"Accept": "application/json"},
                        params={"term": "frog"}
)
data = response.json()
print(data["results"][0]["joke"])

