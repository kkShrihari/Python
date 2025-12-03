# Introduction to python

#usinf end argument
print("Hello world",end = '\n') #after printing defaulty goes to next line

print('Hello ',end = '') #in this case no next line by default
print('world')

print('Hello', end='=') #print =
print('world')

#using sep argument
print("Hello","world") #comma gives spaces

print("Hello","world",sep =".")  #Hello.world

#Addition using print
print(4+2)
print(4-2)
print(4*2)
print(4/2)


#A example of combination of end and sep argument
print("Hi","Hi","Hi",sep='...',end=' ')



#Escape sequences
print('\n I am \n shrihari') # new line

print("create \t tabspace") #4 space bar gap

print('This is shri\'s phone')
print("This is shri's phone")

print("My name is \"shri\".")

print("This is a backslash: \\")

#Task 2
print("'It's Hero Time!' \n \t\t -Ben 10")


# code -> interpreter(data to 1/0) -> output
# if error in 2 lines only error of 1st line is shown cause, its an interpreter

#comments
#interpreter will not run commands # single line comment

#Doc string
'''Multi line comment 1'''
"""
Multi line comments 2
"""

#Data types
#simple --> integer, float, string , boolean(True/False)
#complex ---> list, tuple, dictionary,set


"""       STRING           """
name = "michael"
age = 29
salary = 23500.50
marital_status = False

print(name,age,salary,marital_status , sep ='.')

#Identifieer naming rules
"""
1)A keyword cant be  a variable
2) name and Name are not same
3)No space allowed
4)No specail character
5) use underscore for gaps
6)start with a letter or underscore only
"""

#How to find no of keywords
import keyword
print(keyword.kwlist)



#small exercises
#Type inferred language so need to give datatype manually
name = "michael"
age = 29
salary = 23500.50
marital_status = False
print(type(name),type(age),type(salary),type(marital_status))


#can give in single line too 
name, age, available_for_work, rating = "siva", 201,True, 4.7
print(name,age,available_for_work,rating)

#Value update
name = "gomi"
name = "migo" # value updated
print(name)

#Dynamic typing
name = "shri"
name = 20
print(name, type(name)) #string updated to int


#indexing
name = "shrihari"
print(name[0])
print(name[1])
print(name[-1])

#mutability
#string is immutable also same for basic datatypes
name = "viva"
#name[0] = "s" (not pssible)
print(name)


# Operators
#-------------------arithmetic operators ------------------------------------------
#mathimatical calculations
print(5+5)

a =4
b=5
c = a/b #answer always in float
print(type(c),c)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #give remainder

print(10+5*3) #BODMAS
print(int(20-10/5*2))
 
#floor division
print(20//6)  #no point numbers

#for power
print(2**2)

#tasks
print(2**3**(2%10))



# Operators
#-------------------Relational/comparison operators ------------------------------------------
#less than , greater than etc
#output in bool

a = 10
b = 12

print(a<b)
print(a<=b)
print(a>b)
print(a>=b)
print(a==b)
print(a!=b)

a = "shri "
b = "shri"

print(a==b)
print(a!=b)


print(ord('c'))
print(ord('C'))
a = "C"
b = "c"
print(a<b) # based on ASCII values


a = "shri"
b = "z" 

print("Lets check:", a<b) # ends after comparing 1st char



# Operators
#-------------------Augmented/assignment operators ------------------------------------------
# = also an assignment operator
a =10
a =a+10  #a+=10
print(a)

a =a-10  #a-=10
print(a)

a =a*10    #a*=10
print(a)

a =a/10   #a/=10
print(a)

a =a//10   #a//=10
print(a)

a =a**10    #a**=10
print(a)




#swapping
#method 1
a = 4
b = 7
print(a,b)

temp = a
a = b
b = temp

print(a,b)

#method 2
a,b = 1,2
a,b = b,a
print(a,b)


# Operators
#-------------------Membership operators ------------------------------------------
#Results in bool /possible in string, list, set , dict, etc
list1 = [1,2,4,5,'10']
print(10 in list1)
print(1 in list1)

string1 = "shri"
print('s' not in string1)

# Operators
#-------------------Logical operators ------------------------------------------
#and , or , not
a = 10
b = 10

print(a==10 and b == 10)
print(a<10 or b >= 10) # if 1st itself 2 dont even check 2nd condition


print(not(True))
print(not(False))
print(not(a==10))


# Operators
#-------------------Binary operators ------------------------------------------
#Bitwise and 
print(10 & 11)
#1010
#1011
#------------
#1010
#-------------  

print(10 | 11)
#1010
#1011
#------------
#1011
#-------------  

print(10 ^ 11) #XOR both same - false   /both diff true
#1010
#1011
#------------
#0001
#-------------  


print(~10) #not
#1010
#------------
#0101
#Answer -11
#------------- 


print(10>>2) #right shift
#0 0 1 0 10
#8 4 2 1
#------------
#2 answer
#------------- 

print(10<<2) #left shift
#1   0   1 0 0 0
#32  16  8 4 2 1
#------------
#40 answer
#------------- 






