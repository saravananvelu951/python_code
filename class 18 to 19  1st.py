                          #PYTHON CLASS OWN NOTES                  #wifi pass sapuser@1234aspl
#string = " hello dear "   if any latter come inside of " " that is string
#int = 2 7 749 number 
#float = 9.7 9.4 8.3 like this 
#bool = True or false 

#variable 
a=78    #a varriable
b="hello dear"    #b varriable


#varriable rules 
#1 variable can be start alphabets only EX - abc xyc 
#2 _ is only special character allowed in varriable not any another special character EX ac_b  _abc xyz_
#3 variable cant be start number EX 124 87b8388
#4 keyword not allowed in variablle 


#if both varriable value is same then result shoud be last value  
x=78
x=90
print(x)

#id (address faction)
#if x have multible role but value is diftert then result come out some address(one address only)

x=57
x=99
y=76
print(id(x))
print(id(y))

#string ((str)

print(dir(str))   #all type of string  like : upper , lower , alpha , alnum , digital , numeric , capitalize 

x="hello dear "

print(x.upper())
print(x.lower())
print(x.capitalize())

#bool string if we used IS befor string that work bool type like: isupper , isalpha , islower 

y="hello dear how are you"

print(y.isupper())
print(y.islower())

#Index 
s="hello baby"         #index latter entha edathula irukuna mention pannu 
print(s[0])       #L to R read panna 0 1 2 3 4 R to L read panna -1 -2 -3 -4  important spase kuta oru place the 
                        #print la [] ulla entha place venumo enter pannanu 

#slicing (slicing mean :)

print(s[0:5]) #start 0 end 5 mean o start agi 4 vara iruku latter print pannu ..4 vara venuna 
               #entha latter last ta venumo athuku anutha place number enter pannanu 

y="hello dear my "
print(y[:4])
print(y[:-3])       #starting fill pannalana auto matic ka 0 index last la fill panalana automatic last latter   aguramari 
print(y[0:])       

#23/10/20233

#start_index : end_index : skip\stop_index
#start(0) : end(-1)  : skip(index skip pannu ex 2 mean 2 2 index sa skip pannite iruke )
w="hello my dear "
print(w[0:8:2]) #result : hlom   h appara irukura 2 latter skip appara print appara 2 latter skip 

#len function 
p="hello how  my hy dear bob"
print(len(p)) #len 

print(p.index("m"))   #nera work oda index ku if enter pannura index illaa error 
print(p.find("y"))    #nera work oda index ku (same for index medal)
print(p.find("w"))    #nera work oda index ku if enter pannura index illaa - value varu
print(p.index('h'))       
print(p.index('h',7)) # 7 appara irukura "h" 
print(p.rfind('h')) #lastla irutha 'h' oda index find pannu 

print(p.index("dear"))    #oru sentance oda index print agathu sentace oda first latter oda index mattutha print agu 

#replace function
s="hello baby "
print(s.replace('baby','mine'))      #replace function

#operators
print(10 + 10)        #20f
print(10 - 10)        #0
print(10 * 10)        #100
print(10 /  5)        #2.0  single / result float value 
print(10 // 4)        #2     #floor division  not float value of float value coming then also it result will be floor(number )
print(10 % 5)         #0       # mod
print(5 % 10)         #5
print(2 ** 5)        #32 #  ** mean 2 squar 5

## comparison op. True or false 

print(10 > 10)        # False
print(10 < 10)        # False
print(10 >= 10)       # True
print(10 <= 10)       # True
print(10 == 10)       # True
print(10 != 10)       # False 

print("end")

## Logical op.   (  and,or,not )  true or false 
print(5<10 and 90>80)   #and mean both true value only 
print(5<10 and 90<80) 
print(5<10 or 90<80)    #any one true value 

print("end 1")

print(5 >3 and 9 > 3 or 6 > 9)  #first T 2nd T 3rd F   
                               #5 >3 and 9 > 3 = True
                               # 9 > 3 or 6 > 9 = True 
print( 9 > 10 or 6 > 9 and 90 > 38)        
print(10 > 5 or 50 < 60 and 10 > 67)               #first and value then or value 

print(not(10 > 5 or 50 < 60 and 10 > 67))   #not mean result changer if apply for true vallue then result false 
print(not(4 > 5 or 50 < 60 and 10 > 67))

### Bitwise oper. ( & ,| ,<<,>>  ,~ )     & mean and    | mean or  ~ = ~n 
print(20 & 50 )      #first we want chake bynery 32  16  8  4  2  1      total  bynery value varanu
                      #                          0    1  0  1  o  0     - 20 bynery 
                      #                          *    *  *  *  *  *          #                          1    
                      #                          1    1  0  0  1  0     - 50 bynery
                      #                value      0   1  0  0  0  0       1 value place 16 result 16
print(20 & 54)     
                    #first we want chake bynery 32  16  8   4  2  1      total  bynery value varanu
                      #                          0    1  0  1  o  0     - 20 bynery 
                      #                          *    *  *  *  *  *          #                          1    
                      #                          1    1  0  1  1  0     - 54 bynery 
                      #                value     0    1  0  1  0  0       1 value place 16 another 1 place value 4 tatal 20 result 20 
print(20 | 54)    
                     ##first we want chake bynery 32  16  8   4  2  1      total  bynery value varanu
                      #                          0    1  0  1  o  0     - 20 bynery 
                      #                          +    +  +  +  +  +          #                          1    
                      #                          1    1  0  1  1  0     - 54 bynery 
                      #                value     1    1  0  1  1  0       -toal 1 place oda value 54 result 54


print(36 << 2)      
                     ##first we want chake bynery 32  16  8   4  2  1   
                     #                             1   0  0   1  0  0     36 bynery  << left la iruthu 2 pit veliya edukanu but value loos aga kudathu 
                     #                     128 64 32  16  8   4  2  1           pit men 1 0 0 1 answer
                     #                     0   0   1   0  0   1  0  0         << 2 pit remove 128 64 pit remove
                    #<< 2 pit remoce pannita right la irukura answerr left ku kila vanthutu empty eda 0 aidu
                    #                      128 64 32  16  8   4  2  1
                    #                        1  0  0   1  0   0  0  0   = 144 total  result 
                    # only << left 

print(5 >> 2)        #              8 4 2 1           
                     #              0 1 0 1   #5bynery   >> right 2 pit remove  pannita right answer move agu so 
                     #              8  4  2   1
                     #              0  0   0  1     result one 
                     #   value lose agu but move panna option illa 
print(~4)         #~ = ~n  and -(n+1)     n=print value    odd case 
                   #       -(4+1)    -5


print(~~4)   # result ~~ = n even case   
             #even case result n =  4 

#Escape character   ( \  , \t   , \n)

n="hello \"how\" are you "    
print(n)         

k="hekko \tby yo"
print(k)           #\t one tab space  


j=" hello dear \n where are you"   #n mean new line 
print(j)

u="\\t"   
print(u)





















