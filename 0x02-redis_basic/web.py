#!/usr/bin/env python3
"""Implemnent a get page function"""
import requests
import redis

r = redis.Redis()
count_calls = 0


def get_page(url: str) -> str:
    """get page function"""
    r.set(f"cached:{url}", count_calls)
    r = requests.get(url)
    r.incr(f"count:{url}")
    r.setex(f"cached:{url}", 10, r.get(f"cached:{url}"))
    return r.text


if __name__ == "__main__":
    get_page("http://slowwly.robertomurray.co.uk")
