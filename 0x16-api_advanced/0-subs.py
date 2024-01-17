#!/usr/bin/python3
""""
    Queries the Reddit API and returns the number of subscribers
    """
from sys import argv
from requests import get


def number_of_subscribers(subreddit):
    """"
        Returns the number of subscribers
        """
    user = {"User-Agent": "Mozilla/5.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, headers=user, allow_redirects=False)
    try:
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
