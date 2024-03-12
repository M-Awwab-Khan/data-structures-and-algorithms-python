def dec_to_bin(n: int) -> str:
    assert n >= 0 and type(n) == int, "Number can only be an positive integer"
    if n == 0:
        return 0

    return (n % 2) + 10 * dec_to_bin(n // 2)


print(dec_to_bin(-13))