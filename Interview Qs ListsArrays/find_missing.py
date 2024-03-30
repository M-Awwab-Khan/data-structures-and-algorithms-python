arr = [i for i in range(1, 101) if i != 73]

def find_missing(arr):
    s1 = sum(arr)
    s2 = int((100/2) * (100 + 1))

    print(abs(s1 - s2))


find_missing(arr)