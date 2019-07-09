def pairSwapper(a, len):
    if len%2 != 0:
        len -= 1
    for i in range(0, len, 2):
        tmp = a[i+1]
        a[i+1] = a[i]
        a[i] = tmp
    return a

a = []
len = int(input("How many numbers? "))
for i in range(0, len):
    print("Enter number ",i,": ", end="")
    a.append(int(input()))
    
print("Original: ",a)
print("After modifying: ",pairSwapper(a, len))

