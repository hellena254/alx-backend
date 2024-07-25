# Caching System

## Overview

Caching is a technique used in computing to temporarily store data that is frequently accessed or computationally expensive to retrieve. By keeping this data in a cache, systems can reduce access times, enhance performance, and minimize the load on primary data sources.

## What is Caching?

Caching involves storing copies of data in a special storage area (cache) so that future requests for that data can be served more quickly. This is particularly useful when dealing with data that is repeatedly requested or computational tasks that are resource-intensive. 

### Benefits of Caching

1. **Reduced Latency**: Caches help in serving data quickly, reducing the time it takes to access frequently requested information.
2. **Improved Performance**: By serving data from the cache, the performance of systems and applications is enhanced due to reduced wait times and less load on primary data sources.
3. **Decreased Load**: Caching reduces the number of direct requests to databases or servers, thus lowering their load and potentially reducing operational costs.

## Caching Strategies

This project includes different caching strategies, each with its own approach to managing cached data:

### FIFO (First-In-First-Out)

- **Description**: The oldest data (first-in) is removed first when the cache reaches its capacity.
- **Usage**: Simple and easy to implement. Suitable for cases where the age of data is a primary consideration.

### LRU (Least Recently Used)

- **Description**: The data that has not been used for the longest time is removed first when the cache is full.
- **Usage**: Useful when recent data is more likely to be needed again soon. Ensures that frequently accessed data stays in the cache.

### LFU (Least Frequently Used)

- **Description**: The data that is accessed the least frequently is removed first when the cache reaches its limit.
- **Usage**: Suitable for scenarios where the frequency of access is a key factor in determining which data should be retained.

## Implementation

The project includes implementations of the following caching strategies:

### FIFO Cache

- **File**: `fifo_caching.py`
- **Description**: Implements FIFO caching strategy, where the oldest items are removed first.

### LRU Cache

- **File**: `lru_caching.py`
- **Description**: Implements LRU caching strategy, where the least recently used items are removed first.

### BaseCaching Class

- **File**: `base_caching.py`
- **Description**: Provides a base class for all caching strategies with a dictionary to store data and method signatures for adding and retrieving data.

## Running the Code

1. **Make Files Executable**: Ensure all files are executable.
   ```bash
   chmod +x fifo_caching.py lru_caching.py base_caching.py

