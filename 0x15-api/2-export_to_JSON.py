#!/usr/bin/python3
"""
A REST API to fetch employee data and save it to a JSON file
"""
import json
import requests
import sys


if __name__ == "__main__":
    """Fetches employee data from an API and saves it to a JSON file"""
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    r = requests.get(url)
    name = r.json().get('name')
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    r = requests.get(url)
    tasks = r.json()
    task_list = []
    for task in tasks:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = name
        task_list.append(task_dict)
    json_dict = {}
    json_dict[user_id] = task_list
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
