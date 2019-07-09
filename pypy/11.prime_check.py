import math

def primeCheck(n=4):
    val = range(2, round(math.sqrt(n))+1)
    for i in val:
        if n%i==0:
            return 0
    return 1

num = int(input("Enetr a numebr: "))
isPrime = 1 if num <= 3 else primeCheck(num)

print("The number is " + "Yes" if isPrime==1 else "No")
    
