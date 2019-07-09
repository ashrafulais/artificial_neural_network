import string
import random

if input("Do you want strong password? ") == "yes":
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?_"
    length = 20
    p = "".join(random.sample(s, length))
    print(p)


    #another option
    def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
            return ''.join(random.choice(chars) for _ in range(size))

    print(pw_gen(length))

else:
    plist = ["Hello", "World", "lolpass", "unknown"]
    print("".join(random.sample(plist, 1)))
