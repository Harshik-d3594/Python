# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 21:09:47 2022

@author: Agroveggies
"""

#assignment 1. 

#area of circle 

pi = 3.141592
r = float(input("Enter the radius of the circle : "))
area = pi*r*r
print("Area of the cirle : " ) 
print(area)


#operators : arithmetic and comparision

#set 1 values :
    
x = 7
y = 9

c = x + y
print("the sum is",c)

c = x - y
print("the difference is",c)

c = x*y
print("the product is",c)

c = x/y
print("the division is",c)

c = x%y
print(c)

c = x**y
print(c)

c = x//y
print(c)


#set 2 values :
    
x = 3
y = 8

c = x + y
print("the sum is",c)

c = x - y
print("the difference is",c)

c = x*y
print("the product is",c)

c = x/y
print("the division is",c)

c = x%y
print(c)

c = x**y
print(c)

c = x//y
print(c)


#set 3 values :
    
x = 6
y = 15

c = x + y
print("the sum is",c)

c = x - y
print("the difference is",c)

c = x*y
print("the product is",c)

c = x/y
print("the division is",c)

c = x%y
print(c)

c = x**y
print(c)

c = x//y
print(c)


# set 4 values :
x = -1
y = 7

c = x + y
print("the sum is",c)

c = x - y
print("the difference is",c)

c = x*y
print("the product is",c)

c = x/y
print("the division is",c)

c = x%y
print(c)

c = x**y
print(c)

c = x//y
print(c)


# set 1 values :
x = 5
y = 55

if x == y :
    print("equal")
else:
    print("not equal")


if x != y:
    print("not equal")
else:
    print("equal")


if x>y :
    print("x is greater")
else:
    print("y is greater")


if x<y :
    print("x is smaller")
else :
    print("y is smaller ")


if x >= y :
    print("x is greater equal")
else :
    print("y is greater equal")
    
    
if x <= y :
    print("x is lesser equal")
    
else :
    print("y is lesser equal")
    

# set 2 values :
x = 56.5
y = 57

if x == y :
    print("equal")
else:
    print("not equal")


if x != y:
    print("not equal")
else:
    print("equal")


if x>y :
    print("x is greater")
else:
    print("y is greater")


if x<y :
    print("x is smaller")
else :
    print("y is smaller ")


if x >= y :
    print("x is greater equal")
else :
    print("y is greater equal")
    
    
if x <= y :
    print("x is lesser equal")
    
else :
    print("y is lesser equal")



# set 3 values :
x = 68
y = 68

if x == y :
    print("equal")
else:
    print("not equal")


if x != y:
    print("not equal")
else:
    print("equal")


if x>y :
    print("x is greater")
else:
    print("y is greater")


if x<y :
    print("x is smaller")
else :
    print("y is smaller ")


if x >= y :
    print("x is greater equal")
else :
    print("y is greater equal")
    
    
if x <= y :
    print("x is lesser equal")
    
else :
    print("y is lesser equal")    
    
    
# set 4 values :    
x = 59
y = 43

if x == y :
    print("equal")
else:
    print("not equal")


if x != y:
    print("not equal")
else:
    print("equal")


if x>y :
    print("x is greater")
else:
    print("y is greater")


if x<y :
    print("x is smaller")
else :
    print("y is smaller ")


if x >= y :
    print("x is greater equal")
else :
    print("y is greater equal")
    
    
if x <= y :
    print("x is lesser equal")
    
else :
    print("y is lesser equal")    



#LIST METHODS

#1. Append()

fruits = ['apple' , 'banana' , 'mango'] #list name is fruits
fruits.append("orange")                 #append means to add
print(fruits)



#2. Clear()

fruits = ['apple' , 'banana' , 'mango']
fruits.clear()                          #clears all elements in the list
print(fruits)



#3. Copy()

fruits = ['apple' , 'banana' , 'mango']
x = fruits.copy()                       #copies the list
print(x)



#4.Count()

fruits = ['apple' , 'banana' , 'mango']
x = fruits.count("mango")               #no. of times the value appears
print(x)



#5.Extend()

fruits = ['apple' , 'banana' , 'mango']     #list 1

vegetables = ["potato" , "onion" , "cabbage"] #list 2

fruits.extend(vegetables)           #extends the list of fruits with vegetables

print(vegetables)
print(fruits)



#6.Index()

fruits = ['apple' , 'banana' , 'mango'] 
fruits.index("mango")    #gives the position


#7.Insert()

fruits = ['apple' , 'banana' , 'mango']
fruits.insert(3, "cherry")               #insert any element in the list
print(fruits)



#8.Pop()

fruits = ['apple' , 'banana' , 'mango']
fruits.pop(1)                          #delete a particular element from list
print(fruits)



#9.Remove()

fruits = ['apple' , 'banana' , 'mango']
fruits.remove("apple")                #remove an element from list
print(fruits)



#10.Reverse()

fruits = ['apple' , 'banana' , 'mango']
fruits.reverse()                        #reverses the list
print(fruits)




#Sort()

fruits = ['apple' , 'banana' , 'mango']
fruits.sort()                           #sorts the list
print(fruits)

   
    

#STRING METHODS

#1.Capitalize()

name = "harshik , amitesh , harsh"
x = name.capitalize()       #makes the first letter of first word capital
print(x)


#2.Casefold()

x = name.casefold()         #makes the first letter of first word lowercase
print(x)



#3.Center()

x = name.center(40)      #returns a centred string
print(x)

#4.Count()

txt = " i love apples , apple is my fav fruit"
y = txt.count("apple")      #no. of times a specified value occurs in a string
print(y)


#5.Encode

name = "harshik , amitesh , harsh"
z = name.encode()          #returns an encoded version of the string
print(z)



#6.Endswith()

name = "harshik , amitesh , harsh"
z = name.endswith("h")     #returns true if string ends with specified value
print(z)



#7.Expandtabs()

txt = "h\te\tl\tl\to"
x = txt.expandtabs(2)    #sets the tab size of string
print(x)


#8.Find()

name = "harshik , amitesh , harsh"
z = name.find("harshik")    #searches the string for a specified value and returns the position of where it was found
print(z)



#Negative index and its use

arr = [10, 20, 30, 40, 50]
print(arr[-1])
print(arr[-2])


# if else statement 

snow = 1

if snow == 1  :
    print("i will go out")
    
else :
    print("i will not go out")
    
    
    
rains_frogs = 1

if rains_frogs == 1 :
    print("i will dance")
    
else :
    print("i will not dance")
    



# tuples

myTuple = ("apple" , "pear" , "mango")
print(myTuple)

myTuple = ("apple" , "pear" , "mango")
print(myTuple[1])

myTuple = ("apple" , "pear" , "mango")
print(len(myTuple))


#To add values in tuple use + operator
    
myTuple = ("apple" , "pear" , "mango")

print(myTuple)

T1 = ("banana" ,) #the , is important

myTuple = T1 + myTuple

print(myTuple)



# infinite for loop

l = [1] #list name 
for x in l :
    l.append(x + 1) #append - adds an element in the end of the list
    print(x)




# dictionary methods

#1. clear()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
car.clear()
print()



#2. 

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
x = car.copy()
print(x)



#3. fromkeys()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
color = "blue"      
dict1 = dict.fromkeys(car,color)
print(dict1)





#4. get()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
x = car.get("year")
print(x)





#5. items()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
x  = car.items()
print(x)




#6. keys()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
x  = car.keys()
print(x)




#7. pop() / popitem()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
car.pop("year")
print(car)




#8. setdefault()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964" ,
       "color" : "blue"}
       
x = car.setdefault("color" , "red")
print(x)




#9. update()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
car.update({"color" : "white"})
print(car)



#10. values()

car = {"brand" : "ford" ,
       "model" : "mustang" ,
       "year" : "1964"}
       
x = car.values()
print(x)



#sets 
mySet = { "1" , "2" , "3" , "4"}
print(mySet)

mySet = { "1" , "2" , "3" , "4"}
print(len(mySet))

mySet = { "1" , "2" , "3" , "4"}
mySet.add("5")
print(mySet)

mySet = { "1" , "2" , "3" , "4"}
mySet.remove("3")
print(mySet)



#calculator program


def add(num1 , num2) :
    return num1 + num2
def subtract(num1 , num2) :
    return num1 - num2
def multiply(num1 , num2) :
    return num1 * num2
def divide(num1 , num2) :
    return num1 / num2

print("please select operation : " 
      "1. add "
      "2. subtract "
      "3. multiply "
      "4. divide ")
      
select = int(input("select operation : "))
number_1 = int(input("enter the first number : "))
number_2 = int(input("enter the second number : "))

if select == 1 :
    print("the sum is : " , number_1 + number_2)
    
elif select == 2 :
    print("the difference is : " , number_1 - number_2)
    
elif select == 3 :
    print("the product is : " , number_1 * number_2)
    
elif select == 4 :
    print("the quotient is : " , number_1 / number_2)

else :
    print("invalid input")
 


#step function in for loop 
for x in range(0, 12, 2) :  #0-start parameter , 12-stop parameter , 2-step parameter
    print(x)



#filename extension

x = str(input("what is the filename : "))

print("the extension of the file is : python")

        

#character mississippi 

count = {"M" : 0 , "I" : 0 , "S" : 0 , "P" : 0}

word = "MISSISSIPPI"

for i in word :
    if i == "M" :
        count["M"] = count["M"] + 1
        
    elif i == "I" :
        count["I"] = count["I"] + 1
        
    elif i == "S" :
        count["S"] = count["S"] + 1

    elif i == "P" :
        count["P"] = count["P"] + 1

print(count)
















