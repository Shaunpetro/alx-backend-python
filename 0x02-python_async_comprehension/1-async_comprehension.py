#!/usr/bin/env python3
'''module for task 1
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''creates a list of 10 random num from generator
    '''
    return [num async for num in async_generator()]
