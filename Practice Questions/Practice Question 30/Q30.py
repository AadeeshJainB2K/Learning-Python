str = 'cbse board'
freq = {}

for i in str :
    if i !=" ":
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

print(freq)
