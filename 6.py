def upper(a):
    b={}
    for i in a.keys():
        c=i.upper()
        d=a[i]
        for j in range(len(a)):
            b.update({c:d})
    return(b)

x={}
n=int(input("Enter the number of elements:"))
for i in range(n):
    k=input("Enter the key:")
    v=int(input("Enter the value:"))
    x.update({k:v})
print(upper(x))

k=input("Enter the key to check:")
a=x.get(k,[v])
if(a==[v]):
    print("Key is not found:")
#conver keys in upper case
