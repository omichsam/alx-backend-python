#!/usr/bin/env python3
""" module that contains a function for task 1
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for random delays and returns a sorted list of the delays.
    """
    result_delays = []
    result_tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        result_tasks.append(task)
    for task in result_tasks:
        delay = await task
        result_delays.append(delay)
    return sorted(result_delays)
