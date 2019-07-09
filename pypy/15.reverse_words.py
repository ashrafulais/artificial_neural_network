def reverser(a):
    s = ""
    for i in a:
        s += i[::-1] + " ";
    return s

#txt = input("Enter a sentence:" )
txt = "lorem ipsum dollor sit"
data = txt.split(" ")

rev = reverser(data)
print(rev)
