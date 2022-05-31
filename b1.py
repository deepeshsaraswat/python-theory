m={}
m[1]=1
m['1']=2
m[1.0]=4
sum=0
for k in m:
    sum+=m[k]
print(sum)