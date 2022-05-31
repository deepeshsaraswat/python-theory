n=int(input("Enter the number of elements : "))
lst=[]
for i in range (n):
    a=int(input("Enter value {0} : ".format(i+1)))
    lst.append(a)
print(lst)
for i in range(n-1):
    for j in range(n-1-i):
        if(lst[j]>lst[j+1]):
            t=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=t
print("list in sorted order :",lst)
