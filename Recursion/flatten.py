def flatten(arr):
    flattened = []
    for i in arr:
        if type(i) != list:
            flattened.append(i)
        else:
            flattened.extend(flatten(i))
    return flattened
        

print(flatten([1, 2, [3, [4, 5, [6, [[[7]]]]]]]))
print(flatten([[[[1], [[[[2], [3, 4]]]]]]]))