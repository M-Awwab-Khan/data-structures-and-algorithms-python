from typing import List

def find_pairs(target: int, arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            if arr[i] + arr[j] == target:
                print((i, j))


find_pairs(6, [3, 4, 2, 1, 5, 0])