#!/usr/bin/env python3
"""a type-annotated function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.
    """
    return sum(mxd_lst)
