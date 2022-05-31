def fun(x):
    a=x[-1: :-1]
    if(a==x):
        print("String is palindrome")
    else:
        print("String is not palindrome")
    
n=input("Input the string  :")
fun(n)