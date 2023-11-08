#!/usr/bin/python3

"""
Reddit API Subreddit Subscriber Count

This module provides a function to query the Reddit API and retrieve the number of subscribers for a given subreddit.

Functions:
    number_of_subscribers(subreddit):
        Queries the Reddit API to fetch the number of subscribers for a specified subreddit.
        
        Args:
            subreddit (str): The name of the subreddit to retrieve subscriber count for.
            
        Returns:
            int: The number of subscribers for the specified subreddit, or 0 if the subreddit is invalid.

Usage:
    This module can be used both as a standalone script and as a part of a larger project.

    Standalone Usage:
    $ python3 0-main.py programming
    # Output: 756024
    
    $ python3 0-main.py this_is_a_fake_subreddit
    # Output: 0

Note:
    - This module sends an HTTP GET request to the Reddit API with a custom User-Agent header to avoid "Too Many Requests" errors.
    - It handles cases where the subreddit is invalid and returns 0 in such cases.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to fetch the number of subscribers for a specified subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve subscriber count for.
        
    Returns:
        int: The number of subscribers for the specified subreddit, or 0 if the subreddit is invalid.
    """
    # Reddit API endpoint for getting subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent header to avoid "Too Many Requests" error
    headers = {'User-Agent': 'MyBot/1.0'}
    
    # Send an HTTP GET request to the Reddit API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to get the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or there's an issue, return 0
        return 0

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        [print(subscribers)]
