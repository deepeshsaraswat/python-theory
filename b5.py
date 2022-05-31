f=open('data.txt','r')
a=f.readlines()
l=[l.strip() for l in a]
wo=0
ch=0
digit=0
for i in l:
    w=i.split()
    wo+=len(w)
    for j in i:
        if(((j>='a') and (j<='z'))or ((j>='A') and (j<='Z'))):
            ch+=1
        elif((j<='9') and (j>='0')):
            digit+=1

print("lines",len(l))
print("words",wo)
print("Characters",ch)
print("digit",digit)
