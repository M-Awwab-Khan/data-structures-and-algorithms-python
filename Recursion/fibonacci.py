def fibonacci(n: int) -> int:
    assert n >= 0 and int(n) == n, "Index can only be positive integer."
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(6))