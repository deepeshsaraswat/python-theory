def toh(numbers,start,aux,end):
    if numbers==1:
        print("Move disk 1 from rod {} to {}".format(start,end))
        return
    toh(numbers-1,start,end,aux)
    print("Move disk {} from rod {} to {}".format(numbers,start,end))
    toh(numbers-1,aux,start,end)
disc=3
toh(disc,"A","B","C")