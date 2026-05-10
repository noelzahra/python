#USing the json module to read a JSON file
import json
import requests

url = 'https://jsonplaceholder.typicode.com/users/1/todos/'
response = requests.get(url)
print(response.status_code)

response_json =json.loads(response.text)

#loop trhough json data and print the title of each todo item
for todo in response_json:
    if todo['completed'] == True:
        print(todo['title'])