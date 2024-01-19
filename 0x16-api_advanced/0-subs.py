#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "CGUltimateno"
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    results = r.json().get("data")
    return results.get("subscribers")
