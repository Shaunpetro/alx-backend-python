#!/usr/bin/env python3
"""modelu 7 task"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts a key & its value to a tuple"""
    return (k, float(v**2))
