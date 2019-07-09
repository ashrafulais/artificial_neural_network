def withoutSet(c):
    print("With list: ")
    f=[]
    for i in c:
        if c.count(i)>=1 and i not in f:
            f.append(i)
    print(f)

def withSet(lst):
    print("With set: ")
    print(set(lst))
    


lst = [1, 3, 4, 5, 6, 5, 3, 7, 8, 6, 5, 3, 5, 6]
withoutSet(lst)
withSet(lst)

print("Note: List contains[] and set contains {}")
