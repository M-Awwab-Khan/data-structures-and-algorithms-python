################ Interview Questions #############
#Question1 - O(n)
def foo(array):
    sum = 0
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

ar1 = [1,2,3,4]
foo(ar1)

#Question2 - O(n^2)
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))