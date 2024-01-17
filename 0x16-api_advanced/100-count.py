#!/usr/bin/python3
"""
Queries the Reddit APII
"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """ Prints a sorted count of given keywords """
    if after is None:
        for word in word_list:
            found_list.append([word, 0])
    with requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                      format(subreddit, after),
                      headers={"User-Agent": "Custom_user"},
                      allow_redirects=False) as res:
        if res.status_code == 200:
            for item in res.json()["data"]["children"]:
                for word in word_list:
                    found_list = count_words(subreddit, word_list, found_list,
                                             item["data"]["title"])
        else:
            return None
    if after is None:
        found_list = sorted(found_list, key=lambda x: (-x[1], x[0]))
        for item in found_list:
            if item[1] > 0:
                print("{}: {}".format(item[0], item[1]))
    return found_list
