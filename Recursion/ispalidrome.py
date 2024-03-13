def ispalidrome(x: str) -> bool:
    for i in range(len(x)):
        if x[i] == x[len(x) - i - 1]:
            ispalidrome(x[i + 1:len(x) - i - 1])
            return True
        else:
            return False
    

print(ispalidrome('level'))
print(ispalidrome('tacocat'))
print(ispalidrome('abcdefghijklmnopqrstuvwxyz'))