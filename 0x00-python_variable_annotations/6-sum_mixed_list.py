#!/usr/bin/env python3
"""
    function sum_mixed_list which takes a list mxd_lst of integers
    and floats and returns their sum as a float
"""
def sum_mixed_list(mxd_lst: List[float]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Args:
        mxd_lst: A list of integers and/or floats.

    Returns:
        The sum of the input list as a float.
    """
    return sum(mxd_lst)
