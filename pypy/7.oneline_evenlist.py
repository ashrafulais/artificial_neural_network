a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = [i for i in a if i%2==0]

print(evens)

'''

import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    

evenlist = [number for number in numlist if number % 2 == 0] 

print(numlist)
print(evenlist)

'''
