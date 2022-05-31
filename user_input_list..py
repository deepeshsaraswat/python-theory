n=int(input("Enter the number of elements : "))
lst=[]
for i in range (n):
    a=int(input("Enter value {0} : ".format(i+1)))
    lst.append(a)
print(lst)