from numpy import*
ar=[]
(r,c)=map(int,input("Enter the value of row and column:").split())
for i in range(r):
    a=list(map(int,input("Enter row values:").split()))
    ar.append(a)
x=array(ar)
print("matrix 1=",x)
for i in range(r):
    
    for j in range(len(x[i])):
        arr=x[i][j]
        print(arr)
        if((x[i][j])%3!=0):
            x[i][j]=0

print(x)
