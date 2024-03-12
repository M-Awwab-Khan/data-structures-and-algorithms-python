def find_nth_power(x: int, n: int) -> int:
    assert n >= 0 and type(n) == int, "Power can only be positive integer."

    if n == 0:
        return 1
    
    return x * find_nth_power(x, n - 1)

print(find_nth_power(3, 4))