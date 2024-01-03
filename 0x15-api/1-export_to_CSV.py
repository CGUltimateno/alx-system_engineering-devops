#!/usr/bin/python3
"""
A REST API to fetch employee data and save it to a CSV file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    """Fetches employee data from an API and saves it to a CSV file"""
    user_id = sys.argv[1]
    user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                .format(user_id))
    todos_url = ('https://jsonplaceholder.typicode.com/users/{}/todos'
                 .format(user_id))

    user = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()
    with open('{}.csv'.format(user_id), 'w', ) as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        data = [[user_id, user.get('username'), task.get('completed'),
                 task.get('title')] for task in tasks]
        csv_writer.writerows(data)
