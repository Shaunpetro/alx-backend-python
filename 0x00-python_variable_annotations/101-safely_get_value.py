#!/usr/bin/env python3
"""module for task 101"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Retrieves a value from dict"""
    if key in dict:
        return dct[key]
    else:
        return default
