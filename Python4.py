print ("This is going to be a practice run")

print ("Good luck on your journey for this will be an in depth practice run.")

#1) We will continue to work on variables. A variables is a box and you have to give it a box that being a hypothical box. What is inside the box is that you can store values inside meaning you can store values inside of variables. 

#Values are inside of the variable. 

#Throughout this study, you will learn more about variables and learn about the specefic data types that are stored are inside the variables. 

#A variable is a placeholder where you can store things. 

name = "Nicolas" 

age = 20

occupation = ("TIL Independent Living")

years = (1) 

pi = 3.14 

number = [1,2,3,4,5,6,7,8]

#We can combine all of these things together 

name, age = "Nicolas", 20 

print(name)
print (age)
print (pi)
print(number)
print(occupation)
print (years)

#These are all the results of our variables. So throughout the learning, we will be working with variables. 

# 2) Naming variables 

name = "Dev"
fullName = "A Dev"
# You can also do the following variation: full_name = "A Dev"
AGE = "20"
PI = 3.14

#3 Data types

# When you define a variable, you must have to find a value. A value continues a data type 

brand = "Example" 
age = 1 
pi = 2.14
number = []
isAdult = True

print(type(brand))
print(type(number))
print(type(pi))
print(type(isAdult))
#boolean represents true or false. 

#4) Dynamically Type 

# The data type of any variable or function is random. Unlike other languages such as Java, the different is that with Java for example is that you have to specify the data type in Java while Python it is more accomdating. 

brand = "ExampleA"

# If you want to be explicit when defining your variables, you can do these two things:

brand: str = "ExampleB"

#The same applies with booleans

# Typically, you would do booleans like this 

isAdult = False

#To be more specefic you would do this. 

isAdult: bool = False

#What about methods? Well here is an example of a method that is very straightforward 

def hello(): 
    return "hello"

#In Java, you would do something a bit different, and makes it a bit challenging for beginners. 

# public String hello() {
#    return "hello"
# }

# Well we want to make this function turn towards a int 

def hello () -> int: 
    return 1
    