# Using the requests + json modules to read a JSON API response
import requests

url = "https://jsonplaceholder.typicode.com/users/1/todos/"


def todo_status(url: str) -> tuple[list[str], list[str]]:
    """Split todos into completed and not-completed title lists."""
    response = requests.get(url)
    print(response.status_code)

    todos = response.json()

    completed_list = [f"Completed: {todo['title']}" for todo in todos if todo['completed']]
    not_completed_list = [f"Not Completed: {todo['title']}" for todo in todos if not todo['completed']]

    return completed_list, not_completed_list


if __name__ == "__main__":
    completed_list, not_completed_list = todo_status(url=url)
    for todo in completed_list + not_completed_list:
        print(todo)
