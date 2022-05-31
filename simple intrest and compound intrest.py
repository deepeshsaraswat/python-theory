principal=int(input("Enter the principal amount in rs : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the time : "))
si=(principal*rate*time)/100
ci=principal*((1+rate/100)**time)-principal
print("Simple Intrest is",si)
print("Compound Intrest is",ci)
