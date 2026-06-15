# exercise 01
def add():
    print(5+5)
def sub():
    print(5-5)
def mul():
    print(5*5)
def dev():
    print(5/5)

# exercise 02

def findevenorode():
    n=int(input("Enter a number:"))
    if n%2==0:
        print (n,"is even number")   
    else:
        print(n,"is odd number") 

# exercise 03

def passorfail(n):
    if n>=35:
        print("pass")
    else:
        print("fail")
    n=int(input("Enter your score:"))

# exercise 04

def range_for(a,b ):
    for i in range (a,b ,-1):
        print (i)

a=int(input("num:"))    
b=int(input("num:"))
range_for(a,b)    