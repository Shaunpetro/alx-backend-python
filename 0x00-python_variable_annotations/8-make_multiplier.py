#!/usr/bin/env python3
"""task 8 module"""
from typing import Callable


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """creates a ,ultiplier function"""
    return lambda x: x * multiplier
