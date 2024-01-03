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
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    r = requests.get(url)
    name = r.json().get('name')
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    r = requests.get(url)
    tasks = r.json()
    with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, name, task.get('completed'),
                            task.get('title')])
