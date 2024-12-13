#!/usr/bin/env python3
'''function for safely retrieving a value from a dictionary.
'''
from typing import Mapping, Any, TypeVar, Union
T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    Safely retrieves a value from a dictionary.
      """
    if key in dct:
        return dct[key]
    else:
        return default
