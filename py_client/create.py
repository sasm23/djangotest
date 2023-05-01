import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"

data = {"title": "This field is mandatory testin for mixin"}
get_response= requests.post(endpoint, json= data)


print(get_response.json())

