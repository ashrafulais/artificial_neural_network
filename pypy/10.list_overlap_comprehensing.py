#without set
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 5, 5, 5, 0]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 0]

print("Matched values: ")
c = []
c = [i for i in a if i in b]
print(c)


print("Non-redundant list: ")
f=[]
for i in c:
    if c.count(i)>=1 and i not in f:
        f.append(i)
print(f)

