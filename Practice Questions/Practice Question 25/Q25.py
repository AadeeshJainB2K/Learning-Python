#Write a user-defined function AnalyzeString(txt) that accepts a string and returns a tuple containing the count of uppercase letters and lowercase letters.
#(Example: If txt = "Hello World!", it should return (2, 8)) (2 Marks)

def AnalyzeString(txt):
    upper = 0
    lower = 0
    tup = ()
    for i in range(len(txt)):
        if (txt[i].isupper() == True):
            upper += 1
        if (txt[i].islower() == True):
            lower += 1
    tup = (upper,lower)
    return tup

print(AnalyzeString("Hello World!"))
