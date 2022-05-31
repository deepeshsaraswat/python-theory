n=eval(input("Enter elements of tuple in ()braces: ")) #ex-->Enter elements of tuple in ()braces: (1,2,3)
sum=0
for i in range (len(n)):
    sum+=n[i]
print("Sum of all elements is : ",sum)