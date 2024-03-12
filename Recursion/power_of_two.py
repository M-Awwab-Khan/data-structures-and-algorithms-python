def power_of_two(n: int) -> int:

    assert n >= 0 and type(n) == int, "n can only be positive integer."

    if n == 0:
        return 1
    else:
        return 2 * power_of_two(n - 1)
    
print(power_of_two(4))