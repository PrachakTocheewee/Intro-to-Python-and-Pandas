# create variables
""""
income = 6500
expense=3200
saving= income-expense
print(saving)

# basic calculation
print(1+1)
print(33-21)
print(32*10)
print(9/3)
"""
"""
# print string (character, text)
print("Hello World")
print("Hello"+"Maria")
print("Hello"*10)
# f-string template
name = "Por"
age = 29
text= f"Hi my name is {name} and I am {age} years old."
print(text)
"""
"""
#datatypes
tprint(typeype(100))
print(typeType(167))
print(typetype("Por"))
print(type(true))

#compare values
print(10>5)
print(10<5)
print(10==5)
print(10!=5)    
"""
"""
#data structures
#list
my_list = [1,2,3,4,5]
print(my_list)  
#tuple
my_tuple = (1,2,3,4,5)
print(my_tuple)
#dictionary
my_dict = {"name":"Por","age":29,"city":"Bangkok"}
print(my_dict)
# index on python stars with 0
print(my_list[0])  # output: 1
print(my_tuple[0]) # output: 1
print(my_dict["name"]) # output: Por   
print(my_list[-1]) # output: 5 (last element)
print(my_tuple[-1]) # output: 5 (last element)
print(my_dict["age"]) # output: 29
print(my_dict["city"]) # output: Bangkok
my_list= my_list+[6,7,8,9,10]
print(my_list) # output: [1,2,3,4,5,6,7,8,9,10]
print(my_list[2:])
#len=length
print(len(my_list))
#type
print(type(my_list))
#method = funtions designed specifically for that type, class, object
my_list.append(11)
print(my_list)
my_list.remove(1)
print(my_list)
my_list.sort(reverse=True)
print(my_list)
"""
my_dict = {"name":"Por","age":29,"gender":"Male","city":"Bangkok","Favmovies":["The Arrivals","Mean Girls"],"Favbooks":["1984","Charlot's web"]}
print(my_dict)
# get vales from dictionary

print(my_dict["name"] )
print(my_dict["Favbooks"][1])
#update values in dictionary
#mutable object
my_dict["name"] = "PorPrachak"
print(my_dict["name"] )
print(my_dict["Favbooks"][0])
#check key in dictionary
print("name" in my_dict) # output: True
print("country" in my_dict) # output: False


#create new function
def greet(name):
    return f"Hello {name}!"
print(greet("Por"))
def greet2(name,age):
    return f"Hello {name}! You are {age} years old."
print(greet2("Por", 29))
#if else statement
def grader(score) :
    if score >= 90:
        return("Passes!")
    else:
        return("failed!") 
result =grader(95)
print(result)
#for loop
for i in my_dict:
    print(i) 
#in tro to OOP
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Move this out so it's at the same level as __init__
    def make_some_noise(self):
        print("I am very delicious!")

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old." 

# This will now work correctly!
person2=  Person("Nonny", 28)
print(person2.greet())
person3=  Person("Fah", 28)
print(person3.greet())
Por = Person("Por", 29)
print(Po.greet())
Por.make_some_noise()
Por.make_some_noise()                                    
