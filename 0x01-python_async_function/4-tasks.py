#!/usr/bin/env python3
"""
This module contains the task_wait_n function.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times in
    parallel using asyncio.
    """
    result_delays = []
    result_tasks = []

    for _ in range(n):
        result_tasks.append(task_wait_random(max_delay))

    for completed_task in asyncio.as_completed(result_tasks):
        delay = await completed_task
        result_delays.append(delay)

    return (result_delays)
