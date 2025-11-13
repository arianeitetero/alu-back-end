#!/usr/bin/python3
"""
Exports all tasks of a given employee to a JSON file.
"""

import json
import requests
import sys


def main():
    """Fetch employee tasks and write to JSON file."""
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get('username')

    # Get tasks
    todos_response = requests.get("{}/todos".format(base_url),
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)
    todos = todos_response.json()

    # Prepare JSON data
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    json_data = {str(employee_id): tasks_list}

    # Write JSON file
    filename = "{}.json".format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    main()
