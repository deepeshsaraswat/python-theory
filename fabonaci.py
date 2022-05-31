l=int(input("Enter the number of terms:"))

y=lambda x,y:x+y

a,b=0,1
for i in range (l):
    c=y(a,b)
    print(a,end=" ")
    a,b=b,c