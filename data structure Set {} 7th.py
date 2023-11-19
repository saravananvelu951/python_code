                        #data structure Set {}   

      #- set is a collection unique elements.   (dubbicate elimante not printed)
      #- set is unordered.   ( any value possible to print link middle last any one)
      # - set is unindexed.    ( index not possible to print unindex)
      # - set is immutable.   (not possible to change )
      
x = {2, 4, 44.6 ,"hello" , True, 78}     #set {}   

print(x)       #print value unordered  


x = {23, 67 , 98 }

x.add(65)     #its added on any place first middle last whatever   #single elimante only 
print(x)   

x = { 1,2 , 3 , 4 , 5}

x.update({6,7,8})      #{} importane #update mean x value updated old x value die it not possible to use 

print(x)     

x = {11 , 22 , 33}

z = x.union({44 , 55,66 })   # x value update and x value also there mean is possible to use 
                             #union need to store varriable 
print(x) 
print(z)   

x = { 22 , 44 , 66 , 77}
y = { 22 , 66 , 55 , 33}

a = x.difference(y)         #mean in x kulla irukura y value remove pannutu balance value print agu ( its x.differens(y))
b = x.symmetric_difference(y)     # x and y commen value remove aidu balance value print agu 
c = x.intersection(y)     #commen value mattu print agu 

print(a)            #result 44 and 66 / commen value 22 66 that why its removed  different value printed 
print(b) 
print(c)

print("finish line")

x = { 22 , 44 , 66 , 77}

x.remove(44)   #44 removed 
#x.remove(55)    #55 not there then code error

print(x)    

x = { 22 , 44 , 66 , 77}

x.discard(66)  #66 removed some as remove method but emilate not there then error not come 
x.discard(55)   #not error blank 
print(x)    

print("end")

x = { 1 , 2, 3 , 4} 
x.clear()   #all elimant remove only SET there empty set like this set()
print(x)
 
x = { 8 , 1 , 2, 3 , 4 , 6 , 9 , 9 , 5 } 
x.pop()    #randomly one elimant pop it   #its possible to use 
print(x)


x = { 8 , 1 , 2, 3 , 4 , 6 , 9 , 9 , 5 } 
z = x.pop()    #randomly one elimant pop it 
print(z)

#set one 

z = set()    #set 
z.add(6)
#y = z.union({3 , 9 , 8})
print(y) 


#wap to remove same repeated num  

#loop method 

x = [11,22,33,44,44,55,66,11]

# z = [11,22,33,44,55,66]
z = []
for i in x:
    if i not in z:
        z.append(i)
print(z)


#set method 

x = [11,22,33,44,44,55,66,11]
 
y = set(x)    #result  {33, 66, 11, 44, 22, 55}  come on set but we want list then convert to list
              
print(list(y))    #[33, 66, 11, 44, 22, 55] 

x = [1,2,3]
y = [1,2,4]    #list is not possible to - if some one say do - then another method

z = set(x) - set(y)    #convert to set then - 

print(list(z))
# print(x-y)   
#print(list(set(x)-set(y)))  some single line 


z =  "abc"

y = set(z)   #{'b', 'c', 'a'}
f = list(z)   # ['a', 'b', 'c']
print(y)
print(f)     






