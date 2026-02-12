s =  input("Enter a string to check if it is a palindrome :")
if (s==s[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")