#!/usr/bin/python3
"""
A REST API to fetch todos and save it to a JSON file
"""
import json
import requests


if __name__ == "__main__":
    """Fetches todos from an API and saves it to a JSON file"""
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    users = r.json()
    json_dict = {}
    for user in users:
        user_id = user.get('id')
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        r = requests.get(url)
        tasks = r.json()
        task_list = []
        for task in tasks:
            task_dict = {}
            task_dict['task'] = task.get('title')
            task_dict['completed'] = task.get('completed')
            task_dict['username'] = user.get('username')
            task_list.append(task_dict)
        json_dict[user_id] = task_list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(json_dict, jsonfile)