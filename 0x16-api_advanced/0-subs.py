#!/usr/bin/python3
""""
    Queries the Reddit API and returns the number of subscribers
    """
from requests import get


def number_of_subscribers(subreddit):
    """"
        Returns the number of subscribers
        """
    subs = get("https://www.reddit.com/r/{}/about.json".format(subreddit),
               headers={"User-Agent": "Custom_user"},
               allow_redirects=False)
    if subs.status_code == 200:
        return subs.json().get("data").get("subscribers")
    else:
        return 0
