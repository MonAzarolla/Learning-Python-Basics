#We will be doing comments.
#Comments descrive what the piece of code is doing or what it is doing all about. 

#What I am writting about are comments. 

print ("Hello, these are commands above.")

#Next we will talk about strings 

brand = "Example"

print(brand)

# Example in double quotes is a string. Strings are readable and easy to store. 

# With any given string, you also will have a ton of other methods 

brand = "Example"
print(brand.upper())

# Here is another example 

brand = "Example2"
print(brand.replace('A','33'))
print(len(brand))

# You can even compare strings 

print(brand != "Example2")

print ("code" in brand)

print ("code" not in brand)

# These are pretty much strings in a nutshell. 

comment = """Nicolas is cool
He is a really nice guy, and chill lol
"""

name = "Bob" 
email = f""" 
hello {name}, 
how are you?
It was nice talking to you
age {4 +4}
"""
print (email)

# Indentation 

# Python is very different from languages such as Java. 

name = "Bobby"
surname = "Bobert"

# You cannot indent this or it will cause issues. You could do it in Java, but not in Python. 

#Operators are a contruct that allows you to manupliate an object in Python. 

result = 1 + 2


print (result) 

print = (1 & 2)

print = (1/2)

print = (1 * 2)

print = (9 % 3)

print = (2 **2)

#Now we will be focusing on the Comparison Operators 

print = (10 > 5)

print (11 < 5)

print (10 >= 5)

print (10 != 10)

print (10 == 10)

print (10 <= 10)

# Logical Operators

# Logical operators allow us to combine mutiple expressions. 

print ((10 > 5) and 1 < 3  
        and "A" == "A")

# So this is the logical operator

print (67 < 64
       or 1 > 3
       or "B" == "B")

# Finally, let us do the last type of logical operator.

print (not("Mary" == "Harry")) 