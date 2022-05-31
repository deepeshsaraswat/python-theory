def hamming(a,b):
    c=a^b
    d=bin(c)
    e=str(d)
    f=len(e)
    suma=0
    for i in range(f):
        
        if(e[i]=='1'):
            suma+=1
    print("Hamming distance is ",suma)

n1=int(input("Enter the first no:"))
n2=int(input("Enter the second  no:"))
hamming(n1,n2)

     