def fact(a):
    fact=1
    for i in range(a,0,-1):
        fact*=i
    return fact
n=int(input("Enter the number to find factorial"))
print("factorial is ",fact(n))
