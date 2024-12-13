#!/usr/bin/env python3
'''Module for safe retrieval of the first
element from an iterable.
'''
from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.
    """
    if lst:
        return lst[0]
    else:
        return None
