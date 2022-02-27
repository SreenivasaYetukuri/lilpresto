from calendar import HTMLCalendar
from json import JSONDecodeError
import requests

#endpoint="https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

#get_response=requests.get(endpoint, json= {"query": "Hello World"}) ## API -> Method
#get_response=requests.get(endpoint, data= {"query": "Hello World"}) ## API -> Method
#get_response=requests.get(endpoint, json= {"Product_id": 123}) ## API -> Method
#get_response=requests.post(endpoint, json= {"Product_id": 123}) ## API -> Method
#get_response=requests.post(endpoint, json= {"title": "Hello World"}) ## API -> Method
get_response=requests.post(endpoint, json= {"title": "ABC123", "content": "Hello World", "price": "abc123"}) ## API -> Method


print(get_response.text)  # print raw text response

###HTTP requests -> HTML
####REST API HTTP Request -> JSON (XML)
## javascript object notataion ~ Python Dict
#print(get_response.json())
print(get_response.status_code)