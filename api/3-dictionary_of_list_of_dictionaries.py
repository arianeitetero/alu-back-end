#!/usr/bin/python3
"""
Exports all tasks from all employees to a JSON file.
"""

import json
import requests


def main():
    """Fetch all employees' tasks and write to JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get("{}/users".format(base_url))
    if users_response.status_code != 200:
        return
    users = users_response.json()

    # Prepare data dictionary
    all_data = {}

    for user in users:
        user_id = str(user.get('id'))
        username = user.get('username')

        # Get tasks for this user
        todos_response = requests.get("{}/todos".format(base_url),
                                      params={"userId": user_id})
        if todos_response.status_code != 200:
            continue
        todos = todos_response.json()

        # List of dictionaries per user
        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        all_data[user_id] = user_tasks

    # Write JSON file
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    main()
