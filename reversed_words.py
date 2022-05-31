def reverse(x):
    a=x.split(" ")
    b=" ".join(reversed(a))
    return(b)


if __name__=='_main_':
    n=input("Enter the words to be reversed: ")
    print(reverse(n))

