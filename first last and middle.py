n=int(input("Enter the number of elements : "))
lst=[]
for i in range (n):
    a=int(input("Enter value {0} : ".format(i+1)))
    lst.append(a)
print(lst)
b=n//2-1

a=lst.pop()+lst.pop(0)+lst.pop(b)
print("Sum of first,middle  and last digit is ",a)