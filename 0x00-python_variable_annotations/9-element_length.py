#!/usr/bin/env python3
""" Module for computing the length of sequences
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.
    """
    return [(j, len(j)) for j in lst]
