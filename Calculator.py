a = (int(input("Enter First Number")))
b = (input("Enter Opreation Which You Want To Do ?"))
c = (int(input("Enter Second Number")))
if b == "+":
    d = a + c
    print(d)
elif b == "-":
    e = a - c
    print(e)
elif b == "*":
    f = a * c
    print(f)
elif b == "/":
    if (c == 0):
        print("not defined")
    else :
        g = a / c
        print(g)
else:
    print("Not Define")
