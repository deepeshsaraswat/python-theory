def mygen(x,y):
    while(x<y):
        yield x
        x+=1

a=int(input("Enter starting limit:"))
b=int(input("Enter the end limit:"))

g=mygen(a,b)
for i in g:
    print(i,end=" ")