
#26/10/2023      #forloop

#in and not in membership key word 

for i in range(1,11,2):       # i varriable    type 1 #range(start,stop,step)
    print(i,end=" ")         #\n next line ku reason 2nd print theriya 
                              #stop number ku munnala number the print agu

for i in range(1,11):       # i varriable    type 2 #range(start,stop )- step-inbuild(value -1) )
    print(i,end=" ")


for i in range(11):       # i varriable    type 3 #range(stop)      start-inbuild(starting-0)   step -inbuild (value1))
    print(i,end=" ")       


# start ethula vena start panna 
for i in range(10,0,-1):
    print(i,end=" ")

for i in range(-10,0):
    print(i,end=" ")    


x="hello"    

for i in range(len(x)):      #len x 5   range(5)   type 3
    print(i,"---",x[i])

### wap to calculate the factors of a input number 

a=int(input("enter the number"))
for i in range(1,a+1):
    if(a %  i == 0):

        print("facter",a," is ",i)   

### wap to calculate the factors of a input number factore cound

a=int(input("enter the number"))             # total _ sum _ cound _ add  - kekuragana
c=0                                          #  varriable 0    c=0
for i in range(1,a+1):                       #multi_product_factor
    if(a %  i == 0):                          # varriable 1   c = 1
        c = c + 1
        print("facter",a," is ",i)   

    print("total factor ", c)

#swap  type 1         #swep work on 2 digital only # type 1 commen
x=45 
y=34

print("before swapping",x)
print("before swapping",y)

temp = x
x=y
y=temp

print("after swapping",x)
print("after swapping",y)

#swap  type 2   #pyton swap
x=6
y=8

print("before swapping",x)
print("before swapping",y)

x,y = y ,x

print("after swapping",x)
print("after swapping",y) 

### wap to print the factorial of input number   #factorial

x = int(input("enter a number = "))

fact =  1
for i in range(1,x+1):
    fact = fact * i
    
print("the factorial of ",x,"is =",fact)  

x = ( "hello how")
print(x[-3:],x[:5])
#result : how hello



