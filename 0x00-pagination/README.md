# Pagination Techniques in REST APIs

## Overview

This project demonstrates various pagination techniques for REST APIs using Python. It includes three primary types of pagination:

1. **Simple Pagination**: Using page numbers and page size parameters.
2. **Hypermedia Pagination**: Providing metadata to navigate through pages.
3. **Deletion-Resilient Pagination**: Handling dataset changes where rows might be deleted between queries.

## Project Structure

- `0-simple_helper_function.py`: Implements the `index_range` function to calculate pagination indices.
- `2-hypermedia_pagination.py`: Implements the `Server` class with methods for basic and hypermedia pagination.
- `3-hypermedia_del_pagination.py`: Extends the `Server` class to support deletion-resilient pagination.
- `Popular_Baby_Names.csv`: Sample dataset used for testing.

