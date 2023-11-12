import requests
import random

url = "https://www.icanhazdadjoke.com/search"
user_search = input("Let me tell you a joke! Give me a topic: ")
response = requests.get(url,
                        params={"term": user_search},
                        headers={"Accept": "application/json"})

res = response.json()
num_of_jokes = len(res["results"])

if num_of_jokes > 0:
    joke_list = res["results"]
    joke_ob = random.choice(joke_list)
    joke = joke_ob["joke"]

if num_of_jokes > 0:
    print(f"I've got {num_of_jokes} jokes about {user_search}.  Here's one: ")
    print(joke)
else:
    print(f"Sorry, I don't have any jokes about {user_search}! Please try again")
