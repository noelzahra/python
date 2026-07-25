#USing the json module to read a JSON file
import json
import requests

url = "https://jsonplaceholder.typicode.com/users/1/todos/"

#loop trhough json data and print the title of each todo item
def todo_status(url:str):
    
    response = requests.get(url)
    print(response.status_code)

    response_json =json.loads(response.text)

    completed_list = []
    not_completed_list = []

    for todo in response_json:
        # for truthy values, we can use the 'if' statement to check if the 'completed' key is True
        # if not todo['completed']: for falsy values, we can use the 'if not' statement to check if the 'completed' key is False
        if todo['completed']:
            completed = f"Completed: {todo['title']}"
            completed_list.append(completed)

        else:
            not_completed = f"Not Completed: {todo['title']}"
            not_completed_list.append(not_completed)

    return completed_list, not_completed_list

if __name__ == "__main__" :
    print(f"what is value for __name__: {__name__} and what is value for __main__: {'__main__'}")
    completed_list, not_completed_list = todo_status(url=url)
    for todos in completed_list:
        print(todos)
    for todos in not_completed_list:
        print(todos)