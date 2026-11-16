#!/usr/bin/python3
"""Module that counts keywords in the hot post titles of a subreddit"""
import requests


def count_words(subreddit, word_list, after="", count=0, counts=None):
    """Recursively counts keywords and prints them sorted"""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "PostmanRuntime/7.35.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return
    try:
        data = response.json().get("data")
        for post in data.get("children"):
            title_words = post.get("data").get("title").lower().split()
            for word in title_words:
                if word in counts:
                    counts[word] += 1
    except Exception:
        return

    after = data.get("after")
    count += data.get("dist")
    if after is not None:
        count_words(subreddit, word_list, after, count, counts)
        return

    totals = {}
    for word in word_list:
        word = word.lower()
        if counts[word] > 0:
            totals[word] = totals.get(word, 0) + counts[word]

    sorted_words = sorted(totals.items(), key=lambda x: (-x[1], x[0]))
    for word, total in sorted_words:
        print("{}: {}".format(word, total))
