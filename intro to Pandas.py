# Introduction to Pandas
# imorting the library
import pandas as pd
import numpy as np
# create data frame
data = {   "id":[1,2,3],
        "name":["Por","John","Jane"],
        "age":[29,30,28],
        "gender":["Male","Male","Female"],
        "city":["Bangkok","New York","London"],
        "passed_exam":[True,False,True]}

students = pd.DataFrame(data)
#print(students)
#students.head() # show the first 5 rows
#students.tail() # show the last 5 rows
#filtering data
"""students[students["gender"]=="Male"] # show the gender
students(students["age"]>=20) # show the students whose age is greater than 29
students(students["passed_exam"]==True) # show the students who passed the exam
students[students["passed_exam"]==True] # show the students who passed the exam"""
# --- Filtering Data ---
"""
# 1. Show only students who passed the exam
print("Students who passed:")
print(students[students["passed_exam"] == True])

# 2. Show students older than 28
print("\nStudents older than 28:")
print(students[students["age"] > 28])

# 3. Show only Male students
#print("\nMale students:")
#print(students[students["gender"] == "Male"])

#querying data
#students.query("age > 28") # show the students whose age is greater than 28
#students.query("passed_exam == True") # show the students who passed the exam

#students.query("age >= 28 and passed_exam == True") # show the students whose age is greater than 28 and passed the exam
      """
#select columns
students[['name', 'age']] # show the name and age columns
# To see the name and age columns in your terminal
print(students[["name", "age"]])
print(students[["name", "age"]])