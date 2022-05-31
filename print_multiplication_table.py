from tkinter import Y


n=int(input("Enter the number"))
l=lambda x,y:(x*y)
for i in range(1,11):
    print(l(n,i))