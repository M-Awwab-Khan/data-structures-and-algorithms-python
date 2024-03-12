def find_max_num_rec(sample_array: list, n: int) -> int: #O(1) + M(n-1) = M(n) Time complexity
    
    if n == 1:
        return sample_array[0]
    
    return max(sample_array[n-1], find_max_num_rec(sample_array, n-1))

def find_max_num_rec_alt(sample_array: list):

    if len(sample_array) == 1:
        return sample_array[0]
    
    return max(sample_array[-1], find_max_num_rec_alt(sample_array[:-1]))

x = [3, 12, 4, 34, 23]
print(find_max_num_rec(x, len(x)))
print(find_max_num_rec_alt(x))