def ispalidrome(x: str) -> bool:
    if len(x) == 1:
        return True
    if x[0] == x[-1]:
        return ispalidrome(x[1:-1])
    else:
        return False
    

print(ispalidrome('level'))
print(ispalidrome('tacocat'))
print(ispalidrome('abcdefghijklmnopqrstuvwxyz'))