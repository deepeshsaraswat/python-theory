def lst(a):
    sum=0
    for i in a :
        sum+=i
    return(sum)
n=int(input("Enter the number of elements:"))
b=[]
for i in range(n):
    n=int(input("Enter the value:"))
    b.append(n)
print("sum of all elements of this list is",lst(b))