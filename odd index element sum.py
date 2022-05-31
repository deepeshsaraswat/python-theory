n=int(input("Enter the number of elements : "))
lst=[]
b=0
c=0
for i in range (n):
    a=int(input("Enter value {0} : ".format(i+1)))
    lst.append(a)
for i in range(n):
    if(i%2==0):
        b=b+lst[i]
    else:
        c=c+lst[i]
print("Sum of even index :",b)
print("Sum of odd index is :",c)