# sample input=['kanishk', 'ritik', 'rahul', 'govind', 'dev']
# sample output+=['KANISHK', 'RITIK', 'RAHUL', 'GOVIND', 'DEV']
a=input("Enter string with space:").split()
print(a)
lst=list(map(lambda x:x.upper(), a))
print(lst)