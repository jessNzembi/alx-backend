#!/usr/bin/env python3
"""pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return for the given
    pagination parameters (page number and page size).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
