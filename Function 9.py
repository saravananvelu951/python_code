       #function     

       # - it is a piece of code of block


#function def (varriable):     last call    in middle normal program 
def xyz():         #def mean defination or define      

    print("hello dear ")

xyz()                       #call is import how many time if you want it possible 



def xyz():               #function 
    x = 9
    y = 8                               #middle program 
    z = x + y  
    print(z)

xyz()                  #call 


def add(a , b):      #position      #formal argument 

    z = a  + b
    print(z)              # position and argument want to some count 

add(4 , 7)        #argument     #actual argument 


#if argument not mention then it will be run but possition not mention then it will be error 

## positional argument functions
x = int(input("enter a number = "))
y = int(input("enter a number = "))
z = int(input("enter a number = "))

def add(a,b,c):   #formal arguments
    z = a + b + c
    print(z)
    
add(x,y,z)         # input == position == argument   some count 


w = 23       #it glopble varriable is possible to use anywhere
t = 2

def add():
    m = w + t      #its lockel varriable only use for def in side 
    print(m)

add()


x = 10   #global variables
y = 10

def xyz():
    global x     #changed x varriable lockel to groble 
    x = 100   #local variables 
    y = 100   #local vcariables
    z = x + y #local variables
    print(z)
  
print(x)    #first x value 
xyz()    # call 
print(x)    #after call x value its changed value 



def ver(x=2,y=4):
    z = x + y              
    print(z)

ver()
ver(4)      #x = 4 y there in position 
ver(4,5)      #firt argument value taken if argument not there then position value taken 


def add(*x):
    print(x)
   # print(y)      #its result come out tuple 

add(1,2,3,4,5,6)    #*x mean    its all value in x 

def add(x,*y):
    print(x)
    print(y)

add(1,2,3,4,5,6)     #first value = y , another all values in x      

# *arg used after no possible to mention another 

# **keyarg

def add(*x,**y):
    print(x)
    print(y)                  # ** #its result come out dictnory 


add(5,4,3,a=5,b=9,c=34)       #a=5,b=9,c=34    its only ** key arg 


def dev():
    x = 8
    y = 5
    z = x + y
    return z       #after return code not run 
    print("hello")
print(dev())    #return call mothed 

def dev():
    x = 8
    y = 5
    z = x + y
    m = x - y
    return z , m
print(dev())      

def dev():
    x = 8
    y = 5
    z = x + y
    return z
c = dev()       #store value to new varriable #return call mothed  2
print(c)


# ## Function overloading and function overidiing
# whenever two or more functions having same name but the no. of parameters is different then it is called function overloading

# whenever two or more functions having same name and  the no. of parameters is also same but the task is different then it is called function overridding

#function overloading 

from multipledispatch import dispatch

@dispatch(int,int)
def xyz(x,y):
    print(x,y)

@dispatch(int,int,int)   
def xyz(x,y,z):
    print(x,y,z)
    
xyz(4,5)
xyz(6,7,8)

## Recursion    

  #- function calling itselfs

#def hell():
 #   print("hello dear")
 #   hell()                        #it run storage speach time only when storage full then it died 

#hell()

# Q1 wap of factorial using recursion

x =  int(input("enter a number  = "))
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
    
c = fact(x)
print(c)


# Q1 wap of fibonacci using recursion
# 0 1 1 2 3 5 8 13 21...

x =  int(input("enter a number = "))

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-2)+fib(n-1)

if x <0:
    print("series doesn't exists")
else:
    for i in range(x):
        print(fib(i))