a=int(input("Enter the money to be withdrawn : "))
ahundred=1
a=a-100
twothousand=a//2000
rem=a%2000
fivehundred=rem//500
r=rem%500
hundred=r//100


print("Number of 2000 notes : ",twothousand)
print("Number of 500 notes : ",fivehundred)
print("Number  of hundred notes : ",ahundred+hundred)