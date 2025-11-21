# Aim = [1,4,9,16,25,36,49,64,81,100]

aim = []
i = 1 
while i <= 10 :
    aim.append(i*i)
    i += 1
print(aim)

elemnetToSearch = int(input("Enter the element to search in the list: "))
found = False
i = 0
while i < len(aim):
    if aim[i] == elemnetToSearch:
        found = True
        print(i)
        break
    i += 1
