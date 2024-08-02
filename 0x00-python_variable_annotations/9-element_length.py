#!/usr/bin/env python3
"""task 9 module"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """computes the len of a list of sequence"""
    return [(i, len(i)) for i in lst]
