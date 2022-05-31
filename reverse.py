def fun(x):
    a=str(x)
    rem=0
    rev=0
    sum=0
    for i in range(len(a)):
        rem=x%10
        sum+=rem
        rev=rev*10+rem
        x=x//10
    print(rev)
    print("sum of its digit is",sum)

n=int(input("Enter the number to reverse  :"))
fun(n)