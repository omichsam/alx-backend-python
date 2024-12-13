#!/usr/bin/env python3
""" a type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.
    """
    return sum(input_list)
