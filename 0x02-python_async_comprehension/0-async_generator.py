#!/usr/bin/env python3
'''MOdule for task 1
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''generates a random sequence of 10 num
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
