#!/usr/bin/python3
"""Module that returns the number of subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers, or 0 if the subreddit is invalid"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        return response.json().get("data").get("subscribers")
    except Exception:
        return 0
