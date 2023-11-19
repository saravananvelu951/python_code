if (5 > 4):                        #if contusion not true then else print  
 print("5 greater then 4")
 print("done")                     #if true na athuku kila ethana print vena pannala



if(19 > 29):
    print("19 is greater then 29")
else:
    print("5 not greater then 4")          #one else print achina then code run agathu 


if(1):
    print("one")          #if contusion ulla 0 _ false _ none print panna result false tha 
    
if(0):
    print("zero")

if(10.6):
    print("10.6")
    
if("hello"):
    print("hey")

if(True):
    print("true")
    
if(False):
    print("false")

if (None):
    print("none")

print(" line end")

#if-elif-else    

if(100 > 15):                              #elif extra contusion if or elif true na ethu first true varutho atha print agu 
    print("hello")
elif(20 > 25):
    print("hey")
elif(30 > 36):
    print("hi")    
else:
    print("bye")



#nested if 

if(60 > 40):
    print("hello")
    if(59 > 32):                            #indetation importane   if ku next line vara antha space the indetation
        print("good")
        if(70 > 90):
            print("no")
        else:
            print("wrong")
    else:
        print("okok")
else:
    print("yeah")

#user input 
#x=(str(input("enter name ")))
#print(x)   

#possitive and negative value 

x = int(input("enter a number = "))

if x > 0:
    print(x,"is positive")
elif x == 0:
    print(x,"is zero")
else:
    print(x,"is negative")
 
 #3 type triangle 

s1 = int(input("enter a 1st side = "))
s2 = int(input("enter a 2nd side = "))
s3 = int(input("enter a 3rd side = "))

if s1 == s2 == s3:
    print("eq. tri")
elif(s1 == s2 or s2 == s3 or s1 == s3):
    print("iso. tri.")
else:
    print("scal. tri")

#fizzbuzz

x = int(input("enter a number = "))

if(x % 3 == 0 and x%5 == 0):
    print("fizzBuzz")
elif(x % 5 == 0):
    print("buzz")
elif(x%3 == 0 ):
    print("fizz")
else:
    print(x)



x=int(input("enter the value "))

if(x>80 and x<=100):
    print('rank a') 

elif(x>60 and x<=80):
    print("rank b")

elif(x>40 and x<=60):
    print("rank c")

elif(x>20 and x<=40):
    print("rank d")

elif(x>0 and x<=20):
    print("fail") 

else:
    print("invalid ")  

#greatest value 

x=int(input("enter 1st "))  
y=int(input("enter 2nt "))
if(x>y):
    print(x)
    print("value greter")
elif(x<y):
    print(y)    
    print("value greater ")

 
                                    