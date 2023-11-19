#data structure 


# 1.list      []
# 2.tople   ()
# 3.set      {}
# 4.dicsnory   {}



# List and Tuple   differant 

#list is a collection different data types (same in tuple).
# list is ordered (same in tuple).
#list is indexed (same in tuple).
#repeative elements can be allowed in list and tuple also.
#list is <b>mutable</b> and tuple is <b>Immutable</b>   

                   #list

x = [11 , 12  , 23 , True ,"hello ",  76, 35  ,'hai', 45]        # -> list []          #all data type

print(x)

print(x[3])    #index   space is not count is list 


x[5]=1000    #value change list to all data type accpect but another data type to list not accpect 

print(x)


y = [65 , 89, 32 , 76 , 56]

print(y[1:4])     #same index model

z = [ 32 , 44 , 78 , 90 , 23 , 67 , 65 , 11 , 22 ]

z[1:4] = [100,200,300,400]    # 1:5 la irukura index ku = la irukura index change aidu 

print(z)

y = [65 , 89, 32 , 76 , 56]

y[3] = "hello"   # list to entha data type venalu change pannala 

print(y)

x = [ 1 , 2 , 3] * 3   # same * int data type thavira vera ethu pottala - + / error tha 

y = [4, 5 , 6] + [ 7 , 8 , 9]

print(x)
print(y)


#Nested list
 #                       _______________ 4_______________
   #    0    1   2   3  |                               |   5    6   7    8           #index
x = [ 21 , 56 , 78 , 3 ,[56 , 98, 33, 87 , 23 , 43 , 89 ] ,12 , 98 , 32 , 67]
#                         0    1   2   3    4    5    6
print(x[4])  #4th index fulla print agu 

print(x[4][3])    #4th index la irukura 3rd index print agu 



#                ___________________2______________________
   #  0     1    |                                        |   3    4    5    6            #index
x = [ 21 , 56 , [78 , 3 ,[56 , 98, 33, 87 , 23 ], 43 , 89 ] ,12 , 98 , 32 , 67]
#                 0   1  |________2____________|  3     4 
#                          |
#                          0    1   2   3    4  


print(x[2][2][3])
print(x[2][2])
print(x[2][3])
print(x[5])

#append - single elimate last add agu  
# insert - mention pannura index munnadi add agu 
# extend  - multible elimate add pannala but [] kulla enter pannanu and  last add agu 

#append - single elimate last add agu  

x = [ 23 , 45 , 56 , 23 ]
x.append(123)
print(x)   

# insert - mention pannura index munnadi add agu 

x = [ 23 , 45 , 56 , 23 , 33, 98 ]
x.insert(3,400)
print(x)   

# extend  - multible elimate add pannala but [] kulla enter pannanu and  last add agu 

x = [ 23 , 45 , 56 , 23 ]
x.extend([1,2,3,4])
print(x)   


#importane 
x = [ [] ] * 3                    #[ [], [], [] ] 
 
x[0].append(100)                   #   0   1   2     index
print(x)                           # [[100], [100], [100]]       [ [], [], [] ]  id same that way same answer
print("bye")



x = [[],[],[] ]
x[0].append(100)
print(x)    


#type

x = [1,2,3] 
print(type(x))



x = [1, 2, [3, 4 ,[5, 6, 7, 8], 9, 10], 11, 12]

x[2].insert(2,1000)        #x[2] index 2 index 
print(x)

x = [1, 2, 3, 4 , 5 , 6 ]  

print(min(x))
print(max(x))
print(sum(x))
x.sort()       #sort low to high order 
print(x)
x.sort(reverse=True)         # sort opposite 
print(x)

x = ["hello" , "hai" , "dear" , "bye"]

print(min(x))    #alpha latter base  min mean starting a b c 
print(max(x))    #alpha latter base  max  z y x 
#print(sum(x))     # error srt not sum allow 

