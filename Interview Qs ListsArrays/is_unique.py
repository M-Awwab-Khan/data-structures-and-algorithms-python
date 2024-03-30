from typing import List

def is_unique(arr: List[int]) -> bool:
    return len(set(arr)) == len(arr)


arr = [1, 2, 3, 4, 5, 6]
print(is_unique(arr))