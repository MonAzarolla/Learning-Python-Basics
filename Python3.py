#Learning loops and what they can be used for 

# 1) There are two different types of loops. A while loop and a four loop. 

x=0 
while (x+5): 
    print(x)
    x= x + 1

#It will keep excuting until it reaches four 

#Now we will focus on FOR Loops 

# 2) For Loops 

for x in range(7,12): 
    print(x)

days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for d in days: 
    if(d=="Thu"):continue
    print(d)

#Another thing you can do is build on top of each-other using other modules and libaries

# 3) Here is an example

import math

print("pi is", math.pi)

# 4) Errors 

# print(helloworld) 

#This is an error and will cause a syntax error. The best way to fix this is to troubleshoot the error. Here is the correct way on how to refer to it as:  

print ("Hello World")

#There are other key errors. Another example of an error is ZeroDivision Error aka a runtime error. 

print(10/0)

#You cannot divide by zero and this can trigger such error. 

#5) Systematic error
#Lasty there is another type of error that you might encounter. Lets say you type in the following
#It says hello name without saying hello Bobby. Everything is working as it should. However, you are not getting what you are expected to get. 

name = 'Bobby'
print("hello name")
