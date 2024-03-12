def factorial(n: int) -> int:
    assert n >= 0 and int(n) == n, "Number can only be positive integer."
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)
    

print(factorial(9))