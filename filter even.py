def even(n):
    if(n%2==0):
        return True
    else:
        return False
lst=[2,3,4,5,6,7,8]
a=list(filter((even),lst))
print(a)