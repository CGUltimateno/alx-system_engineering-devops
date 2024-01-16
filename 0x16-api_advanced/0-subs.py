#!/usr/bin/python3
""""
    Queries the Reddit API and returns the number of subscribers
    """
from requests import get


def number_of_subscribers(subreddit):
    """"
        Returns the number of subscribers
        """
    subs = 0
    results = None

    with get(f"https://www.reddit.com/r/{subreddit}/top.json",
             allow_redirects=False) as response:
        if response.status_code == 200:
            res = response.json()
            subs = res["data"]["children"][0]["data"]["subreddit_subscribers"]

    return subs
