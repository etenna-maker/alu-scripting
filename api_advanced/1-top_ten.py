#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts, or None if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404 or 300 <= response.status_code < 400:
        print("None")
        return

    try:
        posts = response.json().get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
    except Exception:
        print("None")
