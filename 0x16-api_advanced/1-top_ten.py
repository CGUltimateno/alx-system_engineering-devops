#!/usr/bin/python3
""" Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
"""
from requests import get


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts for a given subreddit. """
    top = get("https://www.reddit.com/r/{}/hot.json?limit=10"
              .format(subreddit),
              headers={"User-Agent": "Custom_user"},
              allow_redirects=False)
    if top.status_code == 200:
        for post in top.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print("None")
