#!/usr/bin/env python3
"""
Contains the definition of the get_page function
"""
import redis
import requests
from functools import wraps
from typing import Callable


def cached(func: Callable) -> Callable:
    """
    Decorator that caches the results of the function call
    """
    red = redis.Redis()

    @wraps(func)
    def wrapper(url):
        """
        cache results of func and keep track of how many times url is accessed
        """
        red.incr(f"count:{url}")
        content = red.get(f"{url}")
        if content:
            return content.decode("utf-8")
        content = func(url)
        red.setex(f"{url}", 10, content)
        return content
    return wrapper


@cached
def get_page(url: str) -> str:
    """
    Obtain the html content of a particular URL and return it.
    Track how many times a URL was accessed in the key 'count: {url}'
    Cache the result with an expiration time of 10 seconds
    Args:
        url (str): url to be accessed
    Return:
        html content from the accessed url
    """
    response = requests.get(url)
    return response.text
