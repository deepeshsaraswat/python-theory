'''# program to know global and local variable
a=20
def fun():
    
    global a #to access global variable in loc
    a=a+20
    print(a)
fun()

print(a) # now the value of a is changed '''



# program to know non local variable
def fun():
    a=20 # Non local variable
    def asc():
        nonlocal a
        a=10+a
        print(a)

    asc()
    print(a)

fun()
