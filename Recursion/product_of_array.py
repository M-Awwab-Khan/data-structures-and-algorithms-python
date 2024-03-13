def product_of_array(arr: list) -> int:
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    
    else:
        return arr[-1] * product_of_array(arr[0:-1])
    
print(product_of_array([1,2,3])) #6
print(product_of_array([1,2,3,10])) #60