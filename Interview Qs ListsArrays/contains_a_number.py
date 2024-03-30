import numpy as np
from typing import List

def contains(target: int, arr: List[int]) -> bool:
    return target in arr

print(contains(9, np.array([1, 2, 3, 4, 5, 6, 7, 7])))


def linear_search(target: int, arr: List[int]) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(9, np.array([1, 2, 3, 4, 5, 6, 7, 7])))