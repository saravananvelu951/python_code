
#while loop
i=0
while(i<=5):
    print(i)
    i=i+1

#while loop with else 

i=0
while(i<=5):
    print(i)
    i=i+1
else:
    print("bye ")
    
#reverse
  #### wap to reverse a number ex - 1234 ->4321

x=int(input("enter the number"))

rev=0
while(x>0):
    rem=x % 10
    rev = (rev * 10) + rem
    x=x//10
    print("reversed number = ",rev) 


  #### wap to reverse a number ex - 1234 ->4321  find its palindrome or not 
  #palindrome mean 121 madam nitin   like this eppadi ready pannalu latter same  ma varu

x=int (input("enter value"))

rev=0
temp=x
while(x>0):
    rem = x % 10
    rev = (rev * 10) + rem
    x = x // 10

if rev == temp:
    print("its palindrome")
else:
    print("not palindrome")

## wap to print the fibbonacci series
#fibbonacci series 0 1 1 2 3 5 8 13 ....     

x = 0
y = 1
while(x<10):
    print(x)
    x , y = y , x + y

 ## Nested Loop                   *
for i in range(1,6):            # * *
    for j in range(1,i +1):    #  * * *
        print("*",end=" ")

    print()
                            #same * result
i = 1
while(i<=5):
    print("* " *i)  
    i=i+1

i = 5
while(i>0):
    print("* " *i)  
    i=i-1
### Break,continue and pass

for i in range(1,5): 
    if i == 3:
        break
    print(i)

for i in range(1,5):
    if i == 3:
        continue
    print(i)

if(10 > 5):
    pass
print("hello")



#prime number 
x = int(input("enter a number = "))
y = int(input("enter a number = "))
for i in range(x,y+1):
    if i > 1:
        for j in range(2,i):
            if (i % j == 0):
                break
        else:
            print(i)

i=0
while(i<=5):
    print(" " * (5 - i )+ "* " * i )
    i=i+1


i=0
while(i<=5):
    print(" "  * (5 - i) + "*" * i)
    i=i+1  


i=5
while(i>=0):
    print(" " * (5 - i )+ "* " * i )
    i=i-1










