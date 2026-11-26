#!/usr/bin/python3
"""
Module for calculating retained rainwater between walls.
"""


def rain(walls):
    """
    Calculate how many square units of water are retained after it rains.

    Args:
        walls (list): non-negative integers representing wall heights,
                      each of unit width 1.

    Returns:
        int: total units of rainwater retained.
    """
    if not walls or len(walls) < 3:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                water += right_max - walls[right]
            right -= 1

    return water
