          # Dict---> {key:value}  

       # dict is a collection of key value pair
       # dict is ordered
       #dict is unindexed
       # dict is mutable  

x = {
    'a' : 3,                  # , impoty   'a'  import  
    'b' : 4,
    'c' : 9
}

print(x)


x = {
    'a' : 3,                
    'b' : 4,
    'c' : 9
}

print(x['b'])      #key value only printed   

x['b'] = 11     #'b' value changed 

print(x)

x = {

    'a':1,
    'b':2,
    'c':3
}
#print(x['d'])  #key not available then erroe 

print(x.get('b'))   #key not there then result is NONE it possible to tag text messange also 

print(x.get('d','key not found'))   #text messange 

x = {
    
    'a':1,
    'b':2,
    'c':3
}

x['d'] = 43       #if invalid value try to change then it will be make new key  pair 

print(x)    
  
x = {
    'a':1,
    'b':2,
    'c':3,
    56 :78,
    6.7:19
}
print(x)    #int key also  

x = {
    'a':200,
    'b':100,
    'a':589,
    'c':3,
    'a':300

}
print(x)   #if there have dub value then last coming key and value only print 
        
x = {
    'name'  : ['sohan','mohan','rohan'],  #list
    'age'   : (34,56,67),    #tuple
    'marks' : {23,5,56}    #set
}

print(x)  


x = {
    'name'  : ['sohan','mohan','rohan'],
    'age'   : (34,56,67),
    'marks' : {23,5,56}
}
x['name'].append('ram')

print(x)

x = {
    'a':1,
    'b':2,
    'c':3
}
print(x.keys())
print(x.values())
print(x.items())   

x = {
    'name':'abhinav',
    'age':20,
    'marks':9.9
}
print(x['name'],"---",x['age'],"---",x['marks'])

x = {
    'a':1,
    'b':2,
    'c':3
}  

if 'a' in x:     #dict running for key
    print("presend")
else:
    print("not presend")   

if 1 in x:     #dict running for key    1 is value that why is printed not presend 
    print("presend")
else:
    print("not presend")

if 'a' in x.items():    #a is key items mean 'a':1  
     print("presend")
else:
    print("not presend")   


if ('a', 1)in x.items():    #a is key items mean ('a',1 ) 
     print("presend")
else:
    print("not presend")   

x = {
    
    'a':1,
    'b':2,
    'c':3
}

# del x['a']
print(x)    #before x all value there 
g = x.pop('b')      #empty pop not allow   mentioned key  as printed  , it printed value only 
z = x.popitem()     #last key and value like 'a':1 printed , empty allow  , it printed key and value 
print(x)   #after pop and popitem ---pop b remove and popitem last key and value remove then balance 'a':1 only 
print(z)
print(g)

print("end game")

#forloop 

x = {
    'a' : 1,
    'b' : 2,
    'c' : 3
 }

for i in x:     #it will be print key only 
    print(i)

for i in x:
    print(i,"----",x[i])          

for i in x.values():     #it will be print key pai only not key 
    print(i)

for i in x.items():
    print(i)             #it will be print key and key pair 

for i ,j in x.items():      #i key j key pair  
    print(i,"----" ,j)


x = {
    'a' : 1,
    'b' : 2,
    'c' : 3
 }
#x['d'] = 29   #it new key and pair add but only one key pair


#multible key and pair added method

x.update({'f':43 , 'r':32})     #multible key and pair added method 
print(x)



x = "hello how are you"

z = {}

for i in range(len(x)):
    if x[i] not in z:
        z[x[i]] =[i]

    else:
        z[x[i]].append(i)

print(z)