x.sort()              #alpha min base a  b  c  if first latter is same chack secount latter 
print(x)

#x = "snow world"
#x[3] = "s"
#print(x)    #erroe str    #TypeError: 'str' object does not support item assignment

y = [ 23, 23 , 56 , 23 , 89 , 45 , 98 , 32]
y.remove(23)       #first 23 only removed 
print(y)  

#z[23, 45 , 45]
#del z
#print(z) #del mean delete error print 


x = [ 23 , 78 , 45 , 23 , 54 , 98 ]

del x[3]      #3 index value deleted

print(x)
 
del x[2:4]    #2:4 index vara deleted 

print(x)
x = [ 23 , 78 , 45 , 23 , 54 , 98 ]

x.pop()    #pop not filled then automatic last elimant remove if you want to use that removed elimant that also possible 
x = [ 23 , 78 , 45 , 23 , 54 , 98 ]
z = x.pop()    #removed elimante stored on z 
m = z + 100 
print(x)
print(m)

x = [ 23 , 78 , 45 , 23 , 54 , 98 ]
x.pop(2)    #2 index removed but value hold if you want use then used but del mean its del not possible to use 
print(x) 
x = [ 23 , 78 , 45 , 23 , 54 , 98 ]

x.clear()   #clear mean list value empty but not error if used del then error 
print()

m = [1 , 3 , 4 , 5 , 6 , 5 , 8, 9 , 5, ]
print(len(m)) 
print(m.index(4))    #value viws index  
print(m.count(5))    #count mean how many 5 there 

#if and else 

x = [11,22,33,44,55]

    #in method
if 33 in x:
    print("present")
else:
    print("not present")
    #not method 
if 33 not in x:
    print("not present")
else:
    print("present")

x = [ 1 , 2 , 3]

y = [1, 2 , 3]

print(x==y)   #value viws checked 

print(x is y )     #address viws  #list value is some but address is not same 
print(id(x))
print(id(y))

x = [ 23 , 45 ,89, 76 , 56 ] 

for i in x:      #if i in x: there are loop print on starting to end what ever there are mention 
   print(i) 

x = ["hello", "bye","dear", "hai"]

for i in x:    #if i in x: there are loop print on starting to end what ever there are mention
   print(i)

for i in range(len(x)):   #range start 0 to end 
   print(i)   
   print(i,"---",x[i])    #i prited range then x[i]  printed there index 


## wap to multiply top two elements from  the given list

x = [ 23 , 34 , 56 , 78 , 98 ]

x.sort() 
print(x)
print(x[-1]*x[-2])  

x = [ 23 , 34 , 56 , 78 , 98 ]
x.sort(reverse=True)
print(x)
print(x[0]*x[1])    

# wap to sum and multiply all elements from each other from the given 

x = [ 1 , 2 , 3 , 4 , 5]

sum=0             #sum trick 
mul=1             #mul trick 

for i in x:
   sum=sum + i
   mul=mul * i

print("sum value = ",sum)
print("mul value = ",mul)

print("bye ")
### wap to remove all 33 from the list
                                       #method 1
x = [ 33 , 56 , 33 , 89 , 54  , 90 , 33 ]
y=[]
for i in x:
   if i == 33:
      continue
   y.append(i)
print(y)
                        #methed 2
x = [ 33 , 56 , 33 , 89 , 54  , 90 , 33 ]
for i in x: 
   if i != 33:
      print(i)
                           #method 3
x = [ 33 , 56 , 33 , 89 , 54  , 90 , 33 ]

while 33 in x:
   x.remove(33)
print(x) 


x = ["hello","hi"]
y = ["sonu","monu"]

# z = ["hello sonu","hello monu","hi sonu","hi monu"]
z = []
for i in x:
    for j in y:
        z.append(i+" "+j)
        
print(z)


x = ["hello","hi"]
y = ["sonu","monu"]


z = [i+" "+j for i in x for j in y]
print(z)




 






























