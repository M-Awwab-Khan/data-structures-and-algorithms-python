array = [1, 2, 3, 4, 5]

######  Constant time complexity  #######
print('######  Constant time complexity  #######')
print(array[0])


######  Linear time complexity  #######
print('######  Linear time complexity  #######')
for element in array:
     print(element)


######  Logarithmic time complexity  #######
print('######  Logarithmic time complexity  #######')
for index in range(0,len(array),3):
     print(array[index])


######  Quadratic time complexity  #######
print('######  Quadratic time complexity  #######')
for x in array:
    for y in array:
         print(x,y)


######  Exponential time complexity  #######
print('######  Exponential time complexity  #######')
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


######  Add vs Multiply ####### 
arrayA = [1,2,3,4,5,6,7,8,9]
arrayB = [11,12,13,14,15,16,17,18,19] 

for a in arrayA:
    print(a)

for b in arrayB:
    print(b)

for a in arrayA:
    for b in arrayB:
        print(a,b)