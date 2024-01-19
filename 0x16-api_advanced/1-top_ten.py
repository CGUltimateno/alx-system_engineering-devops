#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ Returns the top 10 hot posts for a given subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        print(None)
        return
    results = r.json().get("data").get("children")
    for post in results[:10]:
        print(post.get("data").get("title"))
