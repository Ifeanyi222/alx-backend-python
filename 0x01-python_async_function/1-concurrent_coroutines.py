#!/usr/bin/env python3
""" write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def time_measure(n: int, max_delay: int) -> float:

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
