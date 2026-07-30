#Write a user-defined function ExtractPrimes(NumList) that takes a list of integers and returns a new list containing only the prime numbers from the original list. (2 Marks)
def isPrime (n):
    if (n<0):
        return False
    for i in range (2,n):
        if (n%i*i == 0):
            return False
        else:
            return True

def ExtractPrimes(NumList):
    r = []
    for i in range(len(NumList)):
        if (isPrime(NumList[i]) == True):
           r.append(NumList[i])
    return r

sample_list = [1, 2, 3, 4, 7, 9, 11, 15, 23]
print(ExtractPrimes(sample_list))
