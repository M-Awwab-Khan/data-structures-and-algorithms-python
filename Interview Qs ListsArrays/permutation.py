from typing import Any, List

def is_permutation(arr1: List[Any], arr2: List[Any]) -> bool:

    if len(arr1) != len(arr2):
        return False
    arr1.sort()
    arr2.sort()

    if arr1 == arr2:
        return True
    return False


print(is_permutation([1, 2, 3, 4, 5], [5, 3, 4, 1, 1, 2]))
print(is_permutation(['a', 'w', 'w', 'a', 'b'], ['w', 'a', 'w', 'b', 'a']))