def isPrime(n):
    if n<0:
        return False
    else:
        for i in range(2,n):
            if (n%i*i == 0):
                return False
    return True

def ExtractPrimes(NumList):
    result = []
    for i in NumList :
        if isPrime(i) == True :
            result.append(i)

    return result

sample_list = [1, 2, 3, 4, 7, 9, 11, 15, 23]
print(ExtractPrimes(sample_list))
