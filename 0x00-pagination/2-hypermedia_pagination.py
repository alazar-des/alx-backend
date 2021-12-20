#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Union, Optional, Mapping


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
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
        """Get page
        """
        assert (type(page) is int and page > 0 and
                type(page_size) is int and page_size > 0)
        index = index_range(page, page_size)
        dataset = self.dataset()
        if index[1] > len(dataset):
            return []
        return dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        """Get hyper
        """
        hyper = dict()
        hyper['page_size'] = page_size
        hyper['page'] = page
        hyper['data'] = self.get_page(page, page_size)

        if len(self.__dataset) > page * page_size:
            hyper['next_page'] = page + 1
        else:
            hyper['next_page'] = None

        if page == 1:
            hyper['prev_page'] = None
        else:
            hyper['prev_page'] = page - 1

        hyper['total_pages'] = math.ceil(len(self.__dataset) / page_size)

        return hyper
