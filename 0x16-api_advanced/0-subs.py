#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
from sys import argv

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    results = r.json().get("data")
    return results.get("subscribers")
