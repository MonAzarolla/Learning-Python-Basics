#Day 1 (3/18/2023)

# 1) This is me practicing with my programming and these two things print some texts

print ("Hello World, I am getting started")

print ("This is my first time using python. I hope you tag along with me in my journey")

# 2) This is me trying to add some numbers using python 

1 + 2

4 * 4

10/5

# 3) This is me using python and print to calculate or see how python reacts with numbers using prints

print (5%2)

print (1000)

# 4) More experimental words using the print function lol

print ("Whats up")

print ('Whats up')

print ("whats's up")

# 5) Additional notes 
# a variable can hold additional values. The variable must contain letters or underscores. The variables names are case sensitive, and cannot be keywords 

big_dog = "Max"

print (big_dog)

# This is a clear example of a variable where I assign big_dog (the variable) as Max

# So what data type can assign the variable, well lets try to assign it 10. 

big_dog= "Max"

big_dog = 10

print(big_dog)

# 6) Let us go on to the next step. We will request an input and you can take that input and assign it a variable. 

big_dog = input("What size is the big dog")
print(big_dog) 

# 7 ) Let us ask a question to python. Does 7 equal to 9 

print (7==9) 

# The input we get is false because of course that 7 does not equal to 9! 

# 8) What is my age \

Monroe_Age = 20 
Age_in_College = 19
print (Monroe_Age = Age_in_College)

# 9) Now we will be using if statements 
Monroe_Age = 20 
Age_in_College = 19

if Monroe_Age < Age_in_College: 
    print ("Monroe is not 19 anymore, and has gotten older.")
elif Monroe_Age == Age_in_College: 
    print ("You will graduate if you continue working harder.")
else: 
    print("If Monroe is not 20, they are lying, and should be in college.")

# 10) Learning how to use functions in Python

# We have already been using functions such as functions. This is a basic example of functions we have been using, and we can create our own functions 

print ("Monroe is gonna be successful as long as they stick to learning, and not be lazy")

def print_Monroe(): 
    text = "Monroe is a hard worker, and wants to learn Python."
    print (text)
    print(text)
    print(text)

# 11) We have our function now, but we cannot run it. We have not called the function

def print_Monroe(): 
    text = "Monroe is a hard worker, and wants to learn Python."
    print (text)
    print(text)
    print(text) 

    print_Monroe()