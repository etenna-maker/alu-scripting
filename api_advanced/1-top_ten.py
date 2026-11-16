#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts, or None if invalid"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-reddit-project"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data").get("children")
    for post in posts:
        print(post.get("data").get("title"))
