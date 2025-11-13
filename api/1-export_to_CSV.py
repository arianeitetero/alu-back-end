#!/usr/bin/python3
"""
Exports all tasks of a given employee to a CSV file.
"""

import csv
import requests
import sys


def main():
    """Fetch employee tasks and write to CSV file."""
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

    # Write CSV
    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                             username,
                             task.get('completed'),
                             task.get('title')])


if __name__ == "__main__":
    main()
