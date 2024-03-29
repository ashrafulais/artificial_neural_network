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

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.items())
