#Write a user-defined function TransformList(Arr) that accepts a list of integers. The function should modify the list in-place such that all odd numbers are multiplied by 3 and all even numbers are divided by 2.
#(Example: If Arr = [10, 15, 20, 25], it should become [5.0, 45, 10.0, 75]) (3 Marks)

def isOdd(n):
    isOdd = False
    if n%2 != 0 :
        isOdd = True
        return isOdd

def isEven(n):
    isEven = False
    if n%2 == 0 :
        isEven = True
        return isEven

def TransformList(Arr):
    for i in range(len(Arr)):
        if (isEven(Arr[i]) == True ):
            Arr[i] /= 2
        if (isOdd(Arr[i]) == True ):
            Arr[i] *= 3
    print(Arr)
TransformList([10, 15, 20, 25])

print(isEven(2))
print(isEven(3))
