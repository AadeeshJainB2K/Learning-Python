def safe_array_divider(L1, L2):
    r = []
    for i in range(max(len(L1),len(L2))):
        try:
            r.append(L1[i]/L2[i])
        except ZeroDivisionError:
            print("L2 got a 0 at" , i , "index")
            print("Div by Zero")
            break
        except IndexError :
            print("unequal lengths")
            break
        else: isSucessful = True
    else:
        print(r)

safe_array_divider([1,2,3],[1,2,3])
safe_array_divider([1,2,3],[1,2,3,4])
