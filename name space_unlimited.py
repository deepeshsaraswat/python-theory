def name(n):
    sum=0
    n=" "+n
    for i in range(len(n)):
        if(n[i]==" "):
            sum+=1
    print(sum)        
    temp=0
    for i in range(len(n)):
        if((n[i]==" ") and temp!=(sum-1)):
            a=n[i+1]
            print(a,end=""+" ")
            temp+=1
        elif((n[i]==" ") and temp==(sum-1)):
            b=n[i:len(n)]
            temp+=1
            print(b,end="")
        
a=input("Enter the name :")
name(a)