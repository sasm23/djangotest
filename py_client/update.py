import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/9/update/"

data = {
    "title": "Hello Bengaluru",
    "price": 129.99
}
get_response= requests.put(endpoint, json=data)


print(get_response.json())

