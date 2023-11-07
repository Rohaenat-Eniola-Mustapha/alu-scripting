#!/usr/bin/python3
"""
This is a pthon script that Writes a functionthat
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) 
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""


import json
import requests


"""
Define HTTP headers for the API requests
"""


def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'  # Fixed URL
    response = requests.get(url, headers={'User-agent': 'I am learning Apis'})

    if response.status_code == 200:
        content = response.json()
        result = {"title": content['data']['title'],
                  "subscribers": content['data']['subscribers']}
        print(result)
    elif response.status_code == 404:
        return 0
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


number_of_subscribers('python')
