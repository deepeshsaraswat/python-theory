# unique list means remove duplicate elements from the list
def lst(a):
    b=[]
    for i in a:
        if(i not in b):
            b.append(i)
    return(b)

n=int(input("Enter the number of elements:"))
b=[]
for i in range(n):
    n=int(input("Enter the value:"))
    b.append(n)
print("unique list is ",lst(b))
