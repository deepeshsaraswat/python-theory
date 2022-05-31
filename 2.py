#return unique element
lst=list(map(int,input("Enter:").split()))
b=[]
for i in lst:
    if(i not in b):
        b.append(i)
print(b)