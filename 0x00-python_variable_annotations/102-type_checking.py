#!/usr/bin/env python3
'''function for zooming in on arrays
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on each element in the tuple by
    repeating it 'factor' times.

    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
