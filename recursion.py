'''i=0
def name():
    global i   # to take global value to know how many times this code will execute
    i+=1
    print("kanishk",i) # this wil print around 1000 times name
    name()
    
name() '''

import sys
sys.setrecursionlimit(2000)  # now this will print 2000 times after that it will give error 
i=0
def name():
    global i   # to take global value to know how many times this code will execute
    i+=1
    print("kanishk",i) # this wil print around 2000 times name
    name()
    
name()