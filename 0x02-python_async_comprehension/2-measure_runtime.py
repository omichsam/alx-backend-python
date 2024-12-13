#!/usr/bin/env python3
"""
This module measures the runtime of
the async_comprehension coroutine.
"""
import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension coroutine.
    """
    start_timestamp = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_timestamp = time.time()
    total_runtime = end_timestamp - start_timestamp

    return total_runtime
