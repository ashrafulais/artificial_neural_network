x = range(2, 11)
for elem in x: 
    print(elem)
print("sum is: "+str(sum(x)))

numbers= range(1, 100)
div=int(input("Enter a divisor : "))
divisors=[]

for i in numbers:
    if i%div==0:
        divisors.append(i)

print("divisors are: "+ str(divisors))
