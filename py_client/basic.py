import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"
#get_response= requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World"})
#get_response= requests.post(endpoint, json={"title": "Once More Hello World!!"}) # working one
get_response= requests.post(endpoint, json={"content": "Once More Hello World!!"})
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
# 3hr - 41 mins completed

print(get_response.json())

