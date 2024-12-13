#!/usr/bin/env python3
"""
This module defines a coroutine called async_generator.
The coroutine loops 10 times, each time asynchronously
waits for 1 second,
then yields a random number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that generates random numbers asynchronously.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
