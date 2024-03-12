def recursive_minus_one(n: int) -> None:
    assert type(n) == int, "n can only be of integer type."
    if n < 1:
        print("n is less than one.")

    else:
        print(n)
        recursive_minus_one(n - 1)

recursive_minus_one(4)