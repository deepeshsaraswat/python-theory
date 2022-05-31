a=list(map(int,input("Enter ").split()))
b=len(a)
for i in range (b):
    if(i%2==1):
        a[i]=a[i]**2
print(a)
