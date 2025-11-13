#!/usr/bin/python3
"""
This module fetches and displays the TODO list progress of an employee
from the JSONPlaceholder REST API.
"""

import requests
import sys


def main():
    """Fetch employee info and TODO list, then display progress."""
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get TODO list for the employee
    todos_response = requests.get("{}/todos".format(base_url),
                                  params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)

    todos = todos_response.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed') is True]

    # Print the result in the exact format expected by ALX
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
