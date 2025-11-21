#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method) eg:- Naman , Racecar etc.

list1 = ["r","a","c","e","c","a","r"]

list2 = list1.copy()

list2.reverse()

if list1 == list2 :
    print(True)
else: 
    print(False)