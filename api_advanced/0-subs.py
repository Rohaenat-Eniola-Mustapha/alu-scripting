#!/usr/bin/python3


"""
This is a pthon script that Writes a function
 that queries the Reddit API and returns the number
 of subscribers (not active users, total subscribers) 
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""


import requests

def number_of_subscribers(subreddit):
    # Reddit API URL to get the subreddit data
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {'User-Agent': 'Rohaenat'}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0  # Return 0 for an invalid subreddit
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0  # Return 0 in case of any exception

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers_count = number_of_subscribers(subreddit_name)
        if subscribers_count > 0:
            print(f"The '{subreddit_name}' subreddit has {subscribers_count} subscribers.")
        else:
            print(f"'{subreddit_name}' is not a valid subreddit.")
