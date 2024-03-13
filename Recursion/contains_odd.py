def contains_odd(arr: list, func: "function") -> bool:
    if len(arr) == 0:
        return False
    return func(arr[0]) or contains_odd(arr[1:], func)

def isodd(num: int) -> bool:
    return num % 2 != 0
    

print(contains_odd([1,2,3,4], isodd)) # true
print(contains_odd([4,6,8,9], isodd)) # true
print(contains_odd([4,6,8], isodd)) # false

