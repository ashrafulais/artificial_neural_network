#strings are lists
txt = input("Enter something: ")
rev = txt[::-1]

if txt == rev:
    print("String is pallindrome")
else:
    print("String isn't pallindrome")

print("another way of reversing: "+''.join(reversed(txt)))

# using loop 
def reverseFunc(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

print(reverseFunc(txt))
