def namta(number , i):
    if i != 1:
        for i in range(number):
            print(number, 'x', i, '=', number*i)

    else:
        for i in range(number):
            print(1, 'x', i, '=', 1*i)

namta(5, 2)
