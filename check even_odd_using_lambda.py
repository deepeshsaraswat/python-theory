f=lambda a:True if a%2==0 else False
n=int(input("Enter the number to check :"))
b=f(n)
if(b==True):
    print("It is even number")
else:
    print("Not even")