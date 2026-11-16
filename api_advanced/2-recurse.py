#!/usr/bin/python3
"""Module that returns a list of all hot post titles of a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively gets all hot post titles, or None if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    try:
        data = response.json().get("data")
        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))
    except Exception:
        return None
    after = data.get("after")
    count += data.get("dist")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after, count)
