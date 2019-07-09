import random

print("Type out to terminate...")

while(True):
    a = random.randint(1,9)
    b = int(input("Guess a number: "))

    if str(b) == "out":
        break
    if a == b:
        print("you got it")
    elif a>b:
        print("too low")
    elif a<b:
        print("too high")

