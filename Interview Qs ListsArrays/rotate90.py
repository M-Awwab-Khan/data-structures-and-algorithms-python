from typing import List

def rotate_matrix(mat: List[List[int]]) -> List[List[int]]:
    # transpose
    result = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat)):
            row.append(mat[j][i])

        result.append(row)

    # reverse each row
    for i in range(len(mat)):
        result[i].reverse()

    return result


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in rotate_matrix(arr): 
    print(row)
