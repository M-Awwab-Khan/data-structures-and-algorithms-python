from typing import List

def max_prod(arr: List[int]) -> int:
    prod = 1
    pairs = [1, 1]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            prod = max(prod, arr[i]*arr[j])
            pairs[1] = max(pairs[1], arr[j])
            if max(pairs[0], arr[i]) != pairs[1]:
                pairs[0] = max(pairs[0], arr[i])
    print(pairs)
    return prod


print(max_prod([1, 2, 3, 5, 61, 2, 3, 6 ,12, 64, 32, 21, 34, 2, 34, 12, 11]))