def gcd(a: int, b: int) -> int:
    assert type(a) == int and type(b) == int, "Integers only!"
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a

    return gcd(b, a % b)

print(gcd(-45.5, 210))