#Http post request
# request.get() get data
# request.post() create data
# request.put() update data
# request.delete() delete data
import requests
from datetime import datetime

pixela_url = "https://pixe.la/v1/users"
username = "davidmatthew"
Token = "jhd923dkjhad8381bjkbfdd"
idgraph = "runningc1"

user_information = {
    "token": Token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_url, json=user_information)
print(response.text)
graph = f"{pixela_url}/{username}/graphs"
user_graph_infomation = {
    "id": idgraph,
    "name":"Running days",
    "unit":"km",
    "type":"float",
    "color":"momiji",
}

header = {
    "X-USER-TOKEN": Token
}

response_graph = requests.post(url=graph,json=user_graph_infomation, headers=header)
print(response_graph.text)

date_now = datetime(year=2024,month=7,day=6)
# print(date_now.strftime("%Y%m%d"))
strftime = date_now.strftime("%Y%m%d")
value = {
    "date": date_now.strftime("%Y%m%d"),
    "quantity": "9",
}
graph_post_value = f"{pixela_url}/{username}/graphs/{idgraph}"

# response_value = requests.post(url=graph_post_value, json=value, headers=header)
# print(response_value.text)

value_update = {
    "quantity": "150",
}

graph_put_value = f"{pixela_url}/{username}/graphs/{idgraph}/{strftime}"
response_update_value = requests.put(url=graph_put_value,json=value_update,headers=header)
print(response_update_value.text)

graph_delete_value = f"{pixela_url}/{username}/graphs/{idgraph}/{strftime}"
response_delete_value = requests.delete(url=graph_put_value,json=value_update,headers=header)
print(response_delete_value.text)