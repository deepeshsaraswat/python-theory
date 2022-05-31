def isSorted(lst):
    for i in range (len(lst)-1):
        if(lst[i]>lst[i+1]):
            a=1
        else:
            a=0
    if(a==0):
        return(True)

l=[1,2,3,4]
res=isSorted(l)
print(res)