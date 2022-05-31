lst=list(map(int,input("Enter the element of list with a space").split()))
print(lst)

#by using lambda
# lst2=list(filter(lambda x:x>0 ,lst))
#print(lst2)

#without using lambda
def abc(a):
    if(a>0):
        return True
    else:
        return False

lst2=list(filter(abc,lst))
print(lst2)