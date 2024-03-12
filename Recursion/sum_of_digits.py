def sum_of_digits(n: int) -> int:
    # Unintentional Case
    assert n >= 0 and type(n) == int, "Number can only be positive integer."

    # Base Case
    if n // 10 == 0:
        return n
    
    # Recursive Case
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(4321))