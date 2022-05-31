def per(n):
    suma=0
    for i in range(1,n):
        if(n%i==0):
            suma+=i
    if(suma==n):
        print("No is perfect:")
    else:
        print("No is not perfect :")
x=int(input("Enter the number that you want to check"))
per(x)
        
