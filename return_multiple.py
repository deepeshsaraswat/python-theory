def multiple(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a//b
    return c,d,e,f
x=int(input("Enter first no:"))
y=int(input("Enter the second no:"))
n,n1,n2,n3=multiple(x,y)
print(n)
print(n1)
print(n2)
print(n3)
