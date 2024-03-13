def recursive_range(n: int) -> int:
    assert n >= 0 and type(n) == int, "Number can only be positive integer."
    if n in [0, 1]:
        return n
    else:
        return n + recursive_range(n - 1)
    
print(recursive_range(12))