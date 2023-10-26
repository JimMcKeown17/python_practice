import requests
from datetime import datetime

TOKEN = "jklwlk2hlke"
USERNAME = "dlamini402"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jklwlk2hlke",
    "username": "dlamini402",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config= {
    "id": "graph1",
    "name": "Habit Graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",

}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "2",
}



response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
print(response.text)