n=int(input("enter the month number :"))
if(n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12):
    print("This is a month of 31 days!")
elif(n==2):
    print("this is a month of 28 or 29 days!")
else:
    print("This is a mont of 30 days!")