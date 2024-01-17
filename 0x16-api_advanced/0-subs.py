#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
from sys import argv

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    user = {"User-Agent": "CGU"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=user)
    if res.status_code == 200:
        return res.json()["data"]["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
