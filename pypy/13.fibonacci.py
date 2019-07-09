def fibo():
    num = int(input("Enter fibonacci limit: "))
    n1=0
    n2=1
    n3=0

    print(n1, n2, end="\b ")
    for i in range(2, num):
        n3 = n1+n2
        print(n3 , end=" ", flush=True)
        n1 = n2
        n2 = n3
    return 0


fibo()
