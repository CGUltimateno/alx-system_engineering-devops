from requests import get


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts for a given subreddit. """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    with get(url, allow_redirects=False) as res:
        if res.status_code == 200:
            try:
                data = res.json()
                for item in data["data"]["children"]:
                    print(item["data"]["title"])
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("None")
