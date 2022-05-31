def num(a,b,c):
    if((a>b) and (a>c)):
        return(a)
    elif((b>c) and (b>a)):
        return(b)
    else:
        return(c)
a1=int(input("Enter 1 no:"))
a2=int(input("Enter 2 no:"))
a3=int(input("Enter 3 no:"))
print("maxim no is",num(a1,a2,a3))
