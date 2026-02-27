# DATA TYPE LEARNING SECTION

x = 10        # number
name = "Ram"  # text


# int
a = 10
print(type(a)) # output = <class 'int'>


# float
b = 3.14
print(type(b)) # output = <class 'float'>


#string
c = "Surya"
print(type(c)) # output = <class 'str'>


# boolean
# boolean only two type 1.True,2.False
is_student = True
print(type(is_student)) # output = <class 'bool'>


#List(list)
names = ["Surya","Chandra","Basudev","Krishna"]
roll_no = [1,2,3,4]
print(names[3]) # output = Krishna
print(type(names))
print(type(roll_no))
# list is mutabel,means we can change the value of every current list value.
# example
names[3] = "Chandu"
print(names[3]) # output = Chandu


#Tuple(tuple)
names = ("Surya","Chandra","Basudev","Krishna")
roll_no = (1,2,3,4)
print(names[3]) # output = Krishna
print(type(names))
print(type(roll_no)) 
# tuple is just like list but we can not change the tuple value just like list,means tuple is imutable.


# Dictionary (dict)
# Stores data in key : value pair.
student_info = {
    "name":"Surya",
    "class":"xii",
    "roll_no":1,
    "stream":"science"
}
print(student_info)
print(student_info["name"]) # output = Surya
print(type(student_info))


# Type Conversion (Casting)
# Convert one type → another.
a = 3.00
b = int(a)
print(b) 
print(type(b)) # output = <class 'int'>

p = 10
q = float(p)
print(q) 
print(type(q)) # output = <class 'float'>

x = "10"
y = int(x)
print
print(type(y)) # output = <class 'int'>


# Quick Memory Trick: # Numbers → int, float
                      # Text → str
                      # Logic → bool
                      # Collection → list, tuple, dict





# DATA TYPE QUESTIONS PRACTICE SECTION

# Q.1
# Create variables:
# age (int)
# height (float)
# name (string)
# student (boolean)

# Print their types.

age = 20
print(type(age))

height = 5.5
print(type(height))

name = "Surya"
print(type(name))

student = True
print(type(student))


# Q.2
# Convert "50" into integer and add 10.

a = int("50")
print(a+10) # 60


# Q.3
# Create a list of 5 numbers and print the 3rd number.

number_list = [10,20,30,40,50]
print(number_list[2]) # 30


# Q.4 
# Create dictionary: name → your name
                   # city → your city
                   # age → your age

my_info  = {
    "name":"Suryakanta",
    "city":"Bhubaneswar",
    "age" :20
}
print(my_info)
# now print only the name.
print(my_info["name"])


# Q.5
# convert "100" into integer and multiple by 2.

a = int("100")
print(a*2) # 200


# Q.6
# create a list containing: 10, 3.5, "Python", True
# Print the datatype of each element.

list = [10,3.5,"Python",True]
print(type(list[0]))
print(type(list[1]))
print(type(list[2]))
print(type(list[3]))


# Q.7
# Create a tuple with 5 numbers and print: first element & last element

number = (10,20,30,40,50)
print(number[0])
print(number[4])


# Q.8
# Create dictionary:
   #  name → your name
   #  age → your age 
   # course → Python
# print olny course.

dict = {
    "name":"Surya",
    "age":20,
    "course":"Python"
}
print(dict['course'])


# Q.9
# a = "25"
# b = "5"
# Convert both into integers and print: a devided by b

a = int("25")
b = int("5")
print(a/b)


# Q.10
# Convert these values into string:10,3.14,True and Print their types after conversion.

a = str("10")
b = str("3.14")
c = str("True")
print(type(a))
print(type(b))
print(type(c))


# Q.11
# Take name and age from user and store them in a dictionary:
# Print datatype of:
# dictionary
# name value
# age value

dict = {
    "name":"Surya",
    "age":20,
}
print(dict)
print(type(dict['name']))
print(type(dict['age']))


# Q.12
# Create this list: data = [25, "Python", 3.14, False, [1,2,3]]
# Your tasks: Print datatype of the whole list.
# Print datatype of each element using indexing.
# Print datatype of the last element’s first value.

data = [25,"Python",3.14,False,[1,2,3]]
print(type(data))

print(type(data[0]))
print(type(data[1]))
print(type(data[2]))
print(type(data[3]))
print(type(data[4]))

print(type(data[4][0]))


# Q.13
# Take input number from user:
# Now: 
# Convert it to int
# Convert it to float
# Convert it to string
# Print all values with their types

num = input("Enter your number: ")

a = int(num)
b = float(num)
c = str(num)

print(a, type(a))
print(b, type(b))
print(c, type(c))


# Q.14
# create a dictionary:
# student details: name → your name
                 # marks → list of 3 marks
                 # passed → True/False
# Tasks:
# Print second mark.
# Print datatype of marks.
# Calculate total marks using list values.

student_details = {
    "name":"Surya",
    "marks":[87,90,79],
    "passsed":True
}
print(student_details['marks'][1])
print(type(student_details['marks']))
# print(student_details['marks'][0] + student_details['marks'][1] + student_details['marks'][2]  )
print(sum(student_details["marks"]))


