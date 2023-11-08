#!/usr/bin/python3

"""
Reddit API Top Ten Hot Posts

This module provides a function to query the Reddit API and print the titles of the first 10 hot posts listed for a given subreddit.

Functions:
    top_ten(subreddit):
        Queries the Reddit API to fetch the titles of the first 10 hot posts for a specified subreddit and prints them.
        
        Args:
            subreddit (str): The name of the subreddit to retrieve hot posts from.

        Returns:
            None: Prints the titles of the top 10 hot posts, or None if the subreddit is invalid.

Usage:
    This module can be used both as a standalone script and as a part of a larger project.

    Standalone Usage:
    $ python3 1-main.py programming
    # Output: Titles of the first 10 hot posts in the 'programming' subreddit
    
    $ python3 1-main.py this_is_a_fake_subreddit
    # Output: None

Note:
    - This module sends an HTTP GET request to the Reddit API with a custom User-Agent header to avoid "Too Many Requests" errors.
    - It handles cases where the subreddit is invalid and prints None.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to fetch the titles of the first 10 hot posts for a specified subreddit and prints them.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot posts from.

    Returns:
        None: Prints the titles of the top 10 hot posts, or None if the subreddit is invalid.
    """
    # Reddit API endpoint for getting the hot posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent header to avoid "Too Many Requests" error
    headers = {'User-Agent': 'MyBot/1.0'}
    
    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the titles of the first 10 hot posts
        data = response.json()
        posts = data['data']['children']
        
        for i, post in enumerate(posts[:10]):
            title = post['data']['title']
            print(title)
    else:
        # If the subreddit is invalid or there's an issue, print None
        print(None)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
