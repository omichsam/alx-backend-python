#!/usr/bin/env python3
"""a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies
    a float by the given multiplier.
    """
    def multiplier_float(x: float) -> float:
        return x * multiplier

    return multiplier_float
