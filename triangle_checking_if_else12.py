#2) Write a Python program to check a triangle is equilateral, isosceles or scalene


n1=int(input("Enter the first side : "))
n2=int(input("Enter the second side : "))
n3=int(input("Enter the third side : "))



if n3**2==n1**2+n2**2:
    print("Triangel is right angled! ")
elif n1==n2==n3:
    print("The triangle is equilateral")

elif (n1==n2 ) or (n2==n3) or (n3==n1) :
    print("The triangle is isoscales")

elif n1!=n2!=n1:
    print("The triangle is scalene")
else:
    print("Invalid triange !")

