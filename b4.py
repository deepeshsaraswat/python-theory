wordsfreqdict={"kanishk":32,"patel":23,"royal":45}
l=sorted(wordsfreqdict.items(), key=lambda x:x[1])
a={}
for i in l:
    a.update({i[0]:i[1]})
print(a)