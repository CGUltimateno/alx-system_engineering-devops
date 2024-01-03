#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    """Gather data from an API"""

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    r = requests.get(url)
    name = r.json().get('name')
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    r = requests.get(url)
    tasks = r.json()
    completed_tasks = []
    for task in tasks:
        if task.get('completed') is True:
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
