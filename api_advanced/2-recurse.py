#!/usr/bin/python3
"""Module that returns a list of all hot post titles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively gets all hot post titles, or None if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json().get("data")
        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))
    except Exception:
        return None
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
