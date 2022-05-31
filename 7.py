f=open('table.txt','w')
for i in range(1,11):
    for j in range(1,11):
        b=i*j
        f.write(str(b)+"\n")
    
f.close()