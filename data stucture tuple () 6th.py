            #data stucture tuple

#mini 2 elimate need to tuple EX
# x = ( 1 , 3 , 4 ) this is tuple
#x = ( 1 ,)  this also tuple end is , then is possible to any elimante join in future code 
#x=(1) not tuple - tuple need mini 2 elimante 

x = (2,4,2.9,True,"hello",3,2)     #tuple
y = (2 , 4 , 6,8)

print(len(x))  
print(min(y))                    #true value 1 .false value 0 
print(max(y))
print(sum(y))
print(x.count(2))                    #this function only work on tuple : .min .max .count .len .index  .sum
print(x.index("hello"))


#tuple in immuteable  if some one said to change then OPTION is  list method
 # QA is change 4 value is 10 

x = ( 2, 4 , 6 , 7 ,8) 

y=list(x)

y[1]=10

x = tuple(y)

print(x)

#result (2, 10 , 6 , 7 ,8) 

#tuple add method            #if try to - * / then error  only + allow 
x = ( 1 , 2 , 3 ) 

y=(4 , 5 , 6 , 7 )

z = x + y

print(z)  

#result  (1, 2, 3, 4, 5, 6, 7)  

#swiping also work on tuple  and list both 

x = 5
y = 6

x,y = y,x

print(x)
print(y)

#swipe value equal method if given 3 variable then 3elimante also need if variable and elimante len is differant then error 

x,y,z = (11,22,33)

print(x,y,z) 














 





