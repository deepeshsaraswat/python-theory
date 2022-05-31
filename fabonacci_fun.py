def fun(x):
    a,b=0,1
    for i in range(x):
        print(a)
        a,b=b,a+b
n=int(input("Enter the number of terms  :"))
fun(n)