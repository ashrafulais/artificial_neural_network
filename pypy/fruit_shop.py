'''
clear()         Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	        Returns the value of the specified key
items()	        Returns a list containing the a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

x = car.copy()
car.clear()
car.items()

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = car.get("model")
x = car.keys()
x = car.values()
car.pop("model")
car.popitem()
x = car.setdefault("model", "Bronco")
car.update({"color": "White"})
'''

commands = ["quit", "exit", "out", "stop", "enough", "tham", "terminate", "no" ]
shop1 = { "apple":250, "banana":120, "guava":80, "pineapple":100 }
shop2 = { "apple":200, "orange":200, "mango":300, "jackfruit":350 }
print("FRUIT SHOP\nShop1>>\n")
for s in shop1:
    print(s,"-", shop1.get(s),"tk")
print("\nShop2>>\n")
for s in shop2:
    print(s,"-", shop2.get(s), "tk")
    
print("*lowercase only *exit to stop.\n")

price = int(0)
fruits = {}
while(True):
    name = input("Food name: ")
    if name in commands:
        break

    else:
        quantity = int(input("How much ? *in kg: "))

        a = int(shop1.get(name)) if shop1.get(name)!=None else 0
        b = int(shop2.get(name)) if shop2.get(name)!=None else 0

        if a != None and b!=None:
            if a==0 or b==0:
                if a==0 and b!=0:
                    price += (quantity*b)
                    fruits[name] = "2"
                    
                elif a!=0 and b==0:
                    price += (quantity*a)
                    fruits[name] = "1"
                
            elif a!=0 and b!=0:
                if a<=b:
                    fruits[name] = "1"
                    price += (quantity*a)
                    
                else:
                    fruits[name] = "2"
                    price += (quantity*b)
                    
                    
            print(price)
        else:
            print("please enter valid name...")

print("The fruits you have bought:\n")

for s in fruits:
    print(s," from shop",fruits.get(s),end="\n")
    
print("Total price: ", price)



