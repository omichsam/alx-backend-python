#!/usr/bin/env python3
""" a type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string 'k' and the square of 'v'.
    """
    return k, float(v ** 2)
