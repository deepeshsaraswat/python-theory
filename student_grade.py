n1=int(input("Enter the number of subject physics : "))
n2=int(input("Enter the number of subject chemistry : "))
n3=int(input("Enter the number of subject math : "))
n4=int(input("Enter the number of subject Biology : "))
n5=int(input("Enter the number of subject Computer : "))
a=(n1+n2+n3+n4+n5)//5
print("Percentage is ",a)
if(a>=90):
    print("your grade is A")
elif(a>=80):
    print("Your grade is B")
elif(a>=70):
    print("Your grade is C")
elif(a>=60):
    print("Your grade is D")
elif(a>=840):
    print("Your grade is D")
elif(a<40):
    print("your grade is F")
