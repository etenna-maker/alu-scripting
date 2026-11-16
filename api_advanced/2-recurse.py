#!/usr/bin/python3
"""Module that returns a list of all hot post titles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recursively gets all hot post titles, or None if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after)
    headers = {"User-Agent": "alu-reddit-project"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    for post in data.get("children"):
        hot_list.append(post.get("data").get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
