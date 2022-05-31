#write a program to find the number of rabits and cock given the number of head and number of leg
head=int(input("Enter the total no of head : "))
leg=int(input("Enter the total no of legs : "))
rabbit=(leg//2-head)
cock=2*head-(leg//2)
print("no of rabbit : ",rabbit)
print("Total no of cock : ",cock)