def name(a):
    for i in range(len(a)):
        if(a[i]==' '):
            n=a[i:]
    print(a[0]+' '+n)

a=input("Enter your name:")
name(a)