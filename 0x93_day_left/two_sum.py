#!/usr/bin/env python3

def two_sum(nums, target):
    """use caching much faster but
    more memory
    """
    
    cache = {}

    for idx, value in enumerate(nums):
        complement = target - value

        if value not in cache:
            cache[complement] = idx
        else:
            return [cache[value], idx]
    return []

def two_sum_brutal(nums, target):
    """solve using brutal force
    """
    
    sum = 0;

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

    return []
