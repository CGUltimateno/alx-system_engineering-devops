#!/usr/bin/python3
""""
    Queries the Reddit API and returns the number of subscribers
    """
import requests
import response


def number_of_subscribers(subreddit):
    """"
        Returns the number of subscribers
        """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user = {"User-Agent": "CGUltimateno"}
    request = requests.get(url, headers=user, allow_redirects=False).json()
    if response.status_code == 404:
        return 0
    return request.get('data').get('subscribers')
