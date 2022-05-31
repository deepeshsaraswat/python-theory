n=input("Enter elements separated by commas :").split(',')
print(n)
lst=[int(num) for num in n]
print(lst)
tpl=tuple(lst)
print(tpl)
element=int(input("Enter element to search:"))
try:
    pos=tpl.index(element)
    print("Element found at position no ",pos+1)
except:
    print(" element not found in the tuple")


