#!/usr/bin/env python3
"""
Simple Helper Function
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int: int]:
    """
    Takes two integer arguments page and page_size
    Return a tuple of size two containing a start index and an end index
    Page numbers are 1-indexed
    """
    start_index = page * page_size
    end_index = start_index - page_size
    return (end_index, start_index)
