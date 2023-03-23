# When you start writting applications with Python, you will write things in certain conditions 

# If Statements 

number = 19

if number > 1:
    print(f"number {number} is positive")
else: 
    print("f{number} is negative")

#Another If Statement 

elif number == 0:
print (number)
else: 
print(f"{number} is negative") 

# 2) Tenary If Statements

if number > 0: 
    print("positive")
else: 
    print("0 or negative")

    message = "positive" if number > 0 else "0 or negative"

# Lists 

print (type([])) 

#right here, we have this variable known as number:  

number = 1 

number_two = 2 

number_three = 3

# What we can do is collapse all these three numbers in the following 

numbers =[1,2,3,4]

# Now this is the list that contains all of those numbers. If you want you can even add a statement in it or other stuff

numbers = [1,2,3,4,-1,0]

numbers = [1,2,3,4, "A"]
print(numbers)

# How do you find the index of a number and make sure that the list that is run will bring up one number? 

numbers = [1,2,3,4]
print(number[2])

# Deleting Items From List 

numbers.remove(1)

numbers.remove(-20)

numbers.remove(66)

print (numbers)

numbers.pop() # also removes it 

del numbers[0] # deletes 

print (numbers)

del numbers[0:3] #this can delete from a range from 0 to 3 

# This other one can remove even more numbers 

del numbers[1:20]

# Sets 

#Sets are similar to lists, but with sets duplicates are not allowed

numbersList = [1,1]

numbersSet = {1,1}

print(numbersList)

print (numbersSet)

# Duplicates are not allowed in sets. 

# You can clear, add or remove

print(numbersSet.pop) #removes

print (numbersSet.add) # You can add

# You can also have a letter set 

lettersSet = {"A","B","C","D"}

print(lettersSet)

# Sets is curly braclets while lists are square brackets. 