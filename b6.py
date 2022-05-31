from numpy import*
ar=[]
b=[]
ca=[]
(r,c)=map(int,input("Enter the value of row and column:").split())
for i in range(r):
    a=list(map(int,input("Enter row values:").split()))
    ar.append(a)
x=array(ar)
print("matrix 1=",x)
for i in ar:
    a=max(i)
    b=i.index(a)
    k=i[-1]
    i[-1]=i[b]
    i[b]=k
for i in ar:
    ca.append(i)
d=array(ca)
print(d)
    

