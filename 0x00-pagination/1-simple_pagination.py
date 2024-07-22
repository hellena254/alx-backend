#!/usr/bin/env python3
"""
Simple Pagination
"""

import csv
import math
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int: int]:
    """
    Takes two integer arguments page and page_size
    Return a tuple of size two containing a start index and an end index
    Page numbers are 1-indexed
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
	Get a page from the dataset
	Args:
	    page(int): The current page
            page_size(int): The number of ittems per page
	Return: A list of rows from the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start_index:end_index]














