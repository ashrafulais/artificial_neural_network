from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
    #print(k)
    d[k] += 1
print(d.items())


s = [('yellow', 1), ('blue', 2), ('yellow', 3),\
     ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d)
