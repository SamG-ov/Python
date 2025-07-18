import requests
from datetime import datetime

TOKEN = "1A2B3C4D"
USERNAME = "samthe7"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#To create a user for the first time
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"\

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "11"
}

#Update an existing data
#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#To Delete an existing data
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)