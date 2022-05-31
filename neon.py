def neon(n):
    sq=n**2
    sum=0
    while(sq!=0):
        sumsq=sq%10
        sum+=sumsq
        sq=sq//10
    if(sum==n):
        print("number",n,"is neon number")
    else:
        print("number is not neon")


n=int(input("Enter any number : "))
neon(n)