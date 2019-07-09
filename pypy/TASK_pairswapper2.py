a = [1, 2, 3, 4, 5, 7, 3, 8]
len = len(a)

print(a)
i = 0
while(True):
    a[i:i+2] = a[i:i+2][::-1]
    if i>=len:
        break
    i += 2

print(a)
